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
#   5. If first Card < 10 and second card < 10 always hit
#######################################################################
import enum
import random
import array
import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd


lose = 0
win = 0
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

suits = ['clubs', 'diamonds', 'hearts', 'spades']\



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


def dealer_eval(player_hand):
    num_ace = 0
    use_one = 0
    for card in player_hand:
        if card.rank == "ace":
            num_ace += 1
            use_one += card.value[0]  # use 1 for Ace
        else:
            use_one += card.value

    if num_ace > 0:
        # See if using 11 instead of 1 for the Aces gets the
        # dealer's hand value closer to the [17, 21] range

        # The dealer will follow Hard 17 rules.
        # This means the dealer will not hit again if
        # the Ace yields a 17.

        # This also means that Aces initially declared as 11's can
        # be changed to 1's as new cards come.

        ace_counter = 0
        while ace_counter < num_ace:
            # Only add by 10 b/c 1 is already added before
            use_eleven = use_one + 10

            if use_eleven > 21:
                return use_one
            elif use_eleven >= 17 and use_eleven <= 21:
                return use_eleven
            else:
                # The case where even using Ace as eleven is less than 17.
                use_one = use_eleven

            ace_counter += 1

        return use_one
    else:
        return use_one

# if hand >= 17, stick - otherwise hit


def single_policy_1():
    deck = Deck()
    deck.shuffle()
    print("SINGLE DECK POLICY 1 CALLED")
    p_hand = []
    p_value = 0

    p_hand.append(deck.deal())
    p_hand.append(deck.deal())
    print("Initial Hand: ", p_hand[0].value, p_hand[1].value)
    for i in range(2):
        if (p_hand[i].rank == 'ace'):
            p_hand[i].value = random.choice(ranks["ace"])

    p_value = p_hand[0].value + p_hand[1].value

    #print("Player Hand Value is: ", p_value)
    # print(random.choice(ranks["ace"]))

    if p_value >= 17:
        print("Player sticked")
        pass
    else:
        for i in range(2, 52):
            if p_value >= 21:
                break
            p_hand.append(deck.deal())
            if (p_hand[i].rank == 'ace'):
                p_hand[i].value = random.choice(ranks["ace"])
            print("Card drawn: ", p_hand[i].value)
            p_value += p_hand[i].value

    print("Player Hand Value After policy 1 is: ", p_value)

    if p_value > 21:
        return False
    if p_value <= 21:
        return True


def policyFour():
    pass


def main():
    global lose
    global win
    single_policy_1()
    for i in range(1000):
        if (single_policy_1() == True):
            win += 1
        else:
            lose += 1
    print("Wins: ",  win, "Loses: ",  lose)


labels = ['losses', 'wins']
men_means = [20]
women_means = [25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='win')
rects2 = ax.bar(x + width/2, women_means, width, label='losses')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

#ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

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
