# Find the largest and smallest numbers among three inputs.

x = int(input("Enter the value-1: "))
y = int(input("Enter the value-2: "))
z = int(input("Enter the value-3: "))

if x >= y and x >=z:
    print(f"X = {x} is greater")
elif y >= x and y >= z:
    print(f"Y = {y} is greater")
else:
    print(f"Z = {z} is greater")
    