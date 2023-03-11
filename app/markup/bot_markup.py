from telebot import types


class BotMarkup(object):

    @staticmethod
    def game_selection():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        first_game = types.KeyboardButton('Числовая угадайка')
        second_game = types.KeyboardButton('Виселица')
        markup.add(first_game, second_game)
        return markup

    @staticmethod
    def accept_or_reject():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        rule_yes = types.KeyboardButton('Да')
        rule_no = types.KeyboardButton('Нет')
        markup.add(rule_yes, rule_no)
        return markup