# Create your Character class logic in here.
# The Character instance is responsible for holding the state of a given single character.
# You should ensure when you create instances of Character() that you only pass a character
# that is a single character or len(char) == 1. Anything more or less should be invalid and
# might cause you bugs in your code, especially if you are passing the user's input directly
# into the creation of the Character object.


class Character:
    def __init__(self, original, guessed=False):
        self.original = original
        self.guessed = guessed

    @staticmethod
    def test_class():
        print("From char class")

    def show_char(self, guess):
        if guess == self.original:
            return guess
        else:
            return "_"

    def update_guessed(self, guess):
        if guess == self.original:
            self.guessed = True
