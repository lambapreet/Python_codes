# Print the Fibonacci sequence up to n terms.

def fibonacci_iterative(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Get user input
n_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
if n_terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci sequence up to {n_terms} terms: {fibonacci_iterative(n_terms)}")