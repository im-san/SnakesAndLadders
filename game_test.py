from game import Game
import unittest

class game_test(unittest.TestCase):
    
    def test_range_of_dice(self):
        gameInstance = Game()
        self.assertIn(gameInstance.throwDice(),range(1,7))

    def test_range_of_crooked_dice(self):
        gameInstance = Game(isCrooked=True)
        self.assertIn(gameInstance.throwDice(),range(2,7,2))

    def test_is_crooked(self):
        gameInstance = Game(isCrooked=True)
        self.assertEqual(gameInstance.throwDice()%2,0)
        self.assertEqual(gameInstance.isCrooked, True)

    