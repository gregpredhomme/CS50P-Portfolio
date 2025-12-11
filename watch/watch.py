import re

def main():
    s = print(parse(input("HTML: ")))
    return s


def parse(s):
    matches = re.search(r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"', s)
    if matches:
        id = matches.group(1)
        return f"https://youtu.be/{id}"
    return None


if __name__ == "__main__":
    main()
