#!/bin/bash

# This application is to Create users and groups
# Createuser ia function to create new user and groups and add user to group
# Promptuser is a function to ask name of user and group
# Used While loop to continue to add more users and groups otherwise quit

createuser(){
    sudo useradd $USER
    echo "$USER User is created"
    sleep 1
    sudo groupadd $GROUP
    echo "$GROUP Group is created"
    sleep 1
    sudo usermod -aG $GROUP $USER
    echo "$USER is added to $GROUP"
    id $USER
}

promptuser(){
    echo "Enter the Name of New User"
    read USER
    echo "Enter the Group for the User"
    read GROUP
}

quit(){
    echo "would you like to quit enter exit or press Enter"
    read quit
}

while [ "$quit" != "exit" ]
do 
   promptuser
   createuser
   quit
done 
echo "Thank you...!"
