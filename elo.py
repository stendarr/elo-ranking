#!/usr/bin/env python3
from random import randint
import os.path, sys

# Take filename from input or directly state it in the script:
if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = input("Enter the filename of the list: ").strip()
#filename = 'test_list.txt'
if not os.path.isfile(filename):
    if os.path.isfile(filename+".txt"):
        filename += ".txt"
    else:
        print("File not found.")
        sys.exit(1)
lines = [line.rstrip('\n') for line in open(filename)]

# This is the parameter which makes "wins" more or less important
# In normal chess games this is usually 20
k = 45.0

list = []
for i in lines:
    # Skip line if empty
    if i.strip() == "":
        continue
    splitted = i.split(",")
    element_name = splitted[0].strip()
    # Initialize with 0, 1000 if only name
    if len(splitted) == 1:
        count = 0.0
        elo = 1000.0
    # Initialize with 0, 1000 if second cl argument is init
    elif len(sys.argv) == 3 and sys.argv[2] == 'init':
        count = 0.0
        elo = 1000.0
    else:
        count = float(splitted[1].strip())
        elo = float(splitted[2].strip())
    i = [element_name, count, elo]
    list.append(i)

l = len(list)
try:
    while True:
        # Get two random elements
        a = randint(0,l-1)
        b = randint(0,l-1)
        while a == b:
            b = randint(0,l-1)
        # Get one of the least tested items
        min = [0, 9999, 0]
        min_index = 0
        for i in list:
            if i[1] < min[1]:
                min = i
                min_index = list.index(i)
        if a != min_index:
            b = min_index

        # Get elo from selected elements and calculate their expected value
        element_a = list[a]
        element_b = list[b]
        R_a = element_a[2]
        R_b = element_b[2]
        E_a = 1/(1 + (10**((R_b - R_a)/400)))
        E_b = 1/(1 + (10**((R_a - R_b)/400)))

        inpt = str(input("\nWhich one is better?\n[1] "+str(element_a[0])
        +" or [2] "+str(element_b[0])+"\nEnter 3 if they're equal.\n"))

        if "1" in inpt:
            # Calculate Elo if 1 wins
            element_a[2] = R_a + k*(1-E_a)
            element_b[2] = R_b + k*(0-E_b)
            # Increment counter
            element_a[1] += 1
            element_b[1] += 1
        elif "2" in inpt:
            # Calculate elo if 2 wins
            element_b[2] = R_b + k*(1-E_b)
            element_a[2] = R_a + k*(0-E_a)
            # Increment counter
            element_a[1] += 1
            element_b[1] += 1
        elif "3" in inpt:
            # Calculate elo if draw
            element_b[2] = R_b + k*(0.5-E_b)
            element_a[2] = R_a + k*(0.5-E_a)
            # Increment counter
            element_a[1] += 1
            element_b[1] += 1
        else:
            print("Are you taking the piss? Enter 1, 2, or 3.\n")
# Stop on ctrl+c
except KeyboardInterrupt as e:
    print("\n")
    for i in list:
        print(i)

write_string = ''
# Stores the elements sorted by their ranks
while list != []:
    max = [0, 0, 0]
    for i in list:
        if i[2] > max[2]:
            max = i
    for i in max:
        write_string += str(i)+", "
    write_string += "\n"
    list.remove(max)

list_file = open(filename, "w")
list_file.write(write_string)
list_file.close()
