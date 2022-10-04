#!/usr/bin/python3
"""Alta3 Research | MDalavai
   Challenge  - CSV to Excel and JSON to Excel"""

import pandas

def main():

    # create a dataframe from csv
    df = pandas.read_csv("5movies.csv")
    df2 = pandas.read_json("5movies.json")

    # writeout dataframe to excel
    df.to_excel("5movies-translated-from-json.xlsx")
    df2.to_excel("5movies-translated-from-json.xlsx")

if __name__ == "__main__":
    main()

