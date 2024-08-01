def odd_index_sum(numbers):
    total = 0
    index = 1
    while index < len(numbers):
        total += numbers[index]
        index += 2
    return total