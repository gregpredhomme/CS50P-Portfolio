import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")







# def meow(n: int) -> str:
#     """Meow n times."""
#     return "meow\n" * n

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")

