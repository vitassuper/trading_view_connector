import sys
from telegram import Bot, TelegramError

from src.core.config import settings


class Notifier:
    def __init__(self):
        self.bot = Bot(settings.TELEGRAM_BOT_TOKEN)
        self.exchange_name = 'OKX'

    def send_warning_notification(self, text):
        self.send_message(f"🚨{text}")

    def send_notification(self, text, chatId=None):
        self.send_message(text, chatId)

    def send_message(self, text, chatId=None):
        try:
            text = f"{self.exchange_name}:\n{text}"

            if chatId:
                self.bot.send_message(chatId, text)
            else:
                self.bot.send_message(settings.TELEGRAM_CHAT_ID, text)
                self.bot.send_message(settings.TELEGRAM_CHAT_ID2, text)
        except TelegramError as error:
            print(error.message, file=sys.stderr)