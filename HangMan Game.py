#Hangman Game Yolanda Mokoena

import  random

# List of words to guess
words = ['correlation', 'system', 'java', 'pizza', 'cooldrink', 'web']

# Randomly choose a word from the list
players_word = random.choice(words)
word_screen = ['_' for _ in players_word]  # Create a list of underscores
attempts = 4  # Number of allowed attempts

print("Welcome to the Hangman game!")

while attempts > 0 and  '_' in word_screen:
    print("\n" + ' '.join(word_screen))
    guessed_letter = input("Choose a letter: ").lower()
    if guessed_letter in players_word:
        for index, letter in enumerate(players_word):
            if letter == guessed_letter:
                word_screen[index] = guessed_letter # revealing the letter

        else:
            print("Invalid Letter in the word")
            attempts -= 1

if '_' not in word_screen:
    print("Look at you!! You guessed the word correctly")
    print(' '.join(word_screen))
    print("You did it!")

else:
    print("You don't have any attempts left. The word was : " + players_word)
    print("You lost the game :(")

