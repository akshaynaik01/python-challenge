# Challenge 43 - Check a Disarium Number

num = int(input("Enter a number: "))

original = num
total = 0
digits = str(num)

for i in range(len(digits)):
    total += int(digits[i]) ** (i + 1)

if total == original:
    print("Disarium number")
else:
    print("Not a Disarium number")
