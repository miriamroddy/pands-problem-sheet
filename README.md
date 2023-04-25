# Pands Problem Sheet 2023


In order that this be applicable to a real-world setting, comments within each program will explain the code used. I'll outline more about my thought processes, assumptions etc. here. References will be cited in the text and any extra texts/resources that helped with the tasks in general will be listed at the end.


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
This code prompts the user to input their 10-digit account number and masks the first six digits while displaying the last four digits. If the user enters an account number that is not 10-digits long, the program will display an error message and prompt the user to enter their account number again until a valid input is received - we use a [while loop](https://www.w3schools.com/python/python_while_loops.asp) to do this. 

Inside the loop, we read in the account number inputted by the user using the input() function. We then check if the account number has exactly 10 digits using the len() function. If the account number has exactly 10 digits, we concatenate "XXXXXX" with the last 4 digits of the account number using string slicing. We exit the loop using the [break statement](https://www.geeksforgeeks.org/python-break-statement/). If the account number does not have exactly 10 digits, we print an error message using the print() function and if it does have 10 digits, we also use the print function to diaplay the masked account number.

**Any-length implementation**
We use a slice function to extract the last 4 digits of the account number. Even though SEPA accounts can be no longer than 34 characters, this code can cope with larger numbers - we don't really need to limit the input to 34 digits in the code. Python calculates the number of Xs required by subtracting four from the length of the account number. We concatenate the Xstring variable and the last_4_digits string to create a masked account number. Finally, we print the masked account number to the console.

### Challenges and Research
The second part of the task was purposefully vague, presumably so we would examine what assumptions we would use in the real world. We're in the EU so I am going to assume that the longest number we're going to be using is 34 digits, since [the limit for a SEPA account is 34 digits](https://www.centralbank.ie/consumer-hub/explainers/what-is-iban-discrimination-and-what-can-i-do-about-it) - they are typically alphanumeric, which shouldn't be an issue since the input is treated as a string rather than an int or a float.


This was a good opportunity to get some practice at [string manipulation](https://www.pythonforbeginners.com/basics/string-manipulation-in-python). For both iterations of the task, I read up on using 
 slicing strings on [w3schools](https://www.w3schools.com/python/python_strings_slicing.asp) and on [reddit/r/python](https://www.reddit.com/r/Python/comments/shrw4q/a_comprehensive_guide_to_slicing_in_python/). This was also a nice chance to learn about and to play around with the [len function](https://www.w3schools.com/python/python_strings_slicing.asp). 

=
I came back to this task in later weeks to add a [while loop](https://www.freecodecamp.org/news/while-loops-in-python-while-true-loop-statement-example/#:~:text=A%20while%20loop%20will%20always,while%20the%20condition%20remains%20True%20.) - I hadn't included this initially as we only encountered them in Week 4. Including the loop ensures that we prompt the user until they input 10 digits.


  # ***Collatz***
### Task
    Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values 
	of the following calculation. At each step calculate the next value by taking the current value and, if it is even,
	divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.


### Code Description

We ask the user to input a positive integer, and then use a while loop to perform a sequence of calculations on the number until it is equal to 1. Each time the while loop iterates, the current value of the number is printed to the console, with a space character separating the numbers.
We used an if statement to check whether the number is odd or even, using the modulo operator to do this. If the number is even, we divide by 2. If the number is odd, we multiply it by 3 and it's then added to 1. Finally we print the sequence to the console, formatted so it's all in one line.

### Challenges and Research

The Collatz Conjecture is an [slightly head-melting](https://imgs.xkcd.com/comics/collatz_conjecture.png) unsolved problem in mathematics, which posits that if you repeatedly apply a simple set of rules to a positive integer, you will eventually reach the number 1. The first challenge here is to understand the problem before implementing it in code. After learning about some of the theory behind the conjecture from [the Veritasium channel](https://www.youtube.com/watch?v=094y1Z2wpJg&t=1s&ab_channel=Veritasium), I then researched how a sequence of calculations could best be done in Python on [medium](https://medium.com/the-art-of-python/the-collatz-sequence-in-python-eb7e1f1b4f9e). [Geeksforgeeks](https://www.geeksforgeeks.org/program-to-print-collatz-sequence/) in particular explained this nice and simply.

This was a good chance to get to grips with [if statements](https://www.w3schools.com/python/python_conditions.asp) and [While Loops](https://www.w3schools.com/python/python_while_loops.asp). We need the while loop to iterate through the sequence of numbers and the if statement to check whether the number is odd or even. Initially my code just outputted the text on one line. A bit of googling gave me some infomation about the [end parameter]( https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/), that I could use to make the output tidier by [having each result on a new line](https://www.w3schools.com/python/ref_func_print.asp).


----

  # ***Weekend***
### Task
    Write a program that outputs whether or not today is a weekday. The program should be called weekday.py.
	You will need to search the web to find how you work out what day it is.

### Code Description
We start by importing the [datetime module](https://docs.python.org/3/library/datetime.html), which allows us to manipulate date and time object data.
We use the module to get the day of the week for the system's current date and time. We call the [weekday() 
method](https://www.geeksforgeeks.org/weekday-function-of-datetime-date-class-in-python/) of the today object, which returns an integer representing the day of the week, with Monday being a 0 and Sunday being a 6.
We then create a tuple called weekdays, with each string in the tuple representing a weekday - Monday is 0 and Friday is 4.
We use an if statement to check if the day of the week is less than 5. If the day of the week is less than 5, we know that it must be a weekday (because Monday's index is 0 and Thursday's is 4). We then output the relevant message to the console, depending on whether today is a weekday or not.

### Challenges and Research
This task initially seemed a lot trickier than it turned out to be, highlighting how useful it is to know what modules are available in Python. [Stack overflow](https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python) ultimately clued me in on the datetime module. I learned how to create a datetime object using the [.datetime.datetime() constructor](https://docs.python.org/3/library/datetime.html). It was a nice introduction to using lists, but I changed it to [a tuple](https://www.w3schools.com/python/python_tuples.asp), since the days of the week are unlikely to change. This won't really affect the functionality but it seemed to be the more appropriate choice.

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
We start the program by defining the sqrt function. This involves taking a user inputted argument, assumed to be a floating-point number. If the number is positive, it starts with an initial guess of half the input value.
The program then sets a level of error for the acceptable difference between the current and previous guesses - we are going with .0001. We use a while loop to iterate until the difference between the current and previous guesses 
is within the level of error we deem acceptable. We use the abs function to ensure that the difference between the two guesses is always a positive number.
We use the round function so that we don't get too many decimal places in the output. A while loop is used that keeps going until the user inputs a positive-floating point number. 
When this happens, the loop terminates using the break statement. We can then use the sqrt function, call it on the user input (num) and print the result.

### Challenges and Research
This involved researching the [Newton-Raphson method](https://towardsdatascience.com/develop-your-own-newton-raphson-algorithm-in-python-a20a5b68c7dd), not something for the mathematically uninclined. It is an iterative method for finding the roots of a function. It works by making an initial guess of the root, and then iteratively refining that guess by using the slope of the function at that point to estimate where the root might be. Or, in [layman's terms](https://www.reddit.com/r/explainlikeimfive/comments/mh83qk/eli5_why_does_the_newtonraphson_method_work/), it's a way of finding the root by making an educated guess, and then making better and better guesses until we get the right answer. In Python, this can be implemented using a loop that updates the guess at each iteration until the desired level of accuracy is achieved. 

There are different strategies for choosing the initial guess in numerical methods for approximating the square root, but I chose to go with n/2 as the initial guess. This is a sensible starting point for many numbers because the square root of a number is always going to be less than or equal to half of the number itself, and seemed like the most straightforward approach. A [tolerance level](https://towardsdatascience.com/develop-your-own-newton-raphson-algorithm-in-python-a20a5b68c7dd) of .0001 was selected because it is generally considered to be a good balance between accuracy and computational efficiency for estimating square roots using the Newton-Raphson method. I also had to incorporate a method for handling negative input, since the Newton-Raphson method is not defined for negative input numbers. A while loop did the job here.

I preffered an output that rounded the reult to two decimal places so this needed a bit of research - I used the [round function](https://www.w3schools.com/python/ref_func_round.asp) which is nice and straightforward.
- - - -
  # ***NumberofEs***
  
    Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here,
	document any assumptions you are making.The program should take the filename from an argument on the command line

### Code Description
The first thing we do is import the sys module. The code uses sys.argv to read the argument and pass it to the program - we know we need two arguments (the name of the program and the filename), so we use an if statement here. If the number of arguments is less than two, the program prints a message to the console advising about how to format the query correctly, and exits.   
We use sys.argv[1] to retrieve the second element of the sys.argv list, which is assumed to be the filename input by the user. The code assigns this filename to the variable
filename. We use the open function (with mode r for reading) to read the content of the file. I found that we need to use a [with statement](https://www.youtube.com/watch?v=87DuQWjID_E) to ensure that the file is properly closed after Python is finished with it - this is an important way of avoiding errors. 

Once the file is opened, the program iterates over each line of the file using a for loop. For every line, the code counts how many times the characters 'e' and 'E' appear 
in the line using the [count() method](https://www.w3schools.com/python/ref_list_count.asp) of the string object. It then adds the count of each line to a running total count. When the loop finishes, what is stored in count is the total
number of occurances of both e and E in the file. We use an f-string to print the number of occurances to the console.

### Challenges and Research

A challenge here was to find a method of taking the filename from an argument on the command line. [Geeksforgeeks](https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/) was helpful here and I found that I could import the [sys module](https://docs.python.org/3/library/sys.html). A key assumption here is that we are reading English language texts, and we are interested in counting both lowercase 'e' and uppercase 'E'. We are not considering any other variations of the letter 'e', such as accented characters since an assumption is that the text is in English. If we were do so, we could import the [unicodedata](https://docs.python.org/3/library/unicodedata.html) module.
- - - -
  # ***PlotTask***
    
    Write a program called plottask.py that displays:

	a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
	and a plot of the function  h(x)=x3 in the range [0, 10], 
	on the one set of axes. Some marks will be given for making the plot look nice (legend etc).

### Code Description

We begin by importing the [numpy library](https://www.geeksforgeeks.org/python-numpy/) and give it the alias np [(for ease of reference)](https://www.reddit.com/r/learnpython/comments/eeqmlh/why_bother_with_import_numpy_as_np/) and do the same with the [matplotlib library](https://www.w3schools.com/python/matplotlib_pyplot.asp), giving it the alias plt. 
We then generate 1000 random values from a normal distribution with mean of 5 and SD of 2. The generated values are stored in the data variable - we want an array that contains 1000
random numbers with a mean of 5 and an SD of 2. Now that we have the 1000 values we want, we want to create a histogram of what we have stored in the data variable.  We have various arguments that we can play around with here - e.g. we can select the transparancy of the histogram bars, and we can create a neat legend.
We need to create a second array, called x, that contains a hundred evenly spaced values between 0 and 10 using the [numpy.linspace()](https://realpython.com/np-linspace-numpy/) method. The third argument specifies the number of values to generate in the sequence.
We calculate the function h(x) = x^3 for each value of x. Add labels to both axes. We want to give the graph a title and to include a legend with the [legend() argument](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html). Finally, we show the resulting graph

### Challenges and Research
The first thing to do is to understand the problem requirements: before starting the program, we need to make sure you have a clear understanding of what is required. Combining the plots required some playing around with the library - combining the histogram and function plot onto the same set of axes requires knowledge of how to create [multiple plots](https://www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html) on the same set of axes, and how to adjust the appearance of each plot (e.g. color, line style). 
- - - -


References
====

- PEP 8 -- Style Guide for Python Code - (https://www.python.org/dev/peps/pep-0008/)
- Google Python Style Guide (https://google.github.io/styleguide/pyguide.html)
- Python Style Guide by Guido van Rossum (https://legacy.python.org/dev/peps/pep-0008/#introduction)

- Matthes, E. (2015). Python Crash Course: A Hands-On, Project-Based Introduction to Programming. No Starch Press.
- Beatty, A. (2023). Programming and Scripting [Online Higher Diploma Program]. https://vlegalwaymayo.atu.ie/course/view.php?id=6208
