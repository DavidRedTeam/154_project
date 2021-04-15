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
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

# doorNum = int(input("Enter number of Doors to use in Monty Hall Simulation: "))
# policyNum = int(input("Enter Policy Number: "))


class Game:
    def __init__(self):
        self.policy = [4]
        self.doorNum = [3, 6, 9, 20, 100]
        self.count = [1000]  # [10, 50, 100, 200, 500, 1000]

    def Start(self):
        graphData1 = []
        graphData2 = []
        for doorNum in self.doorNum:
            self.prize = random.randint(doorNum)
            winPer = 0.0
            for policy in self.policy:
                # print("Strategy: " + str(policy))
                for count in self.count:
                    if policy == 0:
                        winPer = self.Policy0(count, doorNum)
                    elif policy == 1:
                        winPer = self.Policy1(count, doorNum)
                    elif policy == 2:
                        winPer = self.Policy2(count, doorNum)
                    elif policy == 3:
                        winPer = self.Policy3(count, doorNum)
                    elif policy == 4:
                        winPer = self.Policy4(count, doorNum)
                    else:
                        print("Invalid Policy choice Bye!")
                        return

                    if count == self.count[-1] and policy == 4:
                        graphData1.append(
                            {
                                "Strategy": policy,
                                "Doors": doorNum,
                                "Average Win Probability": winPer,
                            }
                        )

                    if doorNum == self.doorNum[-1] and policy == 1:
                        graphData2.append(
                            {
                                "Trials": count,
                                "Doors": doorNum,
                                "Average Win Probability": winPer,
                            }
                        )
                    """
                    print(
                        "With "
                        + str(doorNum)
                        + " doors. With Count "
                        + str(count)
                        + " Win percentage: "
                        + str(winPer)
                        + "%"
                    )
                print("\n")"""
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

    def Policy3(self, count, doorNum):
        # The flip of Sticking with original selection is...
        # Randomly switch to one of the remaining doors
        return 100 - self.Policy4(count, doorNum)

        """right = 0
        wrong = 0
        choice = 0

        for i in range(count):
            choice = random.randint(doorNum)

            slipDoor = choice
            while choice == slipDoor:  # choice of player cannot equal random goat door
                slipDoor = random.randint(doorNum)

            if slipDoor == self.prize:
                right += 1
            elif choice == self.prize:
                wrong += 1
            else:
                right += 1

        return (right / count) * 100"""

    def Policy4(self, count, doorNum):
        # Host opens 1 door randomly
        # 1-doorNum = doors possible with prize
        # Stick with your original selection.

        # 1/(1-doorNum) chance of winning
        right = 0
        wrong = 0
        choice = 0

        for i in range(count):
            choice = random.randint(doorNum)
            slipDoor = choice
            while choice == slipDoor:  # choice of player cannot equal random goat door
                slipDoor = random.randint(doorNum)
            if choice == self.prize or slipDoor == self.prize:
                right += 1
            else:
                wrong += 1

        return (right / count) * 100


Monty_Hall = Game()
graphDatas = Monty_Hall.Start()
# print(graphDatas)

""" Approximate Improvement Over Trials
trials1 = [x["Trials"] for x in graphDatas[1]]
wins1 = [x["Average Win Probability"] for x in graphDatas[1]]

namesSTR = [str(x) for x in trials1]

plt.figure(figsize=(9, 3))
plt.bar(trials1, wins1, 5)

for i in range(len(trials1)):
    plt.text(trials1[i] - 0.5, wins1[i] + 0.1, str(wins1[i]) + "%", size=8)

plt.xticks(trials1, [str(x) for x in trials1])

x = np.array(trials1)
y = np.array(wins1)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m * x + b, color="orange")

plt.ylabel("Average Win Percentage")
plt.xlabel("Number of Trials")
plt.suptitle("Approximate Improvement Over Trials 1000 Doors")
plt.show()
"""

# Strategy Probability Graphs
names1 = [x["Doors"] for x in graphDatas[0]]
values1 = [x["Average Win Probability"] for x in graphDatas[0]]

namesSTR = [str(x) for x in names1]

plt.figure(figsize=(9, 3))
plt.bar(names1, values1)

for i in range(len(names1)):
    plt.text(names1[i] - 0.5, values1[i] + 0.1, str(values1[i]) + "%", size=8)


x = np.array(names1)
y = np.array(values1)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m * x + b, color="orange")

plt.ylabel("Average Win Percentage")
plt.xlabel("Number of Doors")
plt.suptitle("Strategy 4 (with 1000 trials)")
plt.show()
