# Week 4 Task. Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values 
## of the following calculation. At each step calculate the next value by taking the current value and, if it is even,
## divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

## We ask the user to input a positive integer, which is stored in the number variable:

number = int(input("Enter a positive integer: "))

## We then use a while loop to perform a sequence of calculations 
## on the inputted number until it is equal to 1. So, while the variable number is not equal to 1, we perform a sequence of calculations on it.

while number != 1:

## While the number is NOT equal to 1, the current value of the number is printed to the console. Each time the while loop iterates, the current value of the number is
# # printed to the console, with a space character separating the numbers (we call this variable end).

    print(number, end=" ")

## We used an if statement to check whether the number is odd or even - we use the modulo operator to do this. If the number is even, we divide by 2. 

    if number % 2 == 0:
        number = number // 2

## If the number is odd, we multiply it by 3 and it's then added to 1.

    else:
        number = number * 3 + 1
        
## Finally we print the sequence to the console
print(number)
