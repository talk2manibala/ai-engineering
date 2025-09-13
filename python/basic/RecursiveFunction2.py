# Factorial program using recursive function

def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:
        return n * factorial(n - 1)   # recursive call

# Taking input from user
num = int(input("Enter a number: "))

# Calculating factorial and printing
print(f"The factorial of {num} is: {factorial(num)}")