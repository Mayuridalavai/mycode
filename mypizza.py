#!/usr/bin/env python3
"""Alta3 Research | MDalavai
   Pizza Party"""

import numpy as np
import matplotlib.pyplot as plt
import time

print("welcome to the Pizza App!")
answer= input(" Are you Ready to order Pizza? say Yes or no -->")

if answer.lower() =="yes":
    print("Awesome! Ordering your pizza now!")
    time.sleep(2)
    print("This may take a few seconds to get ready...", end=' ',flush=True)
    time.sleep(2)
    print("...", end=' ', flush=True)
    time.sleep(2)
    print(".", flush=True)
    time.sleep(2)
    print("Your pizza is Done! and It has been delivered to static Directory!")


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'cheese', 'BBQ chicken', 'fried onions', 'Jalapenos','mushrooms','sausage'
sizes = [30, 20, 10, 5, 5, 10]
explode = (0.1, 0, 0, 0, 0, 0)  # only "explode" the lst slice (i.e. 'cheese')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig("/home/student/static/mypizza.png

