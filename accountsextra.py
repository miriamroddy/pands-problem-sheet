##  The user input is stored in var account_number. We explicitly state that the account number can be up to 34 characters -
## in practice, the code can actually cope with longer numbers because computers are smart.  Humans are less smart so we will
## tell them the account number is no longer than 34 characters so they don't submit any old text. In later weeks, we would use an if 
## statement here if they input something longer than 34 characters, but this is Week 3 so we just prompt them like this.

account_number = input("Enter your account number (up to 34 characters): ")

## The program uses the slice function to extract the last 4 digits of the account number, and stores them in a variable called last_4_digits.

last_4_digits = account_number[-4:]

## python calculates the num of Xs required by subtracting 4 (the number of last digits to be shown) from the length of the account number. Even though SEPA accounts can be no longer than 34
## characters, this can actually cope with larger numbers.This result is then stored in var num_of_xs.

num_of_xs = len(account_number) - 4

## The program creates a string called num_of_xs Xs and stores it in a variable called xs. num_of_xs. 
## This will output how many Xs need to go before the last four digits of the account number. 

xs = "X" * num_of_xs

## We now concatenate the xs string and the last_4_digits string to create a masked account number , which we store in masked_account_number:

masked_account_number = xs + last_4_digits

## Finally, we print the masked account number to the console:

print("Your masked account number is:", masked_account_number)