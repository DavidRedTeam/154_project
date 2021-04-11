#######################################################################
#   Monte Carlo - Black Jack | CSCI 154
#
#   Group: Mitchell Maltezo, Micah Mercado, David Andrade, Harpreet Ghag
#
#   Language: Python
#
#
# Own Policies:
#   4. Always Hit
#   5. Always hit twice regardless
#######################################################################
import enum
import random
import array
import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
lose = 0
win = 0
tie = 0
outcome = None
ranks = {
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "jack": 10,
    "queen": 10,
    "king": 10,
    "ace": (1, 11)
}

suits = ['clubs', 'diamonds', 'hearts', 'spades']


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return self.rank + " of " + self.suit.value


class Deck:

    def __init__(self, num=1):
        self.cards = []
        for i in range(num):
            for suit in suits:
                for rank, value in ranks.items():
                    self.cards.append(Card(suit, rank, value))

    def print(self):
        for i in self.cards:
            print(i.suit, i.rank, i.value)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)

    def peek(self):
        if len(self.cards) > 0:
            return self.cards[0]

    def add_to_bottom(self, card):
        self.cards.append(card)

    def __str__(self):
        result = ""
        for card in self.cards:
            result += str(card) + "\n"
        return result

    def __len__(self):
        return len(self.cards)


def single_policy_1():

    deck = Deck()
    deck.shuffle()
    print("SINGLE DECK POLICY 1 CALLED")
    p_hand = []
    p_value = 0

    d_hand = []
    d_value = 0

    p_hand.append(deck.deal())
    p_hand.append(deck.deal())
    for i in range(2):
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
    p_value = p_hand[0].value + p_hand[1].value
    print("Initial Hand: ", p_hand[0].value, p_hand[1].value)

    d_hand.append(deck.deal())
    d_hand.append(deck.deal())

    for i in range(2):
        if (d_hand[i].rank == 'ace'):
            d_hand[i].value = random.choice(ranks["ace"])
    d_value = d_hand[0].value + d_hand[1].value
    print("Dealer Hand: ", d_hand[0].value, d_hand[1].value)

    for i in range(2, 52):
        if p_value > 21:
            break
        if p_value == 21:
            break
        if p_value >= 17:
            break
        p_hand.append(deck.deal())
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
        print("Card drawn: ", p_hand[i].value)
        p_value += p_hand[i].value

    # Must hit if dealer's hand is not 17+
    if p_value <= 21:
        for i in range(2, 52):
            if d_value >= 17:
                break
            if d_value < 17:
                d_hand.append(deck.deal())
                if (d_hand[i].rank == 'ace'):
                    d_hand[i].value = random.choice(ranks["ace"])
                print("Dealer card drawn: ", d_hand[i].value)
                print(d_value)
                d_value += d_hand[i].value

    print("Player Hand Value  ",
          p_value, "Dealer Hand Value: ", d_value)

    if p_value == d_value or (p_value > 21 and d_value > 21):
        return 2  # tie
    if p_value > 21 or (d_value > p_value and d_value < 22):
        return 1  # loss
    if d_value > 21 or (p_value <= 21 and p_value > d_value):
        return 0  # win


