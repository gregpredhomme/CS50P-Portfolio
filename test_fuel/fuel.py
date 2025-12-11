def main():
    while True:
        fraction_str = input("Fraction: ")
        try:
            percentage = convert(fraction_str)
            output = gauge(percentage)
            print(output)
            break
        except (ValueError, ZeroDivisionError):
                pass

def convert(fraction):
    try:
        x_str, y_str = fraction.split("/")
        x = int(x_str)
        y = int(y_str)
        fraction = x / y
    except ValueError:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    if x > y or x < 0 or y < 0:
        raise ValueError
    percentage = round((x / y) * 100)
    return percentage

def gauge(percentage):
        if percentage <= 1:
             return "E"
        elif percentage >= 99:
             return "F"
        else:
             return f"{percentage}%"

if __name__ == "__main__":
    main()






