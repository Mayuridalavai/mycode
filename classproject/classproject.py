#!/usr/bin/env python3
""" MDalavai | Alta3 Research
    Learn Python Project"""

import pyfiglet
import requests
from pprint import PrettyPrinter
import json


    
URL = "https://api.fastforex.io/currencies?api_key=67f42a4e33-1fcc5e9d1e-rj7nis"

printer = PrettyPrinter()


def get_currencies():
    data = requests.get(URL)
    data = data.json()
    for currency in currencies["currencies"]:
        print(data[])






def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    if len(data) == 0:
        print('Invalid currencies.')
        return

    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")

    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount

def main():
    

    welcome = pyfiglet.figlet_format("Welcome to Curency Converter", font = "bubble")
    print(welcome)

    user = input("Enter your Name: ")
    print("------------------------------------------------")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")

    

    while True:
        answer = input("Enter a option from the List above  or  q to quit:").lower()

        if answer == 'q':
            break
        elif answer == 'list':
            get_currencies(currencies)
        elif answer == 'convert':
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif answer == 'rate':
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)

        else:
            print("Invalid Entry")



        


main()    
