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
policyNum = 1


class Game:
    def __init__(self):
        self.policy = [1, 2]
        self.doorNum = [3, 6, 9, 20, 100]
        self.count = [10, 50, 100]  # , 200, 500, 1000]

    def Start(self):
        graphData1 = []
        graphData2 = []
        for doorNum in self.doorNum:
            self.prize = random.randint(doorNum)
            winPer = 0.0
            for policy in self.policy:
                print("Strategy: " + str(policy))
                for count in self.count:
                    if policy == 0:
                        winPer = self.Policy0(count, doorNum)
                    elif policy == 1:
                        winPer = self.Policy1(count, doorNum)
                    elif policy == 2:
                        winPer = self.Policy2(count, doorNum)
                    else:
                        print("Invalid Policy choice Bye!")
                        return

                    if count == self.count[-1] and policy == 1:
                        graphData1.append(
                            {
                                "Strategy": policy,
                                "Doors": doorNum,
                                "Average Win Probability": winPer,
                            }
                        )

                    if doorNum == self.doorNum[-1] and policy == 2:
                        graphData2.append(
                            {
                                "Trials": count,
                                "Doors": doorNum,
                                "Average Win Propability": winPer,
                            }
                        )

                    print(
                        "With "
                        + str(doorNum)
                        + " doors. With Count "
                        + str(count)
                        + " Win percentage: "
                        + str(winPer)
                        + "%"
                    )
                print("\n")
        return graphData1, graphData2

    def Policy0(self, count, doorNum):  # Experiment
        # Host opens 1 door randomly at a time
        # 1-doorNum = doors possible with prize
        # Randomly switch to one of the remaining doors

        right = 0
        wrong = 0
        choice = 0

        for i in range(count):
            doors = [x for x in range(doorNum)]
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

    def Policy1(self, count, doorNum):
        # The flip of Sticking with original selection is...
        # Randomly switch to one of the remaining doors
        return 100 - self.Policy2(count, doorNum)

    def Policy2(self, count, doorNum):
        # Host opens 1 door randomly
        # 1-doorNum = doors possible with prize
        # Stick with your original selection.

        # 1/(1-doorNum) chance of winning
        right = 0
        wrong = 0
        choice = 0

        for i in range(count):
            choice = random.randint(doorNum)
            if choice == self.prize:
                right += 1
            else:
                wrong += 1

        return (right / count) * 100


Monty_Hall = Game()
graphDatas = Monty_Hall.Start()
print(graphDatas)