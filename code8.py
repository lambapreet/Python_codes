# Generate a multiplication table

# Function to generate multiplication table
def multiplication_table(n, limit=10):
    print(f"Multiplication Table for {n}:")
    for i in range(1, limit + 1):
        print(f"{n} x {i} = {n * i}")

# Get user input
number = int(input("Enter a number to generate its multiplication table: "))
table_limit = int(input("Enter the limit for the multiplication table (default is 10): ") or 10)

# Generate the multiplication table
multiplication_table(number, table_limit)