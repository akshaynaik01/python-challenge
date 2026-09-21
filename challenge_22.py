# Challenge 22 - Reverse Words in a Sentence

sentence = input("Enter a sentence: ")

words = sentence.split()

reversed_words = []

for i in range(len(words) - 1, -1, -1):
    reversed_words.append(words[i])

print("Reversed sentence:", " ".join(reversed_words))
