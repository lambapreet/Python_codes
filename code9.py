# Find the factorial of a number

def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Get user input
number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is: {factorial_iterative(number)}")