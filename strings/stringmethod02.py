#!/usr/bin/env python3
"""Alta3 Research || Author: MDalavai"""

def main():
    # create a small string
    lilstring = "Alta3 Research offers classes on Python coding"
    newlist = lilstring.split(" ")
    print(newlist)

    # create a list of strings
    myiplist = ["192", "168", "0", "12"]
    singleip = ".".join(myiplist)
    print(singleip)

# call our main function
main()    
