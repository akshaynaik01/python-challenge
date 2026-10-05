# Challenge 32 - Find the Most Frequent Character

text = input("Enter a string: ")

frequency = {}

for char in text:
    if char != " ":
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

most_frequent = ""
highest = 0

for char, count in frequency.items():
    if count > highest:
        highest = count
        most_frequent = char

print("Most frequent character:", most_frequent)
print("Frequency:", highest)
