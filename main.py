import os
from dotenv import load_dotenv
from pathlib import Path

from game import Game


def load():
    dotenv_path = Path(os.getcwd() + '/.env')
    load_dotenv(dotenv_path=dotenv_path)
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    game = Game(BOT_TOKEN)
    game.start()


def main():
    load()


if __name__ == '__main__':
    main()
