# Poisson

import math
import matplotlib.pyplot as plt

L = float(input("Enter Poisson parameter: "))
N = 25 # number of probabilities calculated
P = math.exp(-L)
X = [0] # horizontal axis
Y = [P] # vertical axis

for i in range(N):
    if i > 0:
        P = P*(L / i)
        X.append(i)
        Y.append(P)
    print(i, P)

plt.plot(X, Y, 'r+')
plt.show()
