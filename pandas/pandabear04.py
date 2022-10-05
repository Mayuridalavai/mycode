#!/usr/bin/python3

import pandas as pd

def main():
    # create a dataframe ciscocsv
    ciscocsv = pd.read_csv("ciscodata.csv")
    # create a dataframe ciscojson
    ciscojson = pd.read_json("ciscodata2.json")

    # The line below concats and reapplies the index value
    ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)

    ## print to the screen the re-indexed dataframe
    print(ciscodf)
    
    ## print a blankline
    print()

    ## export to json
    ciscodf.to_json("combined_ciscodata.json", orient="records")

    ## export to csv
    ciscodf.to_csv("combined_ciscodata.csv", index=False)
    
    ## export to Excel
    ciscodf.to_excel("combined_ciscodata.xls", index=False)

    ## do not include index number to xlsx
    ciscodf.to_excel("combined_ciscodata.xlsx", index=False)
    
    ## create a python dictionary
    x = ciscodf.to_dict(orient='records')
    print(x)
    
if __name__ == "__main__":
    main()

