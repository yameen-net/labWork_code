# Task 1 Function to take two numbers as parameters and return their sum
def add_numbers(a, b):
    return a + b

# Example
print("Sum:", add_numbers(5, 7))  


# task 2 Function that takes a list of numbers as a parameter and returns the largest number
def find_largest(numbers):
    if not numbers:  # check for empty list
        return None
    return max(numbers)

# Example
num_list = [3, 9, 2, 15, 7]
print("Largest number:", find_largest(num_list))  


# Task 3 Function that takes a string as a parameter and returns the number of vowels in the string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example
sample_text = "Hello World!"
print("Number of vowels:", count_vowels(sample_text))  