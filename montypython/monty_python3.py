#!/usr/bin/python3
"""Alta3 Research | MDalavai
  Conditionals - Life of Brian guessing game without a while True loop."""

def main():
    round = 0
    answer = " "

    round = round + 1

    while round < 3  
        round += 1
        answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
        answer = answer.capitalize()
        if answer == "Brian":
            print("Correct!")
        elif answer == "Shrubbery":
             print("You gave the super secret answer!")
        elif round == 3:
            print("Sorry, the answer was Brian.")
        else:
            print("Sorry. Try again!")


main()            
