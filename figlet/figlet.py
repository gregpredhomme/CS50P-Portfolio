from pyfiglet import Figlet, FontNotFound
import random
import sys

figlet = Figlet()

font_list = figlet.getFonts()
#print(font_list)
random_font = random.choice(font_list)

try:
    if len(sys.argv) == 1:
        figlet.setFont(font=random_font)
        user_str = input("Input: ")
        print(figlet.renderText(user_str))
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            figlet.setFont(font=sys.argv[2])
            user_str2 = input("Input: ")
            print(figlet.renderText(user_str2))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
except FontNotFound:
    sys.exit("Invalid usage")






