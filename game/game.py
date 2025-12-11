import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        else:
            break
    except ValueError:
        continue

number = random.randrange(1, level + 1)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
        elif guess < number:
            print("Too small!")
            continue
        elif guess > number:
            print("Too large!")
            continue
        elif guess == number:
            print("Just right!")
            break
    except ValueError:
        continue

