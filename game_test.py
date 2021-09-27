from game import Game
import unittest

class game_test(unittest.TestCase):
    
    def test_range_of_dice(self):
        gameInstance = Game()
        self.assertIn(gameInstance.throwDice()[0],range(1,7))

    def test_range_of_crooked_dice(self):
        gameInstance = Game(isCrooked=True)
        self.assertIn(gameInstance.throwDice()[0],range(2,7,2))

    def test_is_crooked(self):
        gameInstance = Game(isCrooked=True)
        self.assertEqual(gameInstance.throwDice()[0]%2,0)
        self.assertEqual(gameInstance.isCrooked, True)

    def test_normal_game_initialization(self):
        gameInstance = Game()
        self.assertEqual(gameInstance.currentPosition,0)
        self.assertEqual(gameInstance.isCrooked, False)
        self.assertEqual(gameInstance.maxDice,6)
        self.assertEqual(gameInstance.maxPosition, 100)

    def test_custom_game_initialization(self):
        gameInstance = Game(isCrooked=True,maxPosition=144,maxDice=12)
        self.assertEqual(gameInstance.currentPosition,0)
        self.assertEqual(gameInstance.isCrooked, True)
        self.assertEqual(gameInstance.maxDice,12)
        self.assertEqual(gameInstance.maxPosition, 144)
        
    def test_adding_snake(self):
        gameInstance = Game()
        self.assertEqual(gameInstance.addSnake(12,1),0)
        self.assertEqual(len(gameInstance.snakes),1)
        self.assertEqual(gameInstance.addSnake(12,31),1)
        self.assertEqual(gameInstance.addSnake(12,'q'),2)
        self.assertEqual(gameInstance.addSnake('12','1'),2)

    def test_distance_calculation(self):
        gameInstance = Game()
        __initPos = gameInstance.throwDice()
        self.assertEqual(__initPos[0],__initPos[1])
        __counter = 0
        while(__counter < 5):
            __pos = gameInstance.throwDice()
            self.assertEqual(__pos[0] + __initPos[1] , __pos[1])
            __initPos = __pos
            __counter += 1
