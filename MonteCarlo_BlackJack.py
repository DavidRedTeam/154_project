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

ranks = {
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 9,
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
        return self.rank + " of " + self.suit


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

# Single = only 1 deck


def single_policy_1():

    deck = Deck()
    deck.shuffle()
    print("SINGLE DECK POLICY 1 CALLED")
    p_hand = []
    p_value = 0

    d_hand = []
    d_value = 0
    # Adding cards to p_hand array
    p_hand.append(deck.deal())
    p_hand.append(deck.deal())

    print("Player Hand at 0 and 1 is: ", p_hand[0].value, p_hand[1].value)

    for i in range(2):
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
    p_value = p_hand[0].value + p_hand[1].value
    print("Initial Hand: ", p_hand[0].value, p_hand[1].value)

    # Adding cards to d_hand
    d_hand.append(deck.deal())
    d_hand.append(deck.deal())

    for i in range(2):
        if (d_hand[i].rank == 'ace'):
            d_hand[i].value = random.choice(ranks["ace"])
    d_value = d_hand[0].value + d_hand[1].value
    print("Dealer Hand: ", d_hand[0].value, d_hand[1].value)

    # Figure out sum of player dealt cards
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
    # Figure out sum of dealer dealt cards
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

    deck.print()
    print(deck.__len__())
    if p_value == d_value or (p_value > 21 and d_value > 21):
        return 2  # tie
    if p_value > 21 or (d_value > p_value and d_value < 22):
        return 1  # loss
    if d_value > 21 or (p_value <= 21 and p_value > d_value):
        return 0  # win


def inf_policy_1():

    deck = Deck()
    deck.shuffle()
    print("INF DECK POLICY 1 CALLED")
    p_hand = []
    p_value = 0

    d_hand = []
    d_value = 0
    # Adding cards to p_hand array
    p_hand.append(deck.deal())
    p_hand.append(deck.deal())
    deck.add_to_bottom(p_hand[0])
    deck.add_to_bottom(p_hand[1])
    deck.shuffle()

    print("Player Hand at 0 and 1 is: ", p_hand[0].value, p_hand[1].value)

    for i in range(2):
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
    p_value = p_hand[0].value + p_hand[1].value
    print("Initial Hand: ", p_hand[0].value, p_hand[1].value)

    # Adding cards to d_hand
    d_hand.append(deck.deal())
    d_hand.append(deck.deal())
    deck.add_to_bottom(d_hand[0])
    deck.add_to_bottom(d_hand[1])
    deck.shuffle()

    for i in range(2):
        if (d_hand[i].rank == 'ace'):
            d_hand[i].value = random.choice(ranks["ace"])
    d_value = d_hand[0].value + d_hand[1].value
    print("Dealer Hand: ", d_hand[0].value, d_hand[1].value)

    # Figure out sum of player dealt cards
    for i in range(2, 52):
        if p_value > 21:
            break
        if p_value == 21:
            break
        if p_value >= 17:
            break
        p_hand.append(deck.deal())
        deck.add_to_bottom(p_hand[i])
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
        print("Card drawn: ", p_hand[i].value)
        p_value += p_hand[i].value

    deck.shuffle()

    # Must hit if dealer's hand is not 17+
    # Figure out sum of dealer dealt cards
    if p_value <= 21:
        for i in range(2, 52):
            if d_value >= 17:
                break
            if d_value < 17:
                d_hand.append(deck.deal())
                deck.add_to_bottom(d_hand[i])
                if (d_hand[i].rank == 'ace'):
                    d_hand[i].value = random.choice(ranks["ace"])
                print("Dealer card drawn: ", d_hand[i].value)
                print(d_value)
                d_value += d_hand[i].value

    deck.shuffle()

    print("Player Hand Value  ",
          p_value, "Dealer Hand Value: ", d_value)

    print(deck.__len__())
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
        if p_value >= 17 and (p_hand[0].rank != 'ace' and p_hand[1].rank != 'ace'):
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


def inf_policy_2():

    deck = Deck()
    deck.shuffle()
    print("INF DECK POLICY 2 CALLED")
    p_hand = []
    p_value = 0

    d_hand = []
    d_value = 0

    p_hand.append(deck.deal())
    p_hand.append(deck.deal())
    deck.add_to_bottom(p_hand[0])
    deck.add_to_bottom(p_hand[1])
    deck.shuffle()

    for i in range(2):
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
    p_value = p_hand[0].value + p_hand[1].value
    print("Initial Hand: ", p_hand[0].value, p_hand[1].value)

    d_hand.append(deck.deal())
    d_hand.append(deck.deal())
    deck.add_to_bottom(d_hand[0])
    deck.add_to_bottom(d_hand[1])
    deck.shuffle()

    for i in range(2):
        if (d_hand[i].rank == 'ace'):
            d_hand[i].value = random.choice(ranks["ace"])
    d_value = d_hand[0].value + d_hand[1].value
    print("Dealer Hand: ", d_hand[0].value, d_hand[1].value)

    for i in range(2, 52):
        if p_value > 21:
            print("Bust!")
            break
        if p_value == 21:
            print("Blackjack!")
            break
        if p_value >= 17 and (p_hand[0].rank != 'ace' and p_hand[1].rank != 'ace'):
            print("Rank of Card is: ", p_hand[0].rank)
            break
        # if p_value >= 17 and (p_hand[1].rank == 'ace'):
        #     print("Rank of Card is: ", p_hand[1].rank)
        #     break
        p_hand.append(deck.deal())
        deck.add_to_bottom(p_hand[i])
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
        print("Card drawn: ", p_hand[i].value)
        p_value += p_hand[i].value

    deck.shuffle()
   # Must hit if dealer's hand is not 17+
    if p_value <= 21:
        for i in range(2, 52):
            if d_value >= 17:
                break
            if d_value < 17:
                d_hand.append(deck.deal())
                deck.add_to_bottom(d_hand[i])
                if (d_hand[i].rank == 'ace'):
                    d_hand[i].value = random.choice(ranks["ace"])
                print("Dealer card drawn: ", d_hand[i].value)
                print(d_value)
                d_value += d_hand[i].value

    deck.shuffle()
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


def inf_policy_3():

    deck = Deck()
    deck.shuffle()
    print("INF DECK POLICY 3 CALLED")
    p_hand = []
    p_value = 0

    d_hand = []
    d_value = 0

    p_hand.append(deck.deal())
    p_hand.append(deck.deal())
    deck.add_to_bottom(p_hand[0])
    deck.add_to_bottom(p_hand[1])
    deck.shuffle()

    for i in range(2):
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
    p_value = p_hand[0].value + p_hand[1].value
    print("Initial Hand: ", p_hand[0].value, p_hand[1].value)

    d_hand.append(deck.deal())
    d_hand.append(deck.deal())
    deck.add_to_bottom(d_hand[0])
    deck.add_to_bottom(d_hand[1])
    deck.shuffle()

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
                deck.add_to_bottom(d_hand[i])
                if (d_hand[i].rank == 'ace'):
                    d_hand[i].value = random.choice(ranks["ace"])
                print("Dealer card drawn: ", d_hand[i].value)
                print(d_value)
                d_value += d_hand[i].value

    deck.shuffle()
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


def inf_policy_4():
    deck = Deck()
    deck.shuffle()
    print("INF DECK POLICY 4 CALLED")
    p_hand = []
    p_value = 0

    d_hand = []
    d_value = 0

    p_hand.append(deck.deal())
    p_hand.append(deck.deal())
    deck.add_to_bottom(p_hand[0])
    deck.add_to_bottom(p_hand[1])
    deck.shuffle()

    for i in range(2):
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
    p_value = p_hand[0].value + p_hand[1].value
    print("Initial Hand: ", p_hand[0].value, p_hand[1].value)

    d_hand.append(deck.deal())
    d_hand.append(deck.deal())
    deck.add_to_bottom(d_hand[0])
    deck.add_to_bottom(d_hand[1])
    deck.shuffle()

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
        deck.add_to_bottom(p_hand[i])
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
        print("Card drawn: ", p_hand[i].value)
        p_value += p_hand[i].value

    deck.shuffle()
    # Must hit if dealer's hand is not 17+
    if p_value <= 21:
        for i in range(2, 52):
            if d_value >= 17:
                break
            if d_value < 17:
                d_hand.append(deck.deal())
                deck.add_to_bottom(d_hand[i])
                if (d_hand[i].rank == 'ace'):
                    d_hand[i].value = random.choice(ranks["ace"])
                print("Dealer card drawn: ", d_hand[i].value)
                print(d_value)
                d_value += d_hand[i].value

    deck.shuffle()
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
    print("SINGLE DECK POLICY 5 CALLED")
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


def inf_policy_5():
    deck = Deck()
    deck.shuffle()
    print("INF DECK POLICY 5 CALLED")
    p_hand = []
    p_value = 0

    d_hand = []
    d_value = 0

    p_hand.append(deck.deal())
    p_hand.append(deck.deal())
    deck.add_to_bottom(p_hand[0])
    deck.add_to_bottom(p_hand[1])
    deck.shuffle()

    for i in range(2):
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
    p_value = p_hand[0].value + p_hand[1].value
    print("Initial Hand: ", p_hand[0].value, p_hand[1].value)

    d_hand.append(deck.deal())
    d_hand.append(deck.deal())
    deck.add_to_bottom(d_hand[0])
    deck.add_to_bottom(d_hand[1])
    deck.shuffle()

    for i in range(2):
        if (d_hand[i].rank == 'ace'):
            d_hand[i].value = random.choice(ranks["ace"])
    d_value += d_hand[0].value + d_hand[1].value
    print("Dealer Hand: ", d_hand[0].value, d_hand[1].value)

    for i in range(2, 4):
        if p_value > 21:
            break
        if p_value == 21:
            break
        p_hand.append(deck.deal())
        deck.add_to_bottom(p_hand[i])
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])
        print("Card drawn: ", p_hand[i].value)
        p_value += p_hand[i].value
    deck.shuffle()
    # Must hit if dealer's hand is not 17+
    if p_value <= 21:
        for i in range(2, 52):
            if d_value >= 17:
                break
            if d_value < 17:
                d_hand.append(deck.deal())
                deck.add_to_bottom(d_hand[i])
                if (d_hand[i].rank == 'ace'):
                    d_hand[i].value = random.choice(ranks["ace"])
                print("Dealer card drawn: ", d_hand[i].value)
                print(d_value)
                d_value += d_hand[i].value
    deck.shuffle()
    print("Player Hand Value  ",
          p_value, "Dealer Hand Value: ", d_value)

    if p_value == d_value or (p_value > 21 and d_value > 21):
        return 2  # tie
    if p_value > 21 or (d_value > p_value and d_value < 22):
        return 1  # loss
    if d_value > 21 or (p_value <= 21 and p_value > d_value):
        return 0  # win


