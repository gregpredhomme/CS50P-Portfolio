def main():
    shorten("word")

def shorten(word):
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    output = ""

    for i in word:
        if i.lower() not in VOWELS:
            output += i
    return output

if __name__ == "__main__":
    main()

