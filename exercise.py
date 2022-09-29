#!/usr/bin/env python3
"""Alta3 Research | MayuriDalavai
   List, Input, Print, Concatenate, Variables"""
import random

def main():

     # create a wordbank list 
     wordbank = ["indentation", "spaces"]

     # create a students list
     tlgstudents = ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima",
    "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

     # append 4 to the list wordbank
     wordbank.append(4)
     print(wordbank)

     num =int(input("choose a number between 0 and 18: "))
     name = tlgstudents[num]

     print(f"Your Choice  of tlgstudents is {name}!")
     print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")

     name = random.choice(tlgstudents)
     print(f"{name}")


main()     
