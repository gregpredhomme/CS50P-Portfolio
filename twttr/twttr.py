text = input("Input: ")
VOWELS = ['a', 'e', 'i', 'o', 'u']

output = ""

for i in text:
    if i.lower() not in VOWELS:
        output += i

print(output)

