from telebot import TeleBot

from app.handlers.bot_handler import BotHandler


class Bot:

    def __init__(self, token):
        self.bot = TeleBot(token)
        BotHandler(self.bot)

    def start(self):
        self.bot.polling(none_stop=True)
