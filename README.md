# Pands Problem Sheet 2023


In order that this be applicable to a real-world setting, comments within each program will explain the code used and to outline my thought processes, assumptions etc. so that the code is understandable. The purpose of variables, function etc. will be explained.

The commentary within the README is more focused on explaining each program in a more holistic manner. In a real-world setting, this is to help a user learn more about a project as a whole. 



## Table of Contents
* [Weekly Tasks 1-10 ](#weekly-tasks)
    * [Week 01 - Hello World](#helloWorld)
    * [Week 02 - Bank](#Bank)
    * [Week 03 - Accounts](#accounts)
    * [Week 04 - Collatz](#collatz)
    * [Week 05 - Weekend](#weekend)
    * [Week 06 - Square Root](#squareroot)
    * [Week 07 - NumberofEs](#numberofes)
	* [Week 08 - Plot Task](#plottask)
	
* [Technologies](#technologies)
* [References](#references)


Weekly Tasks
======
# ***HelloWorld***
### Task
    Commit and push a file to the problem sheet called helloworld.py
### Code Description
This is a simple Python script that uses the print() function in Python to output text to the console, so when we run this program, it will output the text "Hello, World!" to the console. Anything with a # symbol is a comment - it's not executed by the program but provides commentary to the code.

<p>Usage</p>

1. Clone the repository to your local machine.
2. Navigate to the directory where the hello_world.py script is located.
3. Open a terminal window and run the following command: python hello_world.py
4. The message "Hello, world!" should be printed to the console.

As this was mostly just an exercise in getting the environment set up, I only had to reference the [course notes](https://vlegalwaymayo.atu.ie/course/view.php?id=6208) and some information on [getting started with git](https://www.git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F).

- - - -

 # ***Bank***
 
 ### Task
	Write a program called bank.py . The program should:

	1. Prompt the user and read in two money amounts (in cent).
	2. Add the two amounts
	3. Print out the answer in a human readable format with a euro sign and 
	decimal point between the euro and cent of the amount 
  
  ### Code Description

The user is prompted to input the first amount in cents; the int() function is used to convert the user's input from a string 
to an integer, so that it can be used in calculations. The user is then prompted to input the second amount in cents.
The two amounts are added together using the + operator, and the result is stored in the total_amount variable.
To convert the cents to euros, we divide by 100 and then use the modulo operator (%). The result is stored in the euros and cents variables.
The string to be printed starts with the text: "The total amount is €", followed by a set of empty curly brackets. 
These brackets work as placeholders where the values of the euros and cents variables will be inserted in the final string.

 ### Challenges and Research

Initially I had used floating points in my calculations e.g. 
```
amount1 = float(input("Enter the first amount in euros: "))
amount2 = float(input("Enter the second amount in euros: "))
```
[Further reading](https://www.geeksforgeeks.org/floating-point-error-in-python/) made it clear that using floating-point numbers in financial calculations can lead to rounding errors and inaccuracies. It is generally recommended to use integer arithmetic when performing these calculations.

 The task asks that the answer should feature a euro sign and decimal point between the euro and cent of the amount. This was something that took some research but I got guidance from [this post on stack overflow](https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python). 
 I discovered that there are several ways of representing a euro symbol in python. I could choose between direct input, the unicode glyph number, glyph name or Windows 1252 codepage. Direct input seemed to be the most straightforward so I went with this.

Initially I had used a print() statement using the .format() method:

``` 
[print('The total amount is €{}.{}'.format(euros, cents))]
``` 

A downside of using the [.format() method](https://www.w3schools.com/python/ref_string_format.asp) is that it can be a bit verbose, so I simplified it by using an [f-string](https://www.datacamp.com/tutorial/f-string-formatting-in-python).



--------
  # ***Accounts***  
   ### Task
	Write a python program called accounts.py that reads in a 10 character account number and outputs the account number 
	with only the last 4 digits showing (and the first 6 digits replaced with Xs). Extra: Modify the program to deal with account 
	numbers of any length (yes that is a vague requirement; comment your assumptions).
	
### Code Description
Two implementations of this program are included, the first of which reads in a ten-digit account number and the second of which reads in an account number of any length.

**Ten-digit implementation:**
This code prompts the user to input their 10-digit account number and masks the first six digits while displaying the last four digits. This technique can be useful when sensitive information needs to be inputted, but the output should be obscured for security reasons. If the user enters an account number that is not 10 digits long, the program will display an error message and prompt the user to enter their account number again until a valid input is received - we use a while loop to do this. 

Inside the loop, we read in the account number inputted by the user using the input() function.We then check if the account number has exactly 10 digits using the len() function. If the account number has exactly 10 digits, we concatenate "XXXXXX" with the last 4 digits of the account number using string slicing and store the result in a variable called masked_account_number. We then exit the loop using the break statement since we have a valid account number. If the account number does not have exactly 10 digits, we print an error message using the print() function. If the account number does have 10 digits, we use the print() function to output the masked account number with the message "Your masked account number is:".

**Any-length implementation**
The second part of the task was purposefully vague, presumably so we would examine what assumptions we would use in the real world. We're in the EU so I am going to assume that the longest number we're going to be using is 34 digits, since [the limit for a SEPA account is 34 digits](https://www.iban.com/glossary) - they are typically alphanumeric, which shouldn't be an issue since the input is treated as a string rather than an int or a float.

In this version, we explicitly state that the account number can be up to 34 characters. Even though SEPA accounts can be no longer than 34 characters, this can actually cope with larger numbers - there functionally doesn't seem to be a need to limit the input to 34 digits in the code. This version also uses the slice function to extract the last 4 digits of the account number, and stores them in a variable called last_4_digits. Python calculates the number of Xs required by subtracting 4 (the number of last digits to be shown) from the length of the account number. . The result is then stored in the number_of_xs variable.  This will output how many Xs need to go before the last four digits of the account number. We now concatenate the Xsting variable and the last_4_digits string to create a masked account number. Finally, we print the masked account number to the console.

### Challenges and Research
It was necessary to read up on slicing [on w3schools](https://www.w3schools.com/python/python_strings_slicing.asp) and on [reddit/r/python](https://www.reddit.com/r/Python/comments/shrw4q/a_comprehensive_guide_to_slicing_in_python/).


  # ***Collatz***
### Task
    Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values 
	of the following calculation. At each step calculate the next value by taking the current value and, if it is even,
	divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

### Code Description
The Collatz Conjecture is an [infamous](https://imgs.xkcd.com/comics/collatz_conjecture.png) unsolved problem in mathematics, which posits that if you repeatedly apply a simple set of rules to a positive integer, you will eventually reach the number 1. This task involves demonstrating this problem using python.

We ask the user to input a positive integer, which is stored in the number variable.
We then use a while loop to perform a sequence of calculations on the inputted number until it is equal to 1. So, while the variable number is not equal to 1, we perform a sequence of calculations on it.
While the number is NOT equal to 1, the current value of the number is printed to the console. Each time the while loop iterates, the current value of the number is
printed to the console, with a space character separating the numbers (we call this variable end).
We used an if statement to check whether the number is odd or even - we use the modulo operator to do this. If the number is even, we divide by 2. 
If the number is odd, we multiply it by 3 and it's then added to 1.
Finally we print the sequence to the console.

### Challenges and Research
[If statements](https://www.w3schools.com/python/python_conditions.asp)
[While Loops](https://www.w3schools.com/python/python_while_loops.asp)


Initially my code just outputted the text on one line. A bit of googling gave me some infomation about the [end parameter]( https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/), that I could use to make the output tidier by [having each result on a new line](https://www.w3schools.com/python/ref_func_print.asp).


----

  # ***Weekend***
### Task
    Write a program that outputs whether or not today is a weekday. The program should be called weekday.py.
	You will need to search the web to find how you work out what day it is.

### Code Description
We start by importing the datetime module, which allows us to manipulate date and time object data.
We use the module to get the day of the week for the current date and time - this is then stored in the today variable. We do this by calling the weekday() 
method of the today object, which returns an integer representing the day of the week, with Monday being a 0 and Sunday being a 6.
We then create a list called weekdays, with each string in the list representing a weekday - Monday is 0 and Friday is 4.
We now use an if statement to check if the day of the week is less than 5. If the day of the week is less than 5, we know that it must be a weekday (because Monday's index is 0 and Thursday's is 4),so we output the "Yes, today is a weekday" message to the console. If the day of the week is 5 or 6, it must be a weekend (Saturday or Sunday), so we output the message "No, today is not a weekday."

### Challenges and References
We are using datetime module to get the current date and time. We then use the weekday() method of the datetime object to get the weekday as an integer, where Monday is 0 and Sunday is 6. If the integer is less than 5, then it's a weekday (Monday to Friday). 
[stack overflow](https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python)

- - - -

  # ***SquareRoot***

    Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
	You should create a function called <tt>sqrt</tt> that does this.
	I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
	This is to demonstrate that you can research and code a process (If you really needed the square root you would 
	use one of the above methods).I suggest that you look at the newton method at estimating square roots.
	This is a more difficult task than some of the others, but will be marked equally, 
	so only do as much work on this as you feel comfortable.

### Code Description
### Challenges and References
This involved researching the [Newton-Raphson method](https://towardsdatascience.com/develop-your-own-newton-raphson-algorithm-in-python-a20a5b68c7dd), not something for the mathematically uninclined. It is an iterative method for finding the roots of a function. It works by making an initial guess of the root, and then iteratively refining that guess by using the slope of the function at that point to estimate where the root might be. Or, in [layman's terms](https://www.reddit.com/r/explainlikeimfive/comments/mh83qk/eli5_why_does_the_newtonraphson_method_work/), it's a way of finding the root by making an educated guess, and then making better and better guesses until we get the right answer. In Python, this can be implemented using a loop that updates the guess at each iteration until the desired level of accuracy is achieved. 

There are different strategies for choosing the initial guess in numerical methods for approximating the square root, but I chose to go with n/2 as the initial guess. This is a sensible starting point for many numbers because the square root of a number is always going to be less than or equal to half of the number itself, and seemed like the most straightforward approach and appealed to my mathematically-averse nature.
- - - -
  # ***NumberofEs***
  
    Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here,
	document any assumptions you are making.The program should take the filename from an argument on the command line

### Code Description
### Challenges and References

 We are counting both lowercase 'e' and uppercase 'E' but it should be kept in mind that we're not considering any other variations of the letter 'e', such as accented characters.
- - - -
  # ***PlotTask***
    
    Write a program called plottask.py that displays:

	a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
	and a plot of the function  h(x)=x3 in the range [0, 10], 
	on the one set of axes. Some marks will be given for making the plot look nice (legend etc).

### Code Description

- - - -

Technologies
====

  List Technologies used


   
- - - -

References
====

PEP 8 -- Style Guide for Python Code: https://www.python.org/dev/peps/pep-0008/
Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
Python Style Guide by Guido van Rossum: https://legacy.python.org/dev/peps/pep-0008/#introduction

Matthes, E. (2015). Python Crash Course: A Hands-On, Project-Based Introduction to Programming. No Starch Press.
Beatty, A. (2023). Programming and Scripting [Online Higher Diploma Program]. https://vlegalwaymayo.atu.ie/course/view.php?id=6208
