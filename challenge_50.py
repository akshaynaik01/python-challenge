# Challenge 50 - Check a Perfect Square

num = int(input("Enter a number: "))

is_square = False

if num >= 0:
    for i in range(num + 1):
        if i * i == num:
            is_square = True
            break

if is_square:
    print("Perfect square")
else:
    print("Not a perfect square")
