# 1.
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

i = 1
while i <= 50:
    if i % 2 != 0:
        print(i)
    i += 1

# 2.
for i in range(1, 21):
    print(i**2)

i = 100
while i >= 1:
    print(i)
    i -= 1

# 3.
for i in range(100, 0, -1):
    print(i)

i = 1
while i <= 10:
    print(i**3)
    i += 1

# 4.
# (Multiplication table of 5)
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# (Multiplication table of 7)
i = 1
while i <= 10:
    print(f"7 x {i} = {7 * i}")
    i += 1

# 5.
for i in range(1, 11):
    print(f"5 : {i} = {5 / i}")

i = 1
while i <= 10:
    print(f"7 : {i} = {7 / i}")
    i += 1


