from telebot import types


class NumericalGuessingGameMarkup(object):

    @staticmethod
    def accept_or_reject():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        rule_yes = types.KeyboardButton('Да')
        rule_no = types.KeyboardButton('Нет')
        markup.add(rule_yes, rule_no)
        return markup

    @staticmethod
    def go_or_back():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        rule_go = types.KeyboardButton('Вперёд!')
        rule_back = types.KeyboardButton('Я передумал')
        markup.add(rule_go, rule_back)
        return markup
