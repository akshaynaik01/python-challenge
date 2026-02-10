"""
Challenge 1: FizzBuzz Problem

Write a program that prints numbers from 1 to 100.
But for multiples of 3, print "Fizz" instead of the number,
and for multiples of 5, print "Buzz".
For numbers that are multiples of both 3 and 5, print "FizzBuzz".
"""

def fizzbuzz(n):
    """
    Solves the FizzBuzz challenge up to n.
    
    Args:
        n: The upper limit (inclusive)
    """
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Run the challenge
if __name__ == "__main__":
    fizzbuzz(100)
