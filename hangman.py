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

    if attempts == 8:
        print("----------------")
    if attempts == 7:
        print("----------------")
        print(      "(-_-)"     )
    if attempts == 6:
        print("----------------")
        print("      (-_-)     ")
        print("        |       ")
        print("        |       ")
        print("        |       ")
    if attempts == 5:
        print("----------------")
        print("      (-_-)     ")
        print("        | \     ")
        print("        |  \    ")
        print("        |       ")
    if attempts == 4:
        print("----------------")
        print("      (-_-)     ")
        print("      / | \     ")
        print("     /  |  \    ")
        print("        |       ")
    if attempts == 3:
        print("----------------")
        print("      (-_-)     ")
        print("      / | \     ")
        print("     /  |  \    ")
        print("        |       ")
        print("         \      ")
        print("          \     ")
    if attempts == 2:
        print("----------------")
        print("      (-_-)     ")
        print("      / | \     ")
        print("     /  |  \    ")
        print("        |       ")
        print("         \      ")
        print("          \     ")
    if attempts == 1:
        print("----------------")
        print("      (-_-)     ")
        print("      / | \     ")
        print("     /  |  \    ")
        print("        |       ")
        print("       / \      ")
        print("      /   \     ")

if "_" not in word_display:
    print("You guessed the word!")
    print(" ".join(word_display))
else:
    print("You lost the word was: " + word)
