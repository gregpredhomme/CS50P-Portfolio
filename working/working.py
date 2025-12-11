import re

def main():
    s = print(convert(input("Hours: ")))

def convert(s):
    rexp = r"^([0-9]+)?(?::([0-9]{2}))? (AM|PM) to ([0-9]+)(?::([0-9]{2}))? (AM|PM)$"
    match = re.search(rexp, s)

    if not match:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = match.groups()

    time1 = normalize(h1, m1, p1)
    time2 = normalize(h2, m2, p2)

    return f"{time1} to {time2}"

def normalize(hour, minute, period):
    if minute is None:
        minute = 0
    h = int(hour)
    m = int(minute)

    if m >= 60:
        raise ValueError
    if h > 12:
        raise ValueError

    if period == "PM":
        if h != 12:
            h += 12
    else:
        if h == 12:
            h = 0
    return f"{h:02}:{m:02}"

if __name__ == "__main__":
    main()
