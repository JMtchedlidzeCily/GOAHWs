def digitize(n):
    str_n = str(n)
    reversed_digits = []
    for i in range(len(str_n) - 1, -1, -1):
        reversed_digits.append(int(str_n[i]))
    return reversed_digits
