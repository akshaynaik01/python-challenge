# Challenge 53 - Find the Missing Elements in a List

numbers = [1, 2, 4, 6, 7, 9]

missing = []

for i in range(1, 10):
    if i not in numbers:
        missing.append(i)

print("Missing numbers:", missing)
