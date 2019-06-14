# Create your Phrase class logic here.
from .character import Character
# The class should include an initializer or def __init__ that receives a phrase parameter
# and holds this phrase in an instance attribute on the Phrase object.
# A phrase should be a collection of Character objects,
# where each letter of the phrase is a Character() instance stored inside a collection such as a List.

# The Phrase instance might be responsible for things like:
# Knowing if the entire phrase has been guessed,
# Iterating over its collection of Character to allow a guess to be checked using a
# Character instance method call or to ask the Character object how it should show its letter.


class Phrase:
    def __init__(self, phrase, all_guessed=False):
        self.list_of_chars = []
        self.phrase = phrase
        for char in self.phrase:
            self.list_of_chars.append(Character(char))

    @staticmethod
    def test_class():
        print("From phrase class")
