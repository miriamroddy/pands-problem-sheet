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

    Commit and push a file to the problem sheet called helloworld.py

This is a simple Python script that uses the print() function in Python to output text to the console, so when we run this program, it will output the text "Hello, World!" to the console. Anything with a # symbol is a comment - it's not executed by the program but provides commentary to the code.

<p>Usage</p>

1. Clone the repository to your local machine.
2. Navigate to the directory where the hello_world.py script is located.
3. Open a terminal window and run the following command: python hello_world.py
4. The message "Hello, world!" should be printed to the console.

As this was mostly just an exercise in getting the environment set up, I only had to reference the [course notes](https://vlegalwaymayo.atu.ie/course/view.php?id=6208) and some information on [getting started with git](https://www.git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F).

- - - -

 # ***Bank***
 
	Write a program called bank.py . The program should:

	1. Prompt the user and read in two money amounts (in cent).
	2. Add the two amounts
	3. Print out the answer in a human readable format with a euro sign and 
	decimal point between the euro and cent of the amount 
  
  
  Commentary about specific code used is provided within the program.
  
 The task asks that the answer should feature a euro sign and decimal point between the euro and cent of the amount. This was something that took a bit of research but was ultimately answered by a post on [stack overflow](https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python). 
 There are several ways of representing a euro symbol in python. I could choose between direct input, the unicode glyph number, glyph name or Windows 1252 codepage. Direct input seemed to be the most straightforward for someone new to coding so I went with this.

Initially I used a print() statement using the .format() method:

``` 
[print('The total amount is €{}.{}'.format(euros, cents))]
``` 

A downside of using the .format() method is that it can be a bit verbose, so I simplified it by using an [f-string](https://www.datacamp.com/tutorial/f-string-formatting-in-python).



--------
  # ***Accounts***  
   
	Write a python program called accounts.py that reads in a 10 character account number and outputs the account number 
	with only the last 4 digits showing (and the first 6 digits replaced with Xs). Extra: Modify the program to deal with account numbers of any length 
	(yes that is a vague requirement; comment your assumptions).
	
This code demonstrates a simple way to obscure part of an account number by replacing it with "XXXXXX". This technique can be useful when sensitive information needs to be inputted, but the output should be obscured for security reasons. 

When writing this code, resources used were: https://www.w3schools.com/python/python_strings_slicing.asp
https://www.reddit.com/r/Python/comments/shrw4q/a_comprehensive_guide_to_slicing_in_python/

The extra task this week asked that we make a modification to our program to deal with account numbers of any length. This tasks was purposefully vague so that we were to examine what assumptions we would use in the real world. We're in the EU so I am going to assume that the longest number we're going to be using is 34 digits. The limit for a SEPA account is 34 digits - they are typically alphanumeric, which shouldn't be an issue since the input is treated as a string rather than an int or a float.


----

  # ***Collatz***

    Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values 
	of the following calculation. At each step calculate the next value by taking the current value and, if it is even,
	divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

If statements: https://www.w3schools.com/python/python_conditions.asp
While Loops: https://www.w3schools.com/python/python_while_loops.asp
https://imgs.xkcd.com/comics/collatz_conjecture.png

Initially my code just outputted the text on one line. A bit of googling gave me some infomation about the End parameter, that I could use to make the outpute tidier by having each reasult on a new line: https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
https://www.w3schools.com/python/ref_func_print.asp

----

  # ***Weekend***

    Write a program that outputs whether or not today is a weekday. The program should be called weekday.py.
	You will need to search the web to find how you work out what day it is.
	
https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python

- - - -

  # ***SquareRoot***

    Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
	You should create a function called <tt>sqrt</tt> that does this.
	I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
	This is to demonstrate that you can research and code a process (If you really needed the square root you would 
	use one of the above methods).I suggest that you look at the newton method at estimating square roots.
	This is a more difficult task than some of the others, but will be marked equally, 
	so only do as much work on this as you feel comfortable.

- - - -
  # ***NumberofEs***
  
    Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here,
	document any assumptions you are making.The program should take the filename from an argument on the command line
    
- - - -
  # ***PlotTask***
    
    Write a program called plottask.py that displays:

	a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
	and a plot of the function  h(x)=x3 in the range [0, 10], 
	on the one set of axes. Some marks will be given for making the plot look nice (legend etc).
    
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
Beatty, A. (2023). Programming and Scripting [Online Higher Diploma Program]. Coursera. https://vlegalwaymayo.atu.ie/course/view.php?id=6208