# Challenge 55 - Find the Sum of Digits Until Single Digit

num = int(input("Enter a number: "))

while num >= 10:
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    num = total

print("Single digit sum:", num)
