# Challenge 29 - Decimal to Binary

num = int(input("Enter a decimal number: "))

binary = ""

if num == 0:
    binary = "0"
else:
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num //= 2

print("Binary:", binary)
