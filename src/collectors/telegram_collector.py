from langdetect import detect_langs

from telethon.sync import TelegramClient

from src.config.settings import SESSION_NAME, TG_API_ID, TG_API_HASH
from src.storage.models import MessageItem

class TelegramCollector:

    """
    Define an object which initializes a client to connect to telegram, 
    fetches mesasges and sorts for channel posts only.
    """
    
    def __init__(self, ):
        self.client = TelegramClient(SESSION_NAME, TG_API_ID, TG_API_HASH)
        

    def fetch_new(self, nr_channels=None):
        with self.client:
            dialogs = self.client.get_dialogs()
            channels = [d for d in dialogs if type(d.entity).__name__ == "Channel"]

            fetched_msgs = {}
            # limit the nr of channels to read
            lim = nr_channels if nr_channels else len(channels)
            for ch in channels[:lim]:
                unread = ch.unread_count
                if unread == 0:
                    continue
                msgs = self.client.get_messages(ch, limit=unread)
                # write messeges to a dictionary with channel names as keys
                fetched_msgs[ch.name] = [
                     MessageItem(
                        msg_id=m.id,
                        author_id=m.sender_id,
                        author_name=getattr(m, "author_name", "User nr." + str(m.sender_id)),
                        text=m.text,
                        cleaned_text=None,
                        language=None,
                        # language=[ll.lang if m.text else None for ll in detect_langs(m.text)],
                        date=m.date,
                        raw=m
                    )
                    for m in msgs
                    if m.text is not None
                ]
                # Mark that message (and everything before it) as read
                self.client.send_read_acknowledge(ch, msgs[0])

                
            return fetched_msgs
        

#mark read messages as read if. If channel is marked as special than it's messages won't be marked as read




