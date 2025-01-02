# Check if a number is a palindrome.
def palidrome(n):
    stn_n = str(n)
    return stn_n == stn_n[::-1]
 
name = 121

if palidrome(name):
    print(f"{name} is palidrome")
else:
    print(f"{name} is not palidrome")