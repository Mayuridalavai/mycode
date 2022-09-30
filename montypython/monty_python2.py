#!/usr/bin/env python3
"""Alta3 Research | MDalavai
   Conditionals - Life of Brian guessing game using a while True loop."""

def main():
    round = 0
    while True:
        round = round + 1
        print('Finish the movie title, "Monty Python\'s The Life of ______"')
        answer = input("Your guess--> ")
        
        if answer == 'Brain':
            print('correct')
            break
        elif round == 3:
            print("Sorry, the answer was Brain.")
            break
        else:
            print("Sorry! Try again!")


main()

