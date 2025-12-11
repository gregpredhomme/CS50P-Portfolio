def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s[0:2].isalpha() is False:
        return False
    if len(s) > 6 or len(s) < 2:
        return False

    found_number = False

    for i in range(len(s)):
        char = s[i]

        if char.isalpha() == False and char.isdigit() == False:
            return False
        if char.isdigit():
            if found_number == False:
                if char == '0':
                    return False
                found_number = True
        if found_number == True and char.isalpha():
            return False
    return True

if __name__ == "__main__":
    main()
