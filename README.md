# SmartDigest

## Description  
SmartDigest is a service which collects new posts from Telegram channels , summarises them using DeepSeek and sends reports daily or more often if it is required.
It is useful for a person who is using telegram and wants to choose spend their time in a "smart" way by firstly reading short summaries to decide if the content is worth to spend time on.


## Installation  
To set up this service you need to copy the repo and use your own machine to get required secrete variables.

1) Copy the repo. 

2) Go to the repo then to "settings" sections, on the left side bar find "Secretes and variables" then click "Actions". By clicking "New repository secrete" you can add all the secrete variables. Enter the variable name and its value. The names must not be changed or code will not work otherwise!

3) Get and fill in required secrete variables:

- TG_API_ID, TG_API_HASH: follow the gide on  https://docs.telethon.dev/en/stable/basic/signing-in.html
- TG_SESSION : Go the environment where you code in python.
Run: 

```bash
pip install python-telegram-bot telethon asyncio
```

Run the code below. It will request the phone number of you telegram account. The string printed out will be the TG_SESSION value.

```python
import os
from telethon import TelegramClient
from telethon.sessions import StringSession

api_id = TG_API_ID
api_hash = TG_API_HASH

client = TelegramClient(StringSession(), api_id, api_hash)
await client.start()
print(client.session.save())
```

- TG_BOT_TOKEN:
Go to Telegram and look for @BotFather. Issue the /newbot command and follow instructions. You will receive a bot token. Don't share it with anyone and treat it like a password!
- TG_CHAT_ID:
The bot will appear in your chat list. Send any message to it. Then go to  environment where you code in python and run:

```python
import os
import requests

TOKEN = TG_BOT_TOKEN
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
resp = requests.get(url)
print(resp.json()['result'][0]['message']['chat']['id'])
```

The number you will receive is the TG_CHAT_ID value.

- EXCLUDE (chat ids you would not like to receive sumarizations from):
Run:

```python
dialogs = await client.get_dialogs()
channels = [d for d in dialogs if (type(d.entity).__name__ == "Channel")]
for ch in channels:
    print("{: <20}{}".format(ch.id, ch.name))
```

You will see chat ids and names. Find the chats you would like to exclude from summarisation and add ids to EXCLUDE value (Minuses must be included!). if you have more then one such chat, then write separating them with comma, like: -123, -146, -198.


- DS_API_KEY:
Go to https://platform.deepseek.com/profile and login. Top up and create an API key.

4) Check if everything works
Run the service  manually:
Go back to the repository. Find "Actions" on the top bar. Then Click "SmartDigest Daily" on left side bar. Press "Run workflow" button and then press green "Run workflow" button. 
If there were some new posts in telegram then you will receive their summarized versions  from the bot you created.


## Usage
The service will run once per day at 12:00 am by UTC time. If you want to adjust the sending time then go to repository then choose "Code" section on teh top bar. Go to .github/workflow/. Open main.yml file. Fine row number 5: - cron: '0 12 * * *'. 0 show minutes and 12 show hours. Hours can be changed from 0 to 23.  If you want to add time of activation of service, then copy - cron: '0 12 * * *' and paste it below the existing one and set the time.

## Tech Stack / Built With
Languages: 
- Python 3.10

Packages: 
- asyncio
- emoji
- langdetect
- openai
- python-dotenv
- sqlite3
- python-telegram-bot
- telethon

##  License
MIT License  
See `LICENSE` file for details.



