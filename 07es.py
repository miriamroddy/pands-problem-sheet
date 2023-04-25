## Write a program that reads in a text file and outputs the number of e's it contains. 
## Think about what is being asked here, document any assumptions you are making.
## The program should take the filename from an argument on the command line.

## We start by importing the sys module

import sys

## The code uses sys.argv the read the argument and pass it to the program- we know we need two arguments (the name of the program and the filename), so we use an if statement here.
## If the number of arguments is less than two, the program prints a message to the console advising about how to format the query correctly, and exits.   

if len(sys.argv) != 2:
    print("Please format your query as following:  python 07es.py <filename>")
    sys.exit(1)

## We use sys.argv[1] to retrieve the second element of the sys.argv list, which is assumed to be the filename input by the user. The code assigns this filename to the variable
## filename.

filename = sys.argv[1]

## We use the open function (with mode r for reading) to read the content of the file. We neeed to use a with statement to ensure that the file is properly closed after Python is finished with it. 

with open(filename, "r") as file:

## Once the file is opened, the program iterates over each line of the files using a for loop. For every line, the code counts how many times the characters 'e' and 'E' appear 
## in the line using the count() method of the string object. It then adds the count of each line to a running total count. When the loop finishes, what is stored in count is the total
## number of occurances of both e and E in the file.

    count = 0
    for line in file:
        count += line.count('e') + line.count('E')
        
 ## we use an f-string to print the number of occurances to the console.

print(f"The file {filename} contains {count} e's.")
