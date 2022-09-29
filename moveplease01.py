#!/usr/bin/env python3
"""A simple script to move two files into ceph_storage/
   Alta3 Research | rzfeeser@alta3.com"""

# standard library imports
import shutil
import os

def main():

    os.chdir('/home/student/mycode/')   # move into this working directory
    shutil.move('raynor.obj', 'ceph_storage/')   # try moving the file raynor.obj into ceph    _storage/ dir
    
    # program will pause while we accept input
     # collect string input from the user
    xname = input('What is he new name for kerrigan.obj? ')
    # moving kerrigan.obj into ceph_storage/ with new name
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


    main()



