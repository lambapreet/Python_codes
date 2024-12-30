def prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    if n % 2 == 0:  # Check divisibility by 2
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

number = 29  # Correct variable spelling
if prime(number):
    print(f"{number} is a prime number.")  # Use print to display the message
else:
    print(f"{number} is not a prime number.")
