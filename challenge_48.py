# Challenge 48 - Check an Alphabet or Digit

char = input("Enter a character: ")

if char.isalpha():
    print("Alphabet")
elif char.isdigit():
    print("Digit")
else:
    print("Special character")
