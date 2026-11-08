# Challenge 52 - Find the Intersection of Two Lists

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

intersection = []

for num in list1:
    if num in list2 and num not in intersection:
        intersection.append(num)

print("Common elements:", intersection)
