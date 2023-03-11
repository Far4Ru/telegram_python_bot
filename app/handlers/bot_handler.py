from app.markup.bot_markup import BotMarkup
from app.handlers.gallows_game_handler import GallowsGameHandler
from app.handlers.numerical_guessing_game_handler import NumericalGuessingGameHandler


class BotHandler:
    def __init__(self, bot):
        self.bot = bot
        self.gallows_game = GallowsGameHandler(self.bot)
        self.numerical_guessing_game = NumericalGuessingGameHandler(self.bot)

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
            self.bot.send_message(message.chat.id, 'Выбери игру, в которую хочешь сыграть.',
                                  reply_markup=BotMarkup.game_selection())
            self.bot.register_next_step_handler(message, game_selection)

        def game_selection(message):
            if message.text == 'Числовая угадайка':
                self.bot.send_message(message.chat.id,
                                      'Добро пожаловать в числовую угадайку! Ознакомишься с правилами?',
                                      reply_markup=BotMarkup.accept_or_reject())
                self.bot.register_next_step_handler(message, self.numerical_guessing_game.rules)
            elif message.text == 'Виселица':
                self.bot.send_message(message.chat.id, 'Добро пожаловать в виселицу! Ознакомишься с правилами?',
                                      reply_markup=BotMarkup.accept_or_reject())
                self.bot.register_next_step_handler(message, self.gallows_game.rules)
