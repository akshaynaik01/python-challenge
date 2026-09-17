# Challenge 18 - Find the Largest Word

sentence = input("Enter a sentence: ")

words = sentence.split()
largest = ""

for word in words:
    if len(word) > len(largest):
        largest = word

print("Largest word:", largest)
