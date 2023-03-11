from app.markup.numerical_guessing_game_markup import NumericalGuessingGameMarkup
from random import randint


class NumericalGuessingGameHandler:
    def __init__(self, bot):
        self.bot = bot

    def rules(self, message):
        if message.text == 'Да':
            self.bot.send_message(message.chat.id, '''Всё просто: бот загадывает цифру от 1 до 10, твоя задача -- 
            отгадать её. Приступим?''', reply_markup=NumericalGuessingGameMarkup.go_or_back())
            self.bot.register_next_step_handler(message, self.start)
        elif message.text == 'Нет':
            self.bot.send_message(message.chat.id, 'да ты умник, я смотрю',
                                  reply_markup=NumericalGuessingGameMarkup.go_or_back())
            self.bot.register_next_step_handler(message, self.start)

    def start(self, message):
        if message.text == 'Вперёд!':
            self.bot.send_message(message.chat.id, 'Бот загадал цифру!')
            self.bot.register_next_step_handler(message, self.game)
        elif message.text == 'Я передумал':
            self.bot.send_message(message.chat.id, 'Как скажешь')

    def game(self, message):
        bot_number = randint(1, 10)
        self.bot.send_message(message.chat.id, 'Твоё предположение?')
        self.guess(message, bot_number)

    def guess(self, message, bot_number):
        try:
            user_number = int(message.text)
        except ValueError:
            self.bot.send_message(message.chat.id, 'Введите число')
            self.bot.register_next_step_handler(message, self.guess, bot_number)
            return
        if user_number < bot_number:
            self.bot.send_message(message.chat.id, 'Маловато')
            self.bot.register_next_step_handler(message, self.guess, bot_number)
        elif user_number > bot_number:
            self.bot.send_message(message.chat.id, 'Многовато')
            self.bot.register_next_step_handler(message, self.guess, bot_number)
        elif user_number == bot_number:
            self.bot.send_message(message.chat.id, 'Ты угадал!')
            self.bot.send_message(message.chat.id, 'Хочешь сыграть ещё раз?',
                                  reply_markup=NumericalGuessingGameMarkup.accept_or_reject())
            self.bot.register_next_step_handler(message, self.game_again)

    def game_again(self, message):
        if message.text == 'Да':
            self.bot.register_next_step_handler(message, self.game)
        elif message.text == 'Нет':
            self.bot.send_message(message.chat.id, 'Очень жаль. Возвращайся, когда появится желание.')
