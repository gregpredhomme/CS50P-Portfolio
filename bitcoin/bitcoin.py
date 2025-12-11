import json
import sys
import requests
try:
    btc_info = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=31da101ab4d63dd899fbefdfe6ef8fac3d8ebc7b7832afcac09acb43dc00b753")
    o = btc_info.json()
    btc_price = float(o["data"]["priceUsd"])
    amount = btc_price * float(sys.argv[1])
    print(f"${amount:,.4f}")
except IndexError:
    print("Missing command-line argument")
    sys.exit(1)
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)
except requests.RequestException:
    print("API error")
    sys.exit(1)
