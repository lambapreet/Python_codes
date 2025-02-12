def two_sum(numbers, target):
    # Create a dictionary to store the numbers and their indices
    num_to_index = {}
    
    # Iterate through the list of numbers
    for index, number in enumerate(numbers):
        # Calculate the complement that would add up to the target
        complement = target - number
        
        # Check if the complement is already in the dictionary
        if complement in num_to_index:
            # If found, return the indices of the two numbers
            return [num_to_index[complement], index]
        
        # Otherwise, add the number and its index to the dictionary
        num_to_index[number] = index
    
    # If no solution is found, return None or an appropriate message
    return None

# Example usage
numbers_list = [2, 7, 11, 15]
target_value = 9
result = two_sum(numbers_list, target_value)

if result:
    print(f'The indices of the two numbers that add up to {target_value} are: {result}')
else:
    print('No two numbers add up to the target.')