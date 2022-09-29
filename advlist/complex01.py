#!/usr/bin/env python3
"""Alta3 Research | MayuriDalavai
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    #display list1
    print(list1)

    #display list[1] which should only display arista_eos
    print(list1[1])

    # create new list containing a songle item
    list2 = ["juniper"]

    # extend liat1 by list by combining both lists together in to single list
    list1.extend(list2)

    # display list1, which has juniper
    print(list1)

    # create list3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    # use append to append list1 by list3
    list1.append(list3)

    # display the new list1
    print(list1)

    #display the list of IP addresses
    print(list1[4])

    # display the first item in the list (0th item) - first IP address
    print(list1[4][0])


main()
