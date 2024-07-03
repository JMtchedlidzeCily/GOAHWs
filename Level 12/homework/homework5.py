num = 1

while num <= 10:
    print(f"Multiplication table of {num}:")
    multiplier = 1
    while multiplier <= 10:
        print(f"{num} x {multiplier} = {num * multiplier}")
        multiplier += 1
    num += 1
    print()