def single_policy_2():

    deck = Deck()
    deck.shuffle()
    print("SINGLE DECK POLICY 2 CALLED")
    p_hand = []
    p_value = 0

    d_hand = []
    d_value = 0

    p_hand.append(deck.deal())
    p_hand.append(deck.deal())
    for i in range(2):
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
    p_value = p_hand[0].value + p_hand[1].value
    print("Initial Hand: ", p_hand[0].value, p_hand[1].value)

    d_hand.append(deck.deal())
    d_hand.append(deck.deal())

    for i in range(2):
        if (d_hand[i].rank == 'ace'):
            d_hand[i].value = random.choice(ranks["ace"])
    d_value = d_hand[0].value + d_hand[1].value
    print("Dealer Hand: ", d_hand[0].value, d_hand[1].value)

    for i in range(2, 52):
        if p_value > 21:
            break
        if p_value == 21:
            break
        if p_value >= 17 and (p_hand[0].rank != 'ace' or p_hand[1].rank != 'ace'):
            break
        p_hand.append(deck.deal())
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
        print("Card drawn: ", p_hand[i].value)
        p_value += p_hand[i].value

    # Must hit if dealer's hand is not 17+
    if p_value <= 21:
        for i in range(2, 52):
            if d_value >= 17:
                break
            if d_value < 17:
                d_hand.append(deck.deal())
                if (d_hand[i].rank == 'ace'):
                    d_hand[i].value = random.choice(ranks["ace"])
                print("Dealer card drawn: ", d_hand[i].value)
                print(d_value)
                d_value += d_hand[i].value

    print("Player Hand Value  ",
          p_value, "Dealer Hand Value: ", d_value)

    if p_value == d_value or (p_value > 21 and d_value > 21):
        return 2  # tie
    if p_value > 21 or (d_value > p_value and d_value < 22):
        return 1  # loss
    if d_value > 21 or (p_value <= 21 and p_value > d_value):
        return 0  # win


def single_policy_3():

    deck = Deck()
    deck.shuffle()
    print("SINGLE DECK POLICY 3 CALLED")
    p_hand = []
    p_value = 0

    d_hand = []
    d_value = 0

    p_hand.append(deck.deal())
    p_hand.append(deck.deal())
    for i in range(2):
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
    p_value = p_hand[0].value + p_hand[1].value
    print("Initial Hand: ", p_hand[0].value, p_hand[1].value)

    d_hand.append(deck.deal())
    d_hand.append(deck.deal())

    for i in range(2):
        if (d_hand[i].rank == 'ace'):
            d_hand[i].value = random.choice(ranks["ace"])
    d_value = d_hand[0].value + d_hand[1].value
    print("Dealer Hand: ", d_hand[0].value, d_hand[1].value)

    # Must hit if dealer's hand is not 17+
    if p_value <= 21:
        for i in range(2, 52):
            if d_value >= 17:
                break
            if d_value < 17:
                d_hand.append(deck.deal())
                if (d_hand[i].rank == 'ace'):
                    d_hand[i].value = random.choice(ranks["ace"])
                print("Dealer card drawn: ", d_hand[i].value)
                print(d_value)
                d_value += d_hand[i].value

    print("Player Hand Value  ",
          p_value, "Dealer Hand Value: ", d_value)

    if p_value == d_value or (p_value > 21 and d_value > 21):
        return 2  # tie
    if p_value > 21 or (d_value > p_value and d_value < 22):
        return 1  # loss
    if d_value > 21 or (p_value <= 21 and p_value > d_value):
        return 0  # win


def single_policy_4():  # Always Hit Once Regardless
    deck = Deck()
    deck.shuffle()
    print("SINGLE DECK POLICY 4 CALLED")
    p_hand = []
    p_value = 0

    d_hand = []
    d_value = 0

    p_hand.append(deck.deal())
    p_hand.append(deck.deal())
    for i in range(2):
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
    p_value = p_hand[0].value + p_hand[1].value
    print("Initial Hand: ", p_hand[0].value, p_hand[1].value)

    d_hand.append(deck.deal())
    d_hand.append(deck.deal())

    for i in range(2):
        if (d_hand[i].rank == 'ace'):
            d_hand[i].value = random.choice(ranks["ace"])
    d_value = d_hand[0].value + d_hand[1].value
    print("Dealer Hand: ", d_hand[0].value, d_hand[1].value)

    for i in range(2, 3):
        if p_value > 21:
            break
        if p_value == 21:
            break
        p_hand.append(deck.deal())
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
        print("Card drawn: ", p_hand[i].value)
        p_value += p_hand[i].value

    # Must hit if dealer's hand is not 17+
    if p_value <= 21:
        for i in range(2, 52):
            if d_value >= 17:
                break
            if d_value < 17:
                d_hand.append(deck.deal())
                if (d_hand[i].rank == 'ace'):
                    d_hand[i].value = random.choice(ranks["ace"])
                print("Dealer card drawn: ", d_hand[i].value)
                print(d_value)
                d_value += d_hand[i].value

    print("Player Hand Value  ",
          p_value, "Dealer Hand Value: ", d_value)

    if p_value == d_value or (p_value > 21 and d_value > 21):
        return 2  # tie
    if p_value > 21 or (d_value > p_value and d_value < 22):
        return 1  # loss
    if d_value > 21 or (p_value <= 21 and p_value > d_value):
        return 0  # win


