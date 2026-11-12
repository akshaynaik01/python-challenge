# Challenge 54 - Find the Longest Palindrome Word

sentence = input("Enter a sentence: ")

words = sentence.split()
longest = ""

for word in words:
    if word.lower() == word.lower()[::-1]:
        if len(word) > len(longest):
            longest = word

if longest:
    print("Longest palindrome word:", longest)
else:
    print("No palindrome word found")
