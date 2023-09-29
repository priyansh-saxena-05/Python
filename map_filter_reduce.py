# 1. filter() Function:
# Filter List Elements Based on a Condition:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# Output: [2, 4, 6, 8, 10]

# Filter Out Empty Strings from a List:

words = ["hello", "", "world", "", "python", ""]
non_empty_words = list(filter(lambda x: x != "", words))
# Output: ["hello", "world", "python"]

# 2. map() Function:
# Convert List of Temperatures from Celsius to Fahrenheit:

celsius_temperatures = [0, 10, 20, 30, 40]
fahrenheit_temperatures = list(map(lambda x: (9/5) * x + 32, celsius_temperatures))
# Output: [32, 50, 68, 86, 104]

# Extract First Letter from a List of Words:

words = ["apple", "banana", "cherry", "date"]
first_letters = list(map(lambda x: x[0], words))
# Output: ['a', 'b', 'c', 'd']


# 3. reduce() Function:
# Calculate the Product of All Elements in a List:
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
# Output: 120

# Concatenate Strings in a List:

words = ["Hello", " ", "World", "!"]
concatenated_string = reduce(lambda x, y: x + y, words)
# Output: "Hello World!"
