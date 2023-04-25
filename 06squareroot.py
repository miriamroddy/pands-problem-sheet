## Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
## You should create a function called <tt>sqrt</tt> that does this.

## We start by defining a function called sqrt. This involves takes an argument (num), assumed to be a floating-point number. This then results in an approximation of the square root of n using the
## Newton-Raphson method.

def sqrt(num):

## Now we start with the main part of the sqrt function. If the number is positive, it start with an initial guess of half the input value - see readme for reasoning.
        
        guess = num / 2

## Set a level of error for the acceptable difference between the current and previous guesses - we are going with .0001.
       
        tolerance = 0.0001

## We use a while loop to iterate until the difference between the current and previous guesses is within the level of error we deem acceptable. We use the abs function to ensure 
## that the difference between the two guesses is always a positive number.

        while abs(guess * guess - num) > tolerance:
            guess = guess - (guess * guess - num) / (2 * guess)
            
## We use the round function so that we don't get too many decimal places in the output.
        
        return round(guess, 2)

# This part of the code prompts the user to enter a positive floating-point number. We use a while loop that keeps going until the user inputs a positive-floating point number. 
# If num is greater than 0, the loop terminates using the break statement.

while True:
    num = float(input("Enter a positive floating-point number: "))
    if num > 0:
        break

# We now use our new sart function, call it on the user input (num) and print the result.
print("The square root of", num, "is approximately", sqrt(num))



