## Write a python program called accounts.py that reads in a 10 character account number and outputs the account number
# with only the last 4 digits showing (and the first 6 digits replaced with Xs).

## This code prompts the user to input their 10-digit account number and masks the first six digits while displaying the last four digits.
## If the user enters an invalid account number that is not 10 digits long, the program will display an error message and prompt the user to
## enter their account number again until a valid input is received.

## We create an infinite while loop that will continue to prompt the user for input until a valid account number is entered.
while True:
    
## We prompt the user to enter their account number and store is in the account_number variable:
    account_number = input("Enter your 10-digit account number: ")
## We use an if statement to check if the length (using len) of the account number is equal to ten digits:
    if len(account_number) == 10:
## We create a new variable (masked_account_number) by concatenating the first six characters with XXXXX and the last four characters or the account_number variable:
        masked_account_number = "XXXXXX" + account_number[-4:]
## we use break to exit the loop when a valid account number has been entered
        break
## If the account number is not ten digits long, an error message is printed to the console:
    else:
        print("Error: account number must be 10 digits.")

# Lastly, we print out the masked account number to the user
print("Your masked account number is:", masked_account_number)
