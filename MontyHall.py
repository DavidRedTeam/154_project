#######################################################################
#   Monty Hall | CSCI 154
#
#   Reference: https://electronut.in/simple-python-matplotlib-implementation-of-conways-game-of-life/
#
#   Group: Mitchell Maltezo, Micah Mercado, David Andrade, Harpreet Ghag
#
#   Language: Python
#
#######################################################################

# import numpy as np
from numpy import random

# doorNum = int(input("Enter number of Doors to use in Monty Hall Simulation: "))
# policyNum = int(input("Enter Policy Number: "))
doorNum = 3
policyNum = 1


class Game:
    def __init__(self, doorNum, policy):
        self.policy = policy
        self.doorNum = doorNum
        self.prize = random.randint(doorNum)
        # self.doors = ["goat" for x in range(doorNum)]
        # self.doors[self.prize] = "prize"
        #  #self.choice = int(input("Choose a Door 1-"+ str(self.doorNum) + ": "))

    def Start(self):
        winPer = 0.0
        count = 1000
        if self.policy == 0:
            winPer = self.Policy0(count)
        elif self.policy == 1:
            winPer = self.Policy1(count)
        elif self.policy == 2:
            winPer = self.Policy2(count)
        else:
            print("Invalid Policy choice Bye!")
            return
        print("How many times won: " + str(winPer) + "%")

    def Policy0(self, count):  # Experiment
        # Host opens 1 door randomly at a time
        # 1-doorNum = doors possible with prize
        # Randomly switch to one of the remaining doors

        right = 0
        wrong = 0
        choice = 0

        for i in range(count):
            doors = [x for x in range(self.doorNum)]
            goats = doors.copy()
            goats.pop(self.prize)
            # goats is all doors that have goat

            for j in range(len(goats) - 1):
                choice = doors[random.randint(len(doors))]

                # host picks random door with goat
                randGoat = choice
                while (
                    choice == randGoat
                ):  # choice of player cannot equal random goat door
                    randGoat = goats[random.randint(len(goats))]

                doors.remove(randGoat)  # open door
                goats.remove(randGoat)  # open door
            doors.remove(choice)
            choice = doors.pop()

            if choice == self.prize:
                right += 1
            else:
                wrong += 1

        return (right / count) * 100

    def Policy1(self, count):
        # The flip of Sticking with original selection is...
        # Randomly switch to one of the remaining doors
        return 100 - self.Policy2(count)

    def Policy2(self, count):
        # Host opens 1 door randomly
        # 1-doorNum = doors possible with prize
        # Stick with your original selection.

        # 1/(1-doorNum) chance of winning
        right = 0
        wrong = 0
        choice = 0

        for i in range(count):
            choice = random.randint(self.doorNum)
            if choice == self.prize:
                right += 1
            else:
                wrong += 1

        return (right / count) * 100


Monty_Hall = Game(doorNum, policyNum)
Monty_Hall.Start()
print()