def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

user_text = input()
print(convert(user_text))
