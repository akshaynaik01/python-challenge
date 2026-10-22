# Challenge 42 - Check an Evil Number

num = int(input("Enter a number: "))

binary = bin(num)[2:]
count = binary.count('1')

print("Binary:", binary)

if count % 2 == 0:
    print("Evil number")
else:
    print("Not an evil number")
