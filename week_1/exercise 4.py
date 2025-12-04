# Task 1:  Print the numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)


# Task 2: Print the even numbers from 2 to 10 usng a for loop.
for i in range(2, 11, 2):
    print(i)


# Task 3 print the first 5 numbers of the Fibonacci sequence using a while loop.

a, b = 0, 1  # Starting values for the Fibonacci sequence.
count = 0
while count < 5:
    print(a)
    a, b = b, a + b  # Update the sequence.
    count += 1