from src.collectors.telegram_collector import TelegramCollector


data = TelegramCollector().fetch_new()
if data != None:
    print(data['жертвы альтушек и четвертый'])