# Challenge 58 - Check Valid Parentheses

text = input("Enter parentheses: ")

stack = []
pairs = {')': '(', '}': '{', ']': '['}

for char in text:
    if char in "({[":
        stack.append(char)

    elif char in ")}]":
        if not stack or stack[-1] != pairs[char]:
            print("Invalid parentheses")
            break
        stack.pop()
else:
    if not stack:
        print("Valid parentheses")
    else:
        print("Invalid parentheses")