def main():
    lose1 = 0
    win1 = 0
    tie1 = 0
    lose2 = 0
    win2 = 0
    tie2 = 0
    lose3 = 0
    win3 = 0
    tie3 = 0
    lose4 = 0
    win4 = 0
    tie4 = 0
    lose5 = 0
    win5 = 0
    tie5 = 0
    lose6 = 0
    win6 = 0
    tie6 = 0
    lose7 = 0
    win7 = 0
    tie7 = 0
    lose8 = 0
    win8 = 0
    tie8 = 0
    lose9 = 0
    win9 = 0
    tie9 = 0
    lose10 = 0
    win10 = 0
    tie10 = 0
    outcome1 = None
    outcome2 = None
    outcome3 = None
    outcome4 = None
    outcome5 = None
    outcome6 = None
    outcome7 = None
    outcome8 = None
    outcome9 = None
    outcome10 = None

   # This is our for loop for grabbing wins and losses for each policy and version.
    for i in range(10):
        outcome1 = inf_policy_1()
        outcome2 = inf_policy_2()
        outcome3 = inf_policy_3()
        outcome4 = inf_policy_4()
        outcome5 = inf_policy_5()
        outcome6 = single_policy_1()
        outcome7 = single_policy_2()
        outcome8 = single_policy_3()
        outcome9 = single_policy_4()
        outcome10 = single_policy_5()
        if (outcome1 == 0):
            win1 += 1
        if(outcome1 == 1):
            lose1 += 1
        if (outcome1 == 2):
            tie1 += 1
        if (outcome2 == 0):
            win2 += 1
        if (outcome2 == 1):
            lose2 += 1
        if (outcome2 == 2):
            tie2 += 1
        if (outcome3 == 0):
            win3 += 1
        if (outcome3 == 1):
            lose3 += 1
        if (outcome3 == 2):
            tie3 += 1
        if (outcome4 == 0):
            win4 += 1
        if (outcome4 == 1):
            lose4 += 1
        if (outcome4 == 2):
            tie4 += 1
        if (outcome5 == 0):
            win5 += 1
        if (outcome5 == 1):
            lose5 += 1
        if (outcome5 == 2):
            tie5 += 1
        if (outcome6 == 0):
            win6 += 1
        if (outcome6 == 1):
            lose6 += 1
        if (outcome6 == 2):
            tie6 += 1
        if (outcome7 == 0):
            win7 += 1
        if (outcome7 == 1):
            lose7 += 1
        if (outcome7 == 2):
            tie7 += 1
        if (outcome8 == 0):
            win8 += 1
        if (outcome8 == 1):
            lose8 += 1
        if (outcome8 == 2):
            tie8 += 1
        if (outcome9 == 0):
            win9 += 1
        if (outcome9 == 1):
            lose9 += 1
        if (outcome9 == 2):
            tie9 += 1
        if (outcome10 == 0):
            win10 += 1
        if (outcome10 == 1):
            lose10 += 1
        if (outcome10 == 2):
            tie10 += 1

    print("INF POLICY 1 Wins: ",  win1, "Losses: ",  lose1, "Ties: ", tie1)
    print("INF POLICY 2 Wins: ",  win2, "Losses: ",  lose2, "Ties: ", tie2)
    print("INF POLICY 3 Wins: ",  win3, "Losses: ",  lose3, "Ties: ", tie3)
    print("INF POLICY 4 Wins: ",  win4, "Losses: ",  lose4, "Ties: ", tie4)
    print("INF POLICY 5 Wins: ",  win5, "Losses: ",  lose5, "Ties: ", tie5)
    print("SINGLE POLICY 1 Wins: ",  win6, "Losses: ",  lose6, "Ties: ", tie6)
    print("SINGLE POLICY 2 Wins: ",  win7, "Losses: ",  lose7, "Ties: ", tie7)
    print("SINGLE POLICY 3 Wins: ",  win8, "Losses: ",  lose8, "Ties: ", tie8)
    print("SINGLE POLICY 4 Wins: ",  win9, "Losses: ",  lose9, "Ties: ", tie9)
    print("SINGLE POLICY 5 Wins: ",  win10,
          "Losses: ",  lose10, "Ties: ", tie10)

    # labels = ['Win/loss']
    # wins = [win1]
    # losses = [lose1]
    # width = 0.35       # the width of the bars: can also be len(x) sequen
    # fig, ax = plt.subplots()
    # ax.bar(labels[1], wins, width,  label='wins')
    # ax.bar(labels[0], losses, width, label='losses')
    # ax.set_title('Wins Loss ratio using Policy 1')
    # ax.legend
    # plt.show()
##############################################################################
    WLlabels = ['INF 1', 'INF 2', 'INF 3', 'INF 4', 'INF 5']
    infW = [win1, win2, win3, win4, win5]
    infL = [lose1, lose2, lose3, lose4, lose5]

    x = np.arange(len(WLlabels))  # the label locations
    infWidth = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1I = ax.bar(x - infWidth/2, infW, infWidth, label='Wins')
    rects2I = ax.bar(x + infWidth/2, infL, infWidth, label='Losses')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number of Wins/Losses')
    ax.set_title('Infinite Deck Policy Wins and Losses')
    ax.set_xticks(x)
    ax.set_xticklabels(WLlabels)
    ax.legend()

    ax.bar_label(rects1I, padding=3)
    ax.bar_label(rects2I, padding=3)

    fig.tight_layout()

    plt.show()
##############################################################################
    WLlabels2 = ['SINGLE 1', 'SINGLE 2', 'SINGLE 3', 'SINGLE 4', 'SINGLE 5']
    sW = [win6, win7, win8, win9, win10]
    sL = [lose6, lose7, lose8, lose9, lose10]

    x2 = np.arange(len(WLlabels2))  # the label locations
    sWidth = 0.35  # the width of the bars

    fig2, ax2 = plt.subplots()
    rects1 = ax2.bar(x - sWidth/2, sW, sWidth, label='Wins')
    rects2 = ax2.bar(x + sWidth/2, sL, sWidth, label='Losses')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax2.set_ylabel('Number of Wins/Losses')
    ax2.set_title('Single Deck Policy Wins and Losses')
    ax2.set_xticks(x2)
    ax2.set_xticklabels(WLlabels2)
    ax2.legend()

    ax2.bar_label(rects1, padding=3)
    ax2.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()


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
