def sqrt(n):
    """
    This function takes a positive floating-point number as input and outputs an approximation of its square root 
    using the Newton-Raphson method.
    """
    if n < 0:
        n = -n
        print("Note: The input number was negative and has been converted to a positive number.")

    x = n
    
    tolerance = 0.000001
    
    while abs(x**2 - n) > tolerance:
        
        x = (x + n/x) / 2

    return round(x, 3)


user_input = float(input("Enter a positive floating-point number: "))

approx_sqrt = sqrt(user_input)

print("The approximation of the square root of", user_input, "is:", approx_sqrt)
