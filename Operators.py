# Get user input
x = int(input("Enter the value-1: "))
y = int(input("Enter the value-2: "))

# Initialize variables for results
add = None
sub = None
mul = None
div = None

# Perform operations based on the conditions
if x < y:
    add = x + y
    print(f"Addition of {x} and {y} is: {add}")
elif x > y:
    sub = x - y
    print(f"Subtraction of {y} from {x} is: {sub}")
elif x == y:
    mul = x * y
    print(f"Multiplication of {x} and {y} is: {mul}")

# Check for division only if y is not zero
if y != 0:
    div = x // y
    print(f"Division of {x} by {y} is: {div}")
else:
    print("Division by zero is not allowed.")