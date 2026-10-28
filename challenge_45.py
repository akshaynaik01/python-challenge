# Challenge 45 - Check a Duck Number

num = input("Enter a number: ")

if num.isdigit() and num[0] != '0' and '0' in num:
    print("Duck number")
else:
    print("Not a Duck number")
