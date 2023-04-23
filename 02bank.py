## Week 2 assignment. Write a program called bank.py . The program should: 
## 1. Prompt the user and read in two money amounts (in cent). 2. Add the two amounts 3. Print out 
## the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 

# The user is prompted to input the first amount in cents.  The int() function is used to convert the user's input from a string 
# to an integer, so that it can be used in calculations.

amount1 = int(input('Enter the first amount (in cent): '))

# User is prompted to input the second amount in cents.

amount2 = int(input('Enter the second amount (in cent): '))

## The two amounts are then added together using the + operator, and the result is stored in the total_amount variable.

total_amount = amount1 + amount2

# To convert the cents to euros, we divide by 100 and then use the modulo operator (%). 
# If python is playing ball, the result is stored in the euros and cents variables.

euros = total_amount // 100
cents = total_amount % 100

## The string to be printed starts with the text: "The total amount is €", followed by a set of empty curly brackets. 
## These work as placeholders where the values of the euros and cents variables will be inserted in the final string.

print(f"The total amount is €{euros}.{cents}")
