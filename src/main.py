from src.collectors.telegram_collector import TelegramCollector
from src.summarizer.summarizer import Summarizer
# from .storage.db import DB
# from .outputs.telegram_sender import send_summary

def main():
    collected = TelegramCollector().fetch_new()
    summarization = Summarizer().summarize(collected)
    for channel_name, (_, result) in summarization.items():
        print(channel_name, ":\n", result)
        # summaries = Summarizer().summarize_many(cleaned)
        # DB().save_summaries(summaries)
        # send_summary(summaries)

if __name__ == "__main__":
    main()


    