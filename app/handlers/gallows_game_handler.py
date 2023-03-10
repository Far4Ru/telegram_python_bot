from app.markup.gallows_game_markup import GallowsGameMarkup
from random import randint


class GallowsGameHandler:
    def __init__(self, bot):
        self.bot = bot

    def rules(self, message):
        if message.text == 'Да':
            self.bot.send_message(message.chat.id, '''Тебе даётся 10 попыток для того, чтобы угадать слово. За 
            каждую ошибку к виселице пририсовывается часть человечка. Когда человечек будет полностью нарисован 
            -- игра заканчивается.''',
                                  reply_markup=GallowsGameMarkup.accept_or_reject())
            self.bot.register_next_step_handler(message, self.start)
        elif message.text == 'Нет':
            self.bot.send_message(message.chat.id, 'да ты умник, я смотрю',
                                  reply_markup=GallowsGameMarkup.accept_or_reject())
            self.bot.register_next_step_handler(message, self.start)

    def start(self, message):
        if message.text == 'Вперёд!':
            self.bot.send_message(message.chat.id, 'тут начинается виселица')
            self.bot.register_next_step_handler(message, self.game)
        elif message.text == 'Я передумал':
            self.bot.send_message(message.chat.id, 'Как скажешь')

    def game(self, message):
        pass
