"""
Challenge 3: Fibonacci Sequence

Write a program that generates the Fibonacci sequence up to n terms.
The Fibonacci sequence is a series of numbers where each number is the sum
of the two preceding ones, usually starting with 0 and 1.

Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
"""

def fibonacci(n):
    """
    Generate the Fibonacci sequence up to n terms.
    
    Args:
        n: Number of Fibonacci numbers to generate
    
    Returns:
        list: A list containing the first n Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_num = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_num)
    
    return fib_sequence[:n]

def fibonacci_recursive(n):
    """
    Generate the nth Fibonacci number using recursion.
    
    Args:
        n: The position in the Fibonacci sequence
    
    Returns:
        int: The nth Fibonacci number
    """
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test cases
if __name__ == "__main__":
    print("Fibonacci sequence (first 10 terms):")
    result = fibonacci(10)
    print(result)
    
    print("\nFibonacci sequence (first 15 terms):")
    result = fibonacci(15)
    print(result)
    
    print("\nUsing recursive approach (first 12 Fibonacci numbers):")
    for i in range(12):
        print(f"F({i}) = {fibonacci_recursive(i)}")
