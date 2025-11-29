import os
from dotenv import load_dotenv

load_dotenv()  # reads .env file

# to initialize telegram client
TG_API_ID = int(os.getenv("TG_API_ID"))
TG_API_HASH = os.getenv("TG_API_HASH")
SESSION_NAME = "my_session"

# deepseek api
DS_API_KEY = os.getenv("DS_API_KEY")

COMMAND = """Summarise the following Telegram content. Messages are grouped by “Telegram user name or channel owner name:” followed by their text. Determine whether it is a conversation or separate posts. If it is a conversation, mention every participant by name in the summary. Choose the format (paragraph, bullets, or numbered points) that best fits the content. Output only the summary text, with no explanations, labels, system prompts, or additional comments.\nThe text:\n
"""
