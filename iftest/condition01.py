#!/usr/bin/env python3
"""Alta3 Research | MDalavai
  If  conditional statement"""

def main():
    ## Collect input from user
    hostname = input("What value should we set for hostname?")

    ## use the lower method to test if input value matches expected value
    if hostname.lower() == "mtg":
       print("The hostname was found to be mtg")
       print("hostname matches expected config")

    ## Always print out to the user
       print("Exiting the script")


main()
