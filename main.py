import telebot
from random import *
from telebot import types

bot = telebot.TeleBot('***')

@bot.message_handler(commands=['start'])  # отслеживает получаемые человеком сообщения и сверяет со списком
def start(message):  # message -- то, что вводит пользователь
    bot.send_message(message.chat.id, 'Привет! Если ты не знаешь, как работает этот бот -- набери команду /help.')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '''Этот бот может предоставить на выбор две игры: числовая угадайка и виселица.
Для выбора какой-либо из них набери команду /game, затем -- на кнопках отобразятся названия игр.
/start -- запустить бота
/help -- краткая инструкция по работе
/game -- начало игры''')

@bot.message_handler(commands=['game'])
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    first_game = types.KeyboardButton('Числовая угадайка')
    second_game = types.KeyboardButton('Виселица')
    markup.add(first_game, second_game)
    bot.send_message(message.chat.id, 'Выбери игру, в которую хочешь сыграть.', reply_markup=markup)

@bot.message_handler()
def game(message):
    if message.text == 'Числовая угадайка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        rule_yes = types.KeyboardButton('Да')
        rule_no = types.KeyboardButton('Нет')
        markup.add(rule_yes, rule_no)
        bot.send_message(message.chat.id, 'Добро пожаловать в числовую угадайку! Ознакомишься с правилами?', reply_markup=markup)
        bot.register_next_step_handler(message, rules_first)
    elif message.text == 'Виселица':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        rule_yes = types.KeyboardButton('Да')
        rule_no = types.KeyboardButton('Нет')
        markup.add(rule_yes, rule_no)
        bot.send_message(message.chat.id, 'Добро пожаловать в виселицу! Ознакомишься с правилами?', reply_markup=markup)
        bot.register_next_step_handler(message, rules_second)

@bot.message_handler()
def rules_first(message):
    if message.text == 'Да':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        rule_go = types.KeyboardButton('Вперёд!')
        rule_back = types.KeyboardButton('Я передумал')
        markup.add(rule_go, rule_back)
        bot.send_message(message.chat.id, '''Всё просто: бот загадывает цифру от 1 до 10, твоя задача -- отгадать её.
Приступим?''', reply_markup=markup)
        bot.register_next_step_handler(message, game_first)
    elif message.text == 'Нет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        rule_go = types.KeyboardButton('Вперёд!')
        rule_back = types.KeyboardButton('Я передумал')
        markup.add(rule_go, rule_back)
        bot.send_message(message.chat.id, 'да ты умник, я смотрю', reply_markup=markup)
        bot.register_next_step_handler(message, game_first)

@bot.message_handler()
def rules_second(message):
    if message.text == 'Да':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        rule_yes = types.KeyboardButton('Вперёд!')
        rule_no = types.KeyboardButton('Я передумал')
        markup.add(rule_yes, rule_no)
        bot.send_message(message.chat.id, '''Тебе даётся 10 попыток для того, чтобы угадать слово.
За каждую ошибку к виселице пририсовывается часть человечка. Когда человечек будет полностью нарисован -- игра заканчивается.''', reply_markup=markup)
        bot.register_next_step_handler(message, game_second)
    elif message.text == 'Нет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        rule_yes = types.KeyboardButton('Вперёд!')
        rule_no = types.KeyboardButton('Я передумал')
        markup.add(rule_yes, rule_no)
        bot.send_message(message.chat.id, 'да ты умник, я смотрю', reply_markup=markup)
        bot.register_next_step_handler(message, game_second)

@bot.message_handler()
def game_first(message):
    if message.text == 'Вперёд!':
        bot.send_message(message.chat.id, 'тут начинается числовая угадайка')
    elif message.text == 'Я передумал':
        bot.send_message(message.chat.id, 'Как скажешь')

@bot.message_handler()
def game_second(message):
    if message.text == 'Вперёд!':
        bot.send_message(message.chat.id, 'тут начинается виселица')
    elif message.text == 'Я передумал':
        bot.send_message(message.chat.id, 'Как скажешь')

@bot.message_handler()
def game1(message):
    if message.text.lower() == 'yes':
        bot.send_message(message.chat.id, 'тогда приступим')

        number = randint(1, 10)
        bot.send_message(message.chat.id, 'число загадано')
        bot.send_message(message.chat.id, 'введи число')

        user_number = message.text
        if user_number.isnumeric:
            while int(user_number) != number:
                if int(user_number) < number:
                    bot.send_message(message.chat.id, 'мало')
                elif int(user_number) > number:
                    bot.send_message(message.chat.id, 'много')
                elif int(user_number) == number:
                    bot.send_message(message.chat.id, 'ты угадал, хочешь сыграть ещё раз?')
                    bot.register_next_step_handler(message, game)
        else:
            bot.send_message(message.chat.id, 'это не число')

# @bot.message_handler()
# def variable_x_y(message):
   # x = message.text
#    if x.isnumeric:
       # bot.send_message(message.chat.id, 'назови вторую границу диапазона')
    #elif x.isnumeric is False:
      #  bot.send_message(message.chat.id, 'astdrd')


bot.polling(none_stop=True)


