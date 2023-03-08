## Write a python program called accounts.py that reads in a 10 character account number and outputs the account number
# with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# add extra bit with account numbs of differing lengths

accountnumber = str(input("Please enter your account number:"))
appendedtext = str("XXXXXX")
accountwithX= (appendedtext+accountnumber[6:10])

print (accountwithX)