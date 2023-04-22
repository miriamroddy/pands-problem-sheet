##  The user input is stored in the account_number variable. We explicitly state that the account number can be up to 34 characters.
##  In practice, the code can actually cope with longer numbers. I chose to go with 34 characters because this is the maximum length of SEPA account numbers. 
## 

account_number = input("Enter your account number (up to 34 characters): ")

## The program uses the slice function to extract the last 4 digits of the account number, and stores them in a variable called last_4_digits.

last_4_digits = account_number[-4:]

## Python calculates the number of Xs required by subtracting 4 (the number of last digits to be shown) from the length of the account number. Even though SEPA accounts can be no longer
#  than 34 characters, this can actually cope with larger numbers.This result is then stored in the num_of_xs variable.

number_of_xs = len(account_number) - 4
hellh
## The program creates a string called number_of_xs and stores it in a variable called xs. number_of_xs. 
## This will output how many Xs need to go before the last four digits of the account number. 

XString = "X" * number_of_xs

## We now concatenate the xs string and the last_4_digits string to create a masked account number , which we store in masked_account_number:

masked_account_number = XString + last_4_digits

## Finally, we print the masked account number to the console:

print("Your account number is:", masked_account_number)
