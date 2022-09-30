#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   nesting an if-statement inside of a for loop"""

def main():
    # create a list of farms
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
    # loop across the list called farms
    for farm in farms:
        print(farm.get("name", "Unknown Farm"), end=":\n")

        for agri in farm.get("agriculture"):
            print("  -", agri)

if __name__ == "__main__":
    main()

