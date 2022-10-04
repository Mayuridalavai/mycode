#!/usr/bin/env python3
""" MDalavai | Alta3 Research
    Learn Python Project"""

import pyfiglet

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
            print("currencies")
         
        elif answer == 'convert':
            print("convert")
        elif answer == 'rate':
            print("rate")

        else:
            print("Invalid Entry")



        


main()    
