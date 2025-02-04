'''
def is_palidrome(n):
    n = n.replace(" ","").lower()
    
    return n == n[::-1]


string = "racecar"
if is_palidrome(string):
    print(f"{string} is palidrome")
else:
    print(f"{string} is not palidrome")

'''

def is_largest(numbers):
    
    if not numbers:
        return None
    
    largest = numbers[0]
    
    for number in numbers:
        if number > largest:
            largest = number
    return largest


numbers_list = [3, 5, 1, 8, 2]
largest_number = is_largest(numbers_list)
print(f'The largest number in the list is: {largest_number}')    
    