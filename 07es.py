## Write a program that reads in a text file and outputs the number of e's it contains. 
## Think about what is being asked here, document any assumptions you are making.
## The program should take the filename from an argument on the command line.


import sys

filename = sys.argv[1]
with open(filename, 'r') as f:
    contents = f.read()

count = 0
for letter in contents:
    if letter == 'e':
        count += 1

print(count)