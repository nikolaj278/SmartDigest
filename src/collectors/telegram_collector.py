import pandas as pd

from telethon.sync import TelegramClient
from src.config.settings import SESSION_NAME, API_ID, API_HASH

class TelegramCollector:
    def __init__(self, ):
        self.client = TelegramClient(SESSION_NAME, API_ID,API_HASH)
        

    def fetch_new(self):
        with self.client:
            dialogs = self.client.get_dialogs()
            channels = [d for d in dialogs if type(d.entity).__name__ == "Channel"]
            posts = [self.client.get_messages(c, limit=c.unread_count) for c in channels]
            return {channels[i].name: pd.DataFrame({"id": [p.id for p in posts[i]],
                                            "author": [p.sender_id for p in posts[i]],
                                            "text": [p.text for p in posts[i]]
                                           })
                    for i in range(len(channels))
                   }
        
        