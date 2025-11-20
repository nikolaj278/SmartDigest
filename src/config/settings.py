import os
from dotenv import load_dotenv

load_dotenv()  # reads .env
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_NAME = "my_session"
