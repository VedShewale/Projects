#Hangman Game

import random

word = input("Enter a word for your opponent: ")
word_display = ["_" for _ in word]
attempts = 8

print("Welcome to the game of Hangman")

while attempts > 0 and "_" in word_display:
    print("\n" + " ".join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                word_display[index] = guess
    else:
        print("Letter is not in the word")
        attempts -= 1


if "_" not in word_display:
    print("You guessed the word!")
    print(" ".join(word_display))
else:
    print("You lost the word was: " + word)