#1.
def add_five(number):
    return number + 5

#2.
def multiply(a, b):
    return a * b

#3.
def string_length(s):
    return len(s)

#4.
def list_of_string_lengths(strings):
    return [len(s) for s in strings]

#5.
def is_palindrome(s):
    return s == s[::-1]

#6.
def longest_string(strings):
    if not strings:
        return None
    return max(strings, key=len)

#7.
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#8.
def sum_of_maximums(list1, list2):
    if not list1 or not list2:
        return None
    return max(list1) + max(list2)

#9.
def difference_of_minimums(list1, list2):
    if not list1 or not list2:
        return None
    return min(list1) - min(list2)

#10.
def difference_max_min(numbers):
    if not numbers:
        return None
    return max(numbers) - min(numbers)

#11.
def sum_of_elements(numbers):
    return sum(numbers)

#12.
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

#13.
def squares_list(numbers):
    return [n ** 2 for n in numbers]

#14.
def reverse_string(s):
    return s[::-1]

#15.
def is_even(n):
    return n % 2 == 0

#16.
def longest_string_in_list(strings):
    if not strings:
        return None
    return max(strings, key=len)

#17.
def smallest_number(numbers):
    if not numbers:
        return None
    return min(numbers)

#18.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#19.
def to_uppercase(s):
    return s.upper()

#20.
def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

# Example usage
print(add_five(10))  #1
print(multiply(3, 4))  #2
print(string_length("hello"))  #3
print(list_of_string_lengths(["apple", "banana", "cherry"]))  #4
print(is_palindrome("racecar"))  #5
print(longest_string(["apple", "banana", "cherry"]))  #6
print(factorial(5))  #7
print(sum_of_maximums([1, 2, 3], [4, 5, 6]))  #8
print(difference_of_minimums([1, 2, 3], [4, 5, 6]))  #9
print(difference_max_min([1, 2, 3, 4, 5]))  #10
print(sum_of_elements([1, 2, 3, 4, 5]))  #11
print(count_vowels("hello world"))  #12
print(squares_list([1, 2, 3, 4, 5]))  #13
print(reverse_string("hello"))  #14
print(is_even(4))  #15
print(longest_string_in_list(["apple", "banana", "cherry"]))  #16
print(smallest_number([1, 2, 3, 4, 5]))  #17
print(gcd(48, 18))  #18
print(to_uppercase("hello world"))  #19
print(average([1, 2, 3, 4, 5]))  #20
