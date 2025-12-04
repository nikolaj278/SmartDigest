from src.collectors.telegram_collector import TelegramCollector
from src.outputs.telegram_sender import send_summary
from src.storage.data_base import DB
from src.summarizer.llm_summarizer import Summarizer



def main():
    # fetch new messages from telegram
    collected = TelegramCollector().fetch_new()
    #continue only if there are new messages 
    if collected is not None:
        # DB().save_messages(collected)
        ## send prompt+messages to LLM 
        summaries = Summarizer().summarize(collected)
        # DB().save_summaries(summaries)
        ## send summaries of channel content with telegram bot
        send_summary(summaries)

if __name__ == "__main__":
    main()


    