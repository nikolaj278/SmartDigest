from dataclasses import dataclass
from datetime import datetime


@dataclass
class MessageItem:
    msg_id: int
    author_id: int 
    author_name: str 
    text: str 
    cleaned_text: str | None
    language: str | None
    date: datetime
    raw: object