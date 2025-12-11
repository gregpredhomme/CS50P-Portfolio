while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        fraction = x / y
        if x > y or y <= 0 or x < 0:
            pass
        elif 0.01 < fraction < 0.99:
            print(f"{fraction:.0%}")
            break
        elif fraction <= 0.01:
            print("E")
            break
        elif fraction >= 0.99:
            print("F")
            break
    except (ValueError, ZeroDivisionError):
        pass








