#!/usr/bin/env python3
""" Alta3 Research || MDalavai"""
import json

def commandpush(devicecmd):

    for ip in devicecmd.keys():
        print(f'Handshaking. .. ... connecting with {ip}')

        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')

    return None

def main():
    """called at runtime"""

    with open("devicecmd.json", "r") as devicecmdfile:
        devicecmd = json.load(devicecmdfile)



    print("Welcome to the network device command pusher")

    print("\nData set found\n")

    commandpush(devicecmd)

main()    
