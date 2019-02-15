# Henri Richardson
# Exercise 8.py
# Blackjack simulator

# print explanation of program
# get number of games to simulate
# simulate the games
# print probability of dealer busting

from random import *

def intro():
    print("This program will simulate the dealer's hand in'n' number of games of Blackjack\nand calculate the probability of the dealer busting.\n")

def getGames():
    n = eval(input("How many games to simulate?: "))
    return n

def simNBlackJ(n):
    busts = 0
    for i in range(n):
        if bustOneGame():
            busts = busts+1
    return busts


def bustOneGame():
   hand = 0
   hasAce = False
   while hand < 17:
       card = randrange(1,14)
       if 1 <= card <= 10:
           hand = hand + card
           if card == 1:
               hasAce = True
        else:
            hand += 10
       # if hasAce and 17 <= hand + 10 <= 21:
            hand += 10
    if hand > 21:
        return True
    return False
            

def printEnd(busts, n):
    prob = busts/n
    print("\nA total of {2} games were played.\nOut of these {2} games, the dealer bust {1} of them.\nSo, the dealer bust on {0:.1%} of games.".format(prob, busts, n))

    
def main():
    intro()
    n = getGames()
    busts = simNBlackJ(n)
    printEnd(busts, n)
main()
