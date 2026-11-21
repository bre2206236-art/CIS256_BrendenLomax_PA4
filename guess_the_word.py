# Brenden Lomax
# CIS256 Fall 2026
# Programming Assignment 4

import random

# List of words for the game
words = ["People", "Gaming", "Work", "School"]

# Choose a random word
def choose_word():
    return random.choice(words)

# Check if the guessed letter is in the word
def check_guess(word, letter):
    if letter in word:
        return True
    return False

# Display the guessed letters for the user
def display_word(word, guesses):
    result = ""
    for letter in word:
        if letter in guesses:
            result = result + letter
        else:
            result = result + "_"
    return result

# Main game loop 
#uses loop to allow user to guess letters until they run out of attempts or guess the word correctly
if __name__ == "__main__":
    word = choose_word()
    guesses = []
    attempts = 6

    while attempts > 0:
        print(display_word(word, guesses))
        guess = input("Guess a letter: ").lower()

        if guess in guesses:
            print("Already guessed!")
        elif check_guess(word, guess):
            guesses.append(guess)
            print("Correct!")
        else:
            guesses.append(guess)
            attempts = attempts - 1
            print("Wrong! Attempts left:", attempts)

        if display_word(word, guesses) == word:
            print("You guessed Correctly!")
            break

    if attempts == 0:
        print("Excellent! The word was:", word)