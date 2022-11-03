import json
import requests
import sys


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
result = response.json()
price = result['bpi']['USD']['rate']
price = float(price.replace(",", ""))


if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
elif sys.argv[1].isalpha():
    sys.exit("Command-line argument is not a number")
else:
    n = float(sys.argv[1])
    amount = n * price
    print(f"${amount:,.4f}")