#!/usr/bin/env python3
"""Alta3 Research | MDalavai
   if, elif, else - A simple program using conditionals to make a decision."""
def main():
    speed = float(input("What is your network speed in Mbps"))

    if speed >= 25:
         print('Your network speed is Advances service')
    elif speed >= 12:
         print('Your network speed is medium range')
    elif speed >= 8:
         print('Your network speed is Basic range')
    else:
         print('Your network speed is low range')


main()          
        
