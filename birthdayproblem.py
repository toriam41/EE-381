# Birthday Problem

P = 1.0 # 1 person in the room
K = 50 # repetitions through the loop

for k in range(1, K - 1):
    P = P * ((365 - k + 1) / 365)
    print(k, 1 - P)
