import os
from dotenv import load_dotenv
from pathlib import Path

from app.bot import Bot


def get_token():
    load_dotenv(dotenv_path=Path(os.getcwd() + '/.env'))
    return os.getenv('BOT_TOKEN')


def load():
    bot = Bot(get_token())
    bot.start()


def main():
    load()


if __name__ == '__main__':
    main()
