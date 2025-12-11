import random

def main():
    digit_count = get_level()
    score = 0
    for _ in range(10):
        X = generate_integer(digit_count)
        Y = generate_integer(digit_count)
        for _ in range(3):
            try:
                answer = int(input(f"{X} + {Y} = "))
                if answer == (X + Y):
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{X + Y}")
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level != 1 and level != 2 and level != 3:
                continue
            else:
                break
        except ValueError:
            continue
    return level

def generate_integer(level):
    if level == 1:
        number = random.randrange(0, 10)
    elif level == 2:
        number = random.randrange(10, 100)
    elif level == 3:
        number = random.randrange(100, 1000)
    return number

if __name__ == "__main__":
    main()
