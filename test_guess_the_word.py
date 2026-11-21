
# Brenden Lomax
# CIS256 Fall 2026
# Programming Assignment 4


import guess_the_word

# Test that the word that comes from the list
def test_choose_word():
    word = guess_the_word.choose_word()
    assert word in guess_the_word.words

# Test a correct guess to see if the function returns True
def test_correct_guess():
    assert guess_the_word.check_guess("People", "e") == True

# Test an incorrect guess to see if the function returns False
def test_wrong_guess():
    assert guess_the_word.check_guess("People", "x") == False

# Test displaying guessed letters to see if the function returns the correct string with underscores for unguessed letters
def test_display_word():
    assert guess_the_word.display_word("People", ["e", "o"]) == "_e__o"