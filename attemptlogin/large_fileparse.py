#!/usr/bin/env python3

def main():
    # counter for fails
    loginfail = 0
    # open the file for reading
    keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

    # loop over the file
    for line in keystone_file:

        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
       
    print("The number of failed log in attempts is", loginfail)
    keystone_file.close() # close the open file  


main()
