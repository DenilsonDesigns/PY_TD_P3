from .phrase import Phrase

# Create your Game class logic in here.


class Game:
    def __init__(self, phrase):
        self.phrase = Phrase(phrase)

    @staticmethod
    def test_class():
        print("From game class")

    def run_game(self):
        name = input("What is your name? ")

        print("Hello, " + name, "Time to play hangman!")
        print()
        print("Start guessing...")
        word = self.phrase.phrase
        guesses = ''
        turns = 10

        while turns > 0:
            wrong = 0
            word_to_print = ''
            for char in word:
                if char in guesses:
                    word_to_print += char + " "
                else:
                    word_to_print += '_ '
                    wrong += 1

            print(word_to_print)
            if wrong == 0:
                print("You Won!")
                break

            print()
            guess = input("Guess a character: ")
            guesses += guess
            if guess not in word:
                turns -= 1
                print("This character is not in the word")
                print("You have ", +turns, "more guesses")
                if turns == 0:
                    print("You lose :(")
