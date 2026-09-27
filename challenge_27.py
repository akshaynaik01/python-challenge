# Challenge 27 - Find the Second Smallest Number

numbers = [25, 10, 45, 5, 78, 32]

smallest = float("inf")
second_smallest = float("inf")

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Second smallest:", second_smallest)
