month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        input_date = input("Date: ")
        if "/" in input_date:
            m, d, y = input_date.split("/")
            m = int(m)
            d = int(d)
            y = int(y)
            if m > 12 or d > 31:
                continue
        else:
            new_date = input_date.title().split()
            m = int(month.index(new_date[0]) + 1)
            if "," not in new_date[1]:
                continue
            else:
                d = int(new_date[1].replace(",",""))
            y = int(new_date[2])
            if m > 12 or d > 31:
                continue
        print(f"{y}-{m:02}-{d:02}")
        break
    except ValueError:
        continue
