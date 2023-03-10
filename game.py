from random import randint

from telebot import types, TeleBot


class Game:

    def __init__(self, token):
        self.bot = TeleBot(token)
        self.init_messages()

    def init_messages(self):
        @self.bot.message_handler(commands=['start'])  # отслеживает получаемые человеком сообщения и сверяет со списком
        def start(message):  # message -- то, что вводит пользователь
            self.bot.send_message(message.chat.id, 'Привет! Если ты не знаешь, как работает этот бот -- набери '
                                                   'команду /help.')

        @self.bot.message_handler(commands=['help'])
        def help(message):
            self.bot.send_message(message.chat.id, '''Этот бот может предоставить на выбор две игры: числовая 
            угадайка и виселица. Для выбора какой-либо из них набери команду /game, затем -- на кнопках отобразятся 
            названия игр. /start -- запустить бота /help -- краткая инструкция по работе /game -- начало игры''')

        @self.bot.message_handler(commands=['game'])
        def game(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            first_game = types.KeyboardButton('Числовая угадайка')
            second_game = types.KeyboardButton('Виселица')
            markup.add(first_game, second_game)
            self.bot.send_message(message.chat.id, 'Выбери игру, в которую хочешь сыграть.', reply_markup=markup)

        @self.bot.message_handler()
        def game(message):
            if message.text == 'Числовая угадайка':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                rule_yes = types.KeyboardButton('Да')
                rule_no = types.KeyboardButton('Нет')
                markup.add(rule_yes, rule_no)
                self.bot.send_message(message.chat.id,
                                      'Добро пожаловать в числовую угадайку! Ознакомишься с правилами?',
                                      reply_markup=markup)
                self.bot.register_next_step_handler(message, rules_first)
            elif message.text == 'Виселица':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                rule_yes = types.KeyboardButton('Да')
                rule_no = types.KeyboardButton('Нет')
                markup.add(rule_yes, rule_no)
                self.bot.send_message(message.chat.id, 'Добро пожаловать в виселицу! Ознакомишься с правилами?',
                                      reply_markup=markup)
                self.bot.register_next_step_handler(message, rules_second)

        @self.bot.message_handler()
        def rules_first(message):
            if message.text == 'Да':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                rule_go = types.KeyboardButton('Вперёд!')
                rule_back = types.KeyboardButton('Я передумал')
                markup.add(rule_go, rule_back)
                self.bot.send_message(message.chat.id, '''Всё просто: бот загадывает цифру от 1 до 10, твоя задача -- 
                отгадать её. Приступим?''', reply_markup=markup)
                self.bot.register_next_step_handler(message, start_game_first)
            elif message.text == 'Нет':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                rule_go = types.KeyboardButton('Вперёд!')
                rule_back = types.KeyboardButton('Я передумал')
                markup.add(rule_go, rule_back)
                self.bot.send_message(message.chat.id, 'да ты умник, я смотрю', reply_markup=markup)
                self.bot.register_next_step_handler(message, start_game_first)

        @self.bot.message_handler()
        def rules_second(message):
            if message.text == 'Да':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                rule_yes = types.KeyboardButton('Вперёд!')
                rule_no = types.KeyboardButton('Я передумал')
                markup.add(rule_yes, rule_no)
                self.bot.send_message(message.chat.id, '''Тебе даётся 10 попыток для того, чтобы угадать слово. За 
                каждую ошибку к виселице пририсовывается часть человечка. Когда человечек будет полностью нарисован 
                -- игра заканчивается.''',
                                      reply_markup=markup)
                self.bot.register_next_step_handler(message, start_game_second)
            elif message.text == 'Нет':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                rule_yes = types.KeyboardButton('Вперёд!')
                rule_no = types.KeyboardButton('Я передумал')
                markup.add(rule_yes, rule_no)
                self.bot.send_message(message.chat.id, 'да ты умник, я смотрю', reply_markup=markup)
                self.bot.register_next_step_handler(message, start_game_second)

        @self.bot.message_handler()
        def start_game_first(message):
            if message.text == 'Вперёд!':
                self.bot.send_message(message.chat.id, 'Бот загадал цифру!')
                self.bot.register_next_step_handler(message, game_first)
            elif message.text == 'Я передумал':
                self.bot.send_message(message.chat.id, 'Как скажешь')

        @self.bot.message_handler()
        def start_game_second(message):
            if message.text == 'Вперёд!':
                self.bot.send_message(message.chat.id, 'тут начинается виселица')
            elif message.text == 'Я передумал':
                self.bot.send_message(message.chat.id, 'Как скажешь')

        @self.bot.message_handler()
        def game_first(message):
            bot_number = randint(1, 10)
            while message.text != bot_number:
                self.bot.send_message(message.chat.id, 'Твоё предположение?')
                user_number = message.text
                if int(user_number) < bot_number:
                    self.bot.send_message(message.chat.id, 'Маловато')
                elif int(user_number) > bot_number:
                    self.bot.send_message(message.chat.id, 'Многовато')
                else:
                    self.bot.send_message(message.chat.id, 'Ты угадал!')
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                    rule_yes = types.KeyboardButton('Да')
                    rule_no = types.KeyboardButton('Нет')
                    markup.add(rule_yes, rule_no)
                    self.bot.send_message(message.chat.id, 'Хочешь сыграть ещё раз?', reply_markup=markup)
                    self.bot.register_next_step_handler(message, game_again)
                break

        @self.bot.message_handler()
        def game_again(message):
            if message.text == 'Да':
                self.bot.register_next_step_handler(message, game_first)
            elif message.text == 'Нет':
                self.bot.send_message(message, 'Очень жаль. Возвращайся, когда появится желание.')

        @self.bot.message_handler()
        def game1(message):
            if message.text.lower() == 'yes':
                self.bot.send_message(message.chat.id, 'тогда приступим')

                number = randint(1, 10)
                self.bot.send_message(message.chat.id, 'число загадано')
                self.bot.send_message(message.chat.id, 'введи число')

                user_number = message.text
                if user_number.isnumeric:
                    while int(user_number) != number:
                        if int(user_number) < number:
                            self.bot.send_message(message.chat.id, 'мало')
                        elif int(user_number) > number:
                            self.bot.send_message(message.chat.id, 'много')
                        elif int(user_number) == number:
                            self.bot.send_message(message.chat.id, 'ты угадал, хочешь сыграть ещё раз?')
                            self.bot.register_next_step_handler(message, game)
                else:
                    self.bot.send_message(message.chat.id, 'это не число')

    def start(self):
        self.bot.polling(none_stop=True)
