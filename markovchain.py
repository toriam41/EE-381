# Markov  chain

RecLoc = [] # Records location of the particle

import random

N = 1000 # number of steps
p_A = float(input("Enter the probability of leaving 0 and going to 1: "))
p_B = float(input("Enter the probability of leaving 1 and going to 0: "))
S = int(input("Starting state of either 0 or 1: "))

RecLoc.append(S)

for i in range(N):
    r = random.uniform(0,1)

    if S == 0 and r < p_A:
        S = 1 # moved to state one
    elif S == 1 and r < p_B:
        S = 0 # moved to state zero

    RecLoc.append(S)

X = 0 # initial value

for x in RecLoc:
    X = X + x # accumulation

print("Percentage in State 1: ", X / N)
print("Percentage in State 2: ", 1 - (X / N))
