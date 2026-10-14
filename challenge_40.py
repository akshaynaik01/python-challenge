# Challenge 40 - Check Twin Prime Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

if is_prime(a) and is_prime(b) and abs(a - b) == 2:
    print("Twin prime numbers")
else:
    print("Not twin prime numbers")
