#1.
def arithmetic_operations(a, b):
    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b if b != 0 else "undefined"
    }

#2.
def add_until_100(a, b):
    while a < 100:
        a += b
    return a

#3.
def is_even_or_odd(n):
    return "even" if n % 2 == 0 else "odd"

#4.
def find_largest(numbers):
    if not numbers:
        return None
    return max(numbers)

#5.
def sum_of_list(numbers):
    return sum(numbers)

#6.
def reverse_mixed_list(mixed_list):
    return mixed_list[::-1]

#7.
def find_longest_and_shortest(strings):
    if not strings:
        return None, None
    longest = max(strings, key=len)
    shortest = min(strings, key=len)
    return longest, shortest

#8.
def swap_case(s):
    return s.swapcase()

#9.
def count_consonants(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char.isalpha() and char not in vowels)

#10.
def is_even(n):
    return n % 2 == 0

#11.
def sum_even_index(numbers):
    return sum(numbers[i] for i in range(len(numbers)) if i % 2 == 0)

#12.
def check_even_or_odd(n):
    return "even" if n % 2 == 0 else "odd"

#13.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#14.
def capitalize_names(names):
    return [name.capitalize() for name in names]

#15.
def process_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num // 2)
        else:
            result.append(num * 2)
    return result

#16.
def reverse_upper(s):
    return s[::-1].upper()

#17.
def categorize_strings(strings):
    odd = []
    even = []
    for s in strings:
        if len(s) % 2 == 0:
            even.append(s.upper())
        else:
            odd.append(s.upper())
    print("Odd length strings:", odd)
    print("Even length strings:", even)

#18.
def process_string_list(strings):
    result = []
    for s in strings:
        if len(s) % 2 == 0:
            result.append(s.upper())
        else:
            result.append(s.capitalize())
    return result

#19.
def categorize_case(strings):
    result = []
    for s in strings:
        if s.isupper():
            result.append(s.lower())
        elif s.islower():
            result.append(s.upper())
    return result

#20.
def find_and_transform(s):
    index = s.find('a')
    if index == -1:
        return s
    return s.upper() if index % 2 == 0 else s.capitalize()

# Example usage
print(arithmetic_operations(10, 5))  #1
print(add_until_100(10, 20))  #2
print(is_even_or_odd(3))  #3
print(find_largest([1, 2, 3, 4, 5]))  #4
print(sum_of_list([1, 2, 3, 4, 5]))  #5
print(reverse_mixed_list(["hello", 123, "world", 456]))  #6
print(find_longest_and_shortest(["apple", "banana", "cherry"]))  #7
print(swap_case("Hello World"))  #8
print(count_consonants("hello world"))  #9
print(is_even(4))  #10
print(sum_even_index([1, 2, 3, 4, 5]))  #11
print(check_even_or_odd(3))  #12
print(is_prime(29))  #13
print(capitalize_names(["alice", "bob", "charlie"]))  #14
print(process_numbers([1, 2, 3, 4, 5]))  #15
print(reverse_upper("example"))  #16
categorize_strings(["dato", "nika", "polieqtori", "zaza"])  #17
print(process_string_list(["example", "test", "string"]))  #18
print(categorize_case(["DATA", "text", "MIXED", "case"]))  #19
print(find_and_transform("banana"))  #20
