## Write a program that reads in a text file and outputs the number of e's it contains. 
## Think about what is being asked here, document any assumptions you are making.
## The program should take the filename from an argument on the command line.




import sys

if len(sys.argv) != 2:
    print("Usage: python count_e.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as file:
    count = 0
    for line in file:
        count += line.count('e') + line.count('E')

print(f"The file {filename} contains {count} e's.")
