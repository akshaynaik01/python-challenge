# Challenge 12 - Find the Second Largest Number

numbers = [10, 25, 7, 45, 32, 45]

largest = float("-inf")
second_largest = float("-inf")

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest:", second_largest)
