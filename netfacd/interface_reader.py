#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try:
        print('MAC: ', end='')
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr'])
        print('IP:', end='')
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr'])
    except:
        print('Could not collect adapter information')

i = input("what adaptor would you like to obtain the MAC address from?")
print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr'])
i = input("What adaptor would you like to abtain the IP addtess from?")
print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr'])
