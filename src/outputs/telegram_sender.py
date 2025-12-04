import asyncio

from telegram import Bot

from src.config.settings import TG_BOT_TOKEN, TG_CHAT_ID


bot = Bot(token=TG_BOT_TOKEN)

async def send_all(summaries):
    for (ch_name, _), (_, summary) in summaries.items():
        await bot.send_message(chat_id=TG_CHAT_ID, 
                               text=ch_name + ":\n\n" + summary)


def send_summary(summaries):
    asyncio.run(send_all(summaries))


if __name__=="__main__":
    send_summary("Testing how does the telegram bot work.")