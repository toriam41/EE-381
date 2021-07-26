"""
Tori McDonald - 018447739
EE 381-07 - Spring 2021
1/31/21

Linear congruential pseudorandom number generator program to generate random
numbers between [0,1).
"""

import math

def rng():
    N = 10000 # norm
    A = 4857 # adder
    M = 8601 # multiplier
    S = 0 # seed

    for i in range(100):
        S = ((M * S) + A) % N
        r = S / N
        print("%d) %.4f" % (i + 1, r))

def coinflip():
    N = 10000 # norm
    A = 4857 # adder
    M = 8601 # multiplier
    S = 0 # seed

    for i in range(25):
        S = (M * S + A) % N
        r = S / N
        coin = math.floor(2 * r)

        if coin == 0:
            print("Tails")
        else:
            print("Heads")

def dieroll():
    N = 10000 # norm
    A = 4857 # adder
    M = 8601 # multiplier
    S = 0 # seed

    for i in range(25):
        S = (M * S + A) % N
        r = S / N
        die = math.ceil(6 * r)

        print(die)

def main():
    choice = int(input("Choose the function you'd like to run:\n1) Generate 100 random numbers\n2) Coin Flip\n3) Die Roll\n"))

    if choice == 1:
        rng()
    elif choice == 2:
        coinflip()
    elif choice == 3:
        dieroll()
    else:
        return 1

main()
