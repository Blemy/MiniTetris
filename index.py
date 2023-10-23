import os, time
from random import randrange

def obstacleBouge():
    obsD = 0
    obsAffAle = "🚔"
    position = randrange(0,100)
    while (obsD <= 7):
        obsD += 1
        pos = " " * position + obsAffAle
        print(pos)
        time.sleep(0.50)
        if obsD == 7:
            obsD = 0
            position = randrange(0,100)
            os.system('cls')
obstacleBouge()