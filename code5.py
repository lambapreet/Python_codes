# Check if a number is positive, negative, or zero.

x = int(input("enter the number: "))

if x > 0:
    print(f"{x} is positive")
elif x == 0:
    print(f"{x} is zero")
else:
    print(f"{x} is negative")