# Challenge 13 - Remove Duplicates from a List

numbers = [10, 20, 10, 30, 20, 40, 30]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("After removing duplicates:", unique)
