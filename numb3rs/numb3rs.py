import re
import sys

def main():
    ip = print(validate(input("IPv4 Address: ")))
    return ip

def validate(ip):
    matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)
    if matches:
        for part in matches.groups():
            if int(part) < 0 or int(part) > 255:
                return False
            if len(part) > 1 and part.startswith("0"):
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
