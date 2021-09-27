from game import Game
from random import choice

_gInsatnce = Game(maxPosition=100)
_gInsatnce2 = Game(isCrooked=True)
__counter = 0

while __counter < 6:
    __start =  choice(range(1,99))
    if __start > 1 :
        __end = choice(range(1,__start))
    else: 
        continue
    print("GAME ::1::")
    _gInsatnce.addSnake(__start,__end)
    print("GAME ::2::")
    _gInsatnce2.addSnake(__start,__end)
    __counter += 1

__counter = 0

while __counter < 19:
    print("GAME ::1::")
    _gInsatnce.throwDice()
    print("GAME ::2::")
    _gInsatnce2.throwDice()