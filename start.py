"""Game of Snakes and Ladders

The program is a implementation for the snakes and ladders game with below capabilities
######
Basic dice roll - allows a player to roll a dice and move the position to the count on dice rolled
Adding Snake - A snake could be added to the game which changes the game in a way when the player position reaches the styaring point of the snake he will be moved to the end point of the snake
Crooked Dice - The dice roll would result in giving a dice throw of even numbers"""

from random import choice as throw
from time import sleep

class Game():
    """Initialize the object with player position and maximum number of positions that a person can move on roll of a dice"""
    def __init__(self,maxPosition=100,maxDice=6):
        self.currentPosition = 0
        self.maxDice = maxDice
        self.maxPosition = maxPosition
        self.snakes = {}

    """Performs a Dice throw, add the new throw to current position of the player"""
    def throwDice(self, isCrooked = False):
        __diceThrow = throw(range(1,self.maxDice+1)) if not isCrooked else throw(range(2,self.maxDice+1,2))
        print("Dice throw done with a throw of {0} !!".format(__diceThrow))
        self.__validateNewPosition(__diceThrow)
        self.__checkForSnake()
        sleep(1)

    def __validateNewPosition(self,distanceDelta):
        if (self.currentPosition + distanceDelta == self.maxPosition):
            self.currentPosition += distanceDelta
            print("Yay !! You completed the game ! \nPlease Re-run the game to start a new game ")
            exit(0)
        elif (self.currentPosition + distanceDelta > self.maxPosition):
            print("Better luck with next throw, you need a {0} or a throw less than {0} to move forward !!".format(self.maxPosition - self.currentPosition ))
        else:
            self.currentPosition += distanceDelta
            print("Your new position is {0} !!".format(self.currentPosition))
        

    def addSnake(self,startPos,endPos):
        if endPos >= startPos:
            print('End Position has to be less than start position for adding a Snake')
            return
        else:
            self.snakes[startPos] = endPos
            print('Snake has been added to the Game board !')
        
    def __checkForSnake(self):
        if self.currentPosition in self.snakes:
            print('Uh! Oh!! Looks like you got bitten by a snake!')
            self.currentPosition = self.snakes[self.currentPosition]
            print("Your new position is {0} !!".format(self.currentPosition))


__exit = False
gameboard = """
**************** GAME *********************
***************** OF **********************
*********** SNAKES & LADDERS **************
1. Roll the dice
2. Roll a Crooked Dice
3. Add a Snake
4. Exit
"""

def getNumInput(msg):
    try:
        get_uip = int(input(gameboard))
    except ValueError as e:
        print('Please enter a INTEGER as input !! ')
        sleep(2)

gameInstance = Game()
while not __exit:
    try:
        get_uip = int(input(gameboard))
    except ValueError as e:
        print('Please enter a INTEGER as input !! ')
        sleep(2)
        continue
    if get_uip == 1:
        gameInstance.throwDice()
    elif get_uip == 2:
        gameInstance.throwDice(isCrooked=True)
    elif get_uip == 3:
        try:
            __start = int(input("Start position of the snake :: "))
            __end = int(input("End position of the snake :: "))
        except ValueError as e:
            print('Please enter a INTEGER as input !! ')
        else:
            gameInstance.addSnake(__start,__end)
    elif get_uip == 4:
        __exit = True
    else:
        print("Please enter a valid input based on the provided menu values !! ")
