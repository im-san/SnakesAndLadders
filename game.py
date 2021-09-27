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
    def __init__(self,isCrooked = False, maxPosition=100,maxDice=6):
        self.currentPosition = 0
        self.maxDice = maxDice
        self.maxPosition = maxPosition
        self.snakes = {}
        self.isCrooked = isCrooked

    """Performs a Dice throw, add the new throw to current position of the player"""
    def throwDice(self):
        if self.currentPosition == self.maxPosition:
            print('You have completed the game already ! ')
            return
        __diceThrow = throw(range(1,self.maxDice+1)) if not self.isCrooked else throw(range(2,self.maxDice+1,2))
        print("Dice throw done with a throw of {0} !!".format(__diceThrow))
        self.__validateNewPosition(__diceThrow)
        self.__checkForSnake()
        sleep(1)
        return __diceThrow

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
            print('Snake has been added to the Game board starting at {0} and ending at {1} !'.format(startPos,endPos))
        
    def __checkForSnake(self):
        if self.currentPosition in self.snakes:
            print('Uh! Oh!! Looks like you got bitten by a snake!')
            self.currentPosition = self.snakes[self.currentPosition]
            print("Your new position is {0} !!".format(self.currentPosition))


if __name__ == "__main__":
    print('This is an Import module. Can not be run directly')