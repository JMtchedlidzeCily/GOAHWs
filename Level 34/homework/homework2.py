# Separate string variables
string1 = "apple,banana,cherry"
string2 = "one;two;three"
string3 = "hello world"
string4 = "python|java|c++"
string5 = "a-b-c-d-e"
string6 = "dog cat mouse"
string7 = "red/green/blue"
string8 = "2024-07-31"
string9 = "name:age:city"
string10 = "item1:item2:item3:item4"

# Use split() on each string and store results in separate lists
split1 = string1.split(',')    # Split by comma
split2 = string2.split(';')    # Split by semicolon
split3 = string3.split()       # Split by whitespace (default behavior)
split4 = string4.split('|')    # Split by pipe
split5 = string5.split('-')    # Split by hyphen
split6 = string6.split()       # Split by whitespace (default behavior)
split7 = string7.split('/')    # Split by forward slash
split8 = string8.split('-')    # Split by hyphen
split9 = string9.split(':')    # Split by colon
split10 = string10.split(':')  # Split by colon