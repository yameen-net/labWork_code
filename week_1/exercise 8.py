import random

# List of words and maximum incorrect guesses allowed
word_list = ["python", "java", "javascript"]
max_guesses = 6

# Randomly select a word from the list
word = random.choice(word_list)
word_letters = set(word)
guessed_letters = set()
incorrect_guesses = 0

# Function to show the amount of letters
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

print("Let's play Hangman!")
print("Word to guess:")
print(display_word(word, guessed_letters))
print(f"You have {max_guesses} incorrect guesses allowed.\n")

#while loop
while incorrect_guesses < max_guesses and word_letters != guessed_letters:
    guess = input("Guess a letter: ").lower()
    
    # validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.\n")
        continue

    # If letter has already been guessed.
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    # Check if the guessed letter is in the word
    if guess in word_letters:
        guessed_letters.add(guess)
        print("Correct!")
    else:
        incorrect_guesses += 1
        print(f"Incorrect! You have {max_guesses - incorrect_guesses} guesses left.")
    
    print("\n" + display_word(word, guessed_letters) + "\n")

# Outcome of the game.
if word_letters == guessed_letters:
    print(f"Congratulations, you guessed the word \"{word}\"!")
else:
    print(f"Game over! The word was \"{word}\".")