def main():
    time_str = input("what is the time?")
    time_float = convert(time_str)
    if 7.0 <= time_float <= 8.0:
        print('breakfast time')
    elif 12.0 <= time_float <= 13.0:
        print('lunch time')
    elif 18.0 <= time_float <= 19.0:
        print('dinner time')

def convert(time):
    hours_str, minutes_str = time.split(":")
    hours = float(hours_str)
    minutes = float(minutes_str)
    minutes_as_hour = minutes / 60
    return hours + minutes_as_hour

if __name__ == "__main__":
    main()
