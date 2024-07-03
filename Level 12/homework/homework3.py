sum_excluding_500_to_600 = 0
for i in range(1, 1001):
    if 500 <= i < 600:
        continue
    sum_excluding_500_to_600 += i

print("The sum of numbers from 1 to 1000 excluding 500 to 600 is:", sum_excluding_500_to_600)
