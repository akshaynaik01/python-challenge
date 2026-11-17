# Challenge 56 - Check Whether Two Strings Are Rotations

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2) and str2 in (str1 + str1):
    print("Strings are rotations")
else:
    print("Strings are not rotations")
