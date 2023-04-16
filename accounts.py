## Write a python program called accounts.py that reads in a 10 character account number and outputs the account number
# with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# add extra bit with account numbs of differing lengths

## The user is prompted to enter their account number - the input is stored as a string in the accountnumber variable:

accountnumber = str(input("Please enter your account number:"))

## We now create a string variable called xs - this contains the text "XXXXXX".

xs = str("XXXXXX")

## We now create a new variable accountwithX by concatenating appendedtext (i.e. the six XXXXXXs) with a portion/slice of
## the accountnumber variable. This slice accountnumber[6:10] takes characters 6-9 
## from the accountnumber variable, i.e. the last four digits of the account number.

maskedaccountnumber= (xs+accountnumber[6:10])

# final result (the contents of variable maskedaccountnumber) is printed to the console:

print (maskedaccountnumber)