import random

times = 0
n = random.randint(1, 100)
while True:
    a = float(input("whats your guess: "))
    times += 1
    if a == n:
        print(f"you won cause the number was {n} and you won with {times} times")
        break
    elif a > n:
        print("guess lower")
    else:
        print("guess higher")