def single_policy_5():  # 5. Always hit twice regardless

    deck = Deck()
    deck.shuffle()
    print("SINGLE DECK POLICY 1 CALLED")
    p_hand = []
    p_value = 0

    d_hand = []
    d_value = 0

    p_hand.append(deck.deal())
    p_hand.append(deck.deal())
    for i in range(2):
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
    p_value = p_hand[0].value + p_hand[1].value
    print("Initial Hand: ", p_hand[0].value, p_hand[1].value)

    d_hand.append(deck.deal())
    d_hand.append(deck.deal())

    for i in range(2):
        if (d_hand[i].rank == 'ace'):
            d_hand[i].value = random.choice(ranks["ace"])
    d_value = d_hand[0].value + d_hand[1].value
    print("Dealer Hand: ", d_hand[0].value, d_hand[1].value)

    for i in range(2, 4):
        if p_value > 21:
            break
        if p_value == 21:
            break
        p_hand.append(deck.deal())
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
        print("Card drawn: ", p_hand[i].value)
        p_value += p_hand[i].value

    # Must hit if dealer's hand is not 17+
    if p_value <= 21:
        for i in range(2, 52):
            if d_value >= 17:
                break
            if d_value < 17:
                d_hand.append(deck.deal())
                if (d_hand[i].rank == 'ace'):
                    d_hand[i].value = random.choice(ranks["ace"])
                print("Dealer card drawn: ", d_hand[i].value)
                print(d_value)
                d_value += d_hand[i].value

    print("Player Hand Value  ",
          p_value, "Dealer Hand Value: ", d_value)

    if p_value == d_value or (p_value > 21 and d_value > 21):
        return 2  # tie
    if p_value > 21 or (d_value > p_value and d_value < 22):
        return 1  # loss
    if d_value > 21 or (p_value <= 21 and p_value > d_value):
        return 0  # win


def main():
    global lose
    global win
    global tie
    global outcome

    for i in range(10000):
        outcome = single_policy_3()
        if (outcome == 0):
            win += 1
        elif (outcome == 1):
            lose += 1
        elif (outcome == 2):
            tie += 1
    print("Wins: ",  win, "Loses: ",  lose, "Ties: ", tie)

    # labels = ['losses', 'wins']
    # wins = [win]
    # losses = [lose]
    # ties = [tie]

    # width = 0.35       # the width of the bars: can also be len(x) sequence

    # fig, ax = plt.subplots()

    # ax.bar(labels[1], wins, width,  label='wins')
    # ax.bar(labels[0], losses, width, label='losses')

    # ax.set_title('Wins Losses using Policy 1')
    # ax.legend()

    # plt.show()
# wl = [win, lose]
# print("Wins: ",  win, "Loses: ",  lose)
# fig = plt.figure(figsize=(10, 5))
# ax = fig.add_axes([0, 0, 1, 1])
# wl.plot(kind='bar', fontsize=20)
# plt.axis('equal')
# ax.bar(win, height=1.0, width=0.5, color="blue")
# plt.xlabel('Wins and Loses', fontsize=15)
# plt.ylabel('Number of Wins and Loses', fontsize=15)
# plt.title('David is POGGERS!', fontsize=15)
# plt.show()
# fig = plt.figure()
# plt = fig.add_axes([0, 1])
# plt.bar(win, lose)
# plt.title("Policy 1 Single Deck Simulation Outcomes in W/L")
# plt.show()


#####################################
if __name__ == "__main__":
    main()
