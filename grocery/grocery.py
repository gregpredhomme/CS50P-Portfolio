
grocery_dict = {}
while True:
    try:
        grocery = input().strip().upper()
        grocery_dict[grocery] = grocery_dict.get(grocery, 0) + 1
    except KeyError:
        pass
    except EOFError:
        for grocery, count in sorted(grocery_dict.items()):
            print(f"{count} {grocery}")
        break
