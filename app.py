import copy
from phrasehunter.constants import phrases
from phrasehunter.game import Game


def main():
    phrases_copy = copy.deepcopy(phrases)

    while True:
        game = Game(phrases_copy)
        game.start_game()


if __name__ == '__main__':
    main()
