# Given list
list1 = [2, 51, 11, 13, 51, 100]

# 1. Output every item from list with positive indexing.
for i in range(len(list1)):
    print(list1[i], end=' ')
print()

# 2. Output every item from list with negative indexing.
for i in range(-1, -len(list1)-1, -1):
    print(list1[i], end=' ')
print()

# 3. Replace the last element of a list with a new value.
list1[-1] = 999
print("List after replacing last element:", list1)

# 4. Replace the fifth element of a list with a new value.
if len(list1) >= 5:
    list1[4] = 777
    print("List after replacing fifth element:", list1)
else:
    print("List doesn't have a fifth element.")

# 5. Extract the last three elements of a list.
last_three = list1[-3:]
print("Last three elements:", last_three)

# 6. Extract the first three elements of a list.
first_three = list1[:3]
print("First three elements:", first_three)

# 7. Extract the middle two elements of a list. ([11, 13])
if len(list1) >= 4:
    middle_two = list1[2:4]
    print("Middle two elements:", middle_two)
else:
    print("List doesn't have enough elements for middle extraction.")

# 8. Extract random elements of a list with negative indexes.
random_elements = list1[-3:-1]  # Extracts elements from the third last to second last
print("Random elements with negative indexes:", random_elements)
