
import inflect
p = inflect.engine()

# Ask user for names - 1 per line
# user hits ctrl d

# print names - seperate 2 names with "and" and three names wiht 2 commas and "and" and n names with n-1 commas and one "and"

name_list = []
while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except EOFError:
        print()
        final = ("Adieu, adieu, to " + p.join((name_list)))
        print(final)
        break



