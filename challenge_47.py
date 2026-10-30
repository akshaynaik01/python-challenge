# Challenge 47 - Check a Fascinating Number

num = int(input("Enter a number: "))

result = str(num) + str(num * 2) + str(num * 3)

if all(str(i) in result for i in range(1, 10)) and len(result) == 9:
    print("Fascinating number")
else:
    print("Not a fascinating number")
