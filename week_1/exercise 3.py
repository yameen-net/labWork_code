
#Task 1

x = int(input("enter a number to be checked"))
if x < 0:
    print("your number is negative")
elif x > 0:
    print("your number is positive")
else:
    print ("your number is 0")



#Task 2


consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
vowels = ["A", "E", "I", "O", "U"]

word = input("Enter a word: ")

#print(list)

first_char = word[0].upper()
if first_char in consonants:
    print("Your word starts with a consonant!")
elif first_char in vowels:
    print("Your word starts with a vowel!")
else:
    print("Your word starts with neither a vowel nor a consonant.")
      

#Task 3

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")