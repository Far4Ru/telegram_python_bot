from telebot import types


class GallowsGameMarkup(object):

    @staticmethod
    def accept_or_reject():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        rule_yes = types.KeyboardButton('Вперёд!')
        rule_no = types.KeyboardButton('Я передумал')
        markup.add(rule_yes, rule_no)
        return markup
