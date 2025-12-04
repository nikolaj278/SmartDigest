from langdetect import detect

from emoji import replace_emoji

from telethon.sync import TelegramClient

from src.config.settings import SESSION_NAME, TG_API_ID, TG_API_HASH, EXCLUDE
from src.storage.models import MessageItem

class TelegramCollector:

    """
    Define an object which initializes a client to connect to telegram, 
    fetches mesasges and sorts for channel posts only.
    """
    
    def __init__(self, ):
        self.client = TelegramClient(SESSION_NAME, TG_API_ID, TG_API_HASH)
        

    def fetch_new(self, nr_posts=None, mark_read=True):
        with self.client:
            dialogs = self.client.get_dialogs()
            # list channels excluding those written in .env file
            channels = [d for d in dialogs if (type(d.entity).__name__ == "Channel") 
                                          and (d.id not in EXCLUDE)]
            fetched_msgs = {}
            for ch in channels:
                # take explicitely defined nr of posts per channel or all unread posts
                unread = nr_posts if nr_posts else ch.unread_count 
                if unread == 0:
                    continue
                msgs = self.client.get_messages(ch, limit=unread)
                msg_objects = [
                     MessageItem(
                        msg_id=m.id,
                        channel_name=ch.name,
                        channel_id=ch.id,
                        # use name if author has a name else "user nr. {sender_id}"
                        author_name=m.sender.username if m.sender.username 
                                                      else "User nr." + str(m.sender_id),
                        author_id=m.sender_id,
                        text=m.text,
                        language=detect(m.text),
                        date=m.date,
                        raw=m
                    )
                    for m in msgs
                    # skip empty or emoji only strings
                    if replace_emoji(m.text, "") 
                ]
                # if there are new messages containing text
                if msg_objects:
                    # write messeges to a dictionary with tuples of channel name and id as keys
                    fetched_msgs[(ch.name, ch.id)] = msg_objects
                # Mark that message (and everything before it) as read
                if mark_read:
                    self.client.send_read_acknowledge(ch, msgs[0])
            
            # if there is not a single new message among all channels return None
            return fetched_msgs if fetched_msgs else None
        
if __name__=="__main__":
    print(TelegramCollector().fetch_new(nr_posts=1, mark_read=False))




