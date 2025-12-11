from datetime import date
import sys
import inflect

def main():
    user_input = input("Date of Birth: ")
    try:
        birth_date = date.fromisoformat(user_input)
    except ValueError:
        sys.exit("Invalid date")
    today = date.today()
    minutes = get_minutes(birth_date, today)
    print(format_words(minutes))

def get_minutes(birth, current):
    diff = current - birth
    minutes = diff.days * 24 * 60
    return minutes

def format_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"

if __name__ == "__main__":
    main()
