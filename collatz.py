#the user is asked to enter a positive integer - it's stored it in the variable num
#The program then enters a loop that continues as long as num is not equal to 1. This loop will iterate through the successive values of the Collatz sequence.
#Inside the loop, the program prints the current value of num on the same line.
#The program then checks if num is even or odd. If it is even, the program divides it by 2 using integer division (//). If it is odd, the program multiplies it by 3 and adds 1.
#After each iteration of the loop, the program checks if num is equal to 1. If it is, the loop ends and the final value of num is printed.


num = int(input("Enter a positive integer: "))
while num != 1:
    print(num, end=" ")
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1
print(num)