# Challenge 26 - Find the Largest and Smallest Number

numbers = [25, 10, 45, 5, 78, 32]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)
