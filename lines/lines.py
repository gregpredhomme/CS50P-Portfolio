import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")


lines = 0
try:
    with open(sys.argv[1]) as file:
        for line in file:
            if line.lstrip() != "" and line.lstrip().startswith("#") is False:
                lines += 1
        print(lines)
except FileNotFoundError:
    sys.exit("File does not exist")



