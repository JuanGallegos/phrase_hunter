class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def __repr__(self):
        return str(self.phrase)

    def display(self, guess):
        current = list(self.phrase)
        for index, item in enumerate(current):
            if item not in guess:
                if item == ' ':
                    current[index] = ' '
                else:
                    current[index] = '_'

        print(' '.join(current), '\n')
        return set(current)

    def check_letter(self, guess):
        if guess in self.phrase:
            return True
        else:
            return False

    def check_complete(self, correct_guesses):
        if '_' in correct_guesses:
            correct_guesses.remove('_')
        else:
            if correct_guesses == set(self.phrase):
                print('You win! You guessed all the characters! \n')
                return True
