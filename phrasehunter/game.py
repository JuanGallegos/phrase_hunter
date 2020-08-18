import random
import phrasehunter.phrase as phrase


class Game:
    def __init__(self, phrases, missed=0, active_phrase=None, guesses=[]):
        self.missed = missed
        self.phrases = phrases
        self.active_phrase = active_phrase
        self.guesses = guesses

    def start_game(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        p = phrase.Phrase(self.active_phrase)
        p.display(' ')

        while True:
            if self.missed < 5:
                self.get_guess(p)
                if p.check_letter(self.guesses[-1]):
                    correct_guesses = p.display(self.guesses)
                    if p.check_complete(correct_guesses):
                        self.reset()
                        break
                else:
                    self.point_lost()
                    p.display(self.guesses)
            else:
                print('Sorry! You lose! You did not guess the phrase!')
                print(f'The correct phrase was: \"{str(p).title()}\" \n')
                self.reset()
                break

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print('\n-------------------------')
        print('Welcome to Phrase Hunter!')
        print('-------------------------\n')
        print('Can you guess the hidden phrase?')

    def get_guess(self, p):
        while True:
            guess = input('Guess a letter: ').lower()

            if guess.isalpha():
                if len(guess) > 1:
                    print('You entered too many letters.')
                    p.display(self.guesses)
                else:
                    if guess in self.guesses:
                        print(f'The letter "{guess}" has been guessed before.')
                        print('As a reminder, the letters guessed are: ',
                              f'{(",").join(self.guesses)}')
                        p.display(self.guesses)
                    else:
                        return self.guesses.append(guess)
            else:
                print('You did not enter a letter. \n')
                p.display(self.guesses)

    def game_over(self):
        print('\n-------------------------')
        print('- Thank you for Playing -')
        print('-------------------------\n')

    def point_lost(self):
        self.missed += 1
        print(f'You have {5 - self.missed} out of 5 lives '
              'remaining! \n')

    def reset(self):
        while True:
            reset_value = input('Would you like to play again (y/n): ')
            if reset_value.lower() == 'y':
                self.missed = 0
                self.phrases = []
                self.active_phrase = None
                self.guesses.clear()
                return True
            elif reset_value.lower() == 'n':
                self.game_over()
                exit()
            else:
                print("\nYou did not enter a response of 'y' or 'n'.")
