# Import your Game class
from phrasehunter.game import Game
from phrasehunter.phrase import Phrase
from phrasehunter.character import Character

# Create your Dunder Main statement.

# Inside Dunder Main:
# Create an instance of your Game class
# Start your game by calling the instance method that starts the game loop
if __name__ == '__main__':
    new_game = Game("test game")
    Game.test_class()
    Phrase.test_class()
    Character.test_class()
    new_game.run_game()

