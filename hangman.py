"""
Name    : Zainab Batool
Program : BS Business Data Analytics, COMSATS University Islamabad
Internship : CodeAlpha - Python Programming
Task 1  : Hangman Game
"""

import random

WORDS = ["python", "analytics", "pandas", "internship", "dataset"]
MAX_WRONG = 6


def show_progress(word, guessed):
    """Return the word with unguessed letters hidden as underscores."""
    return " ".join(letter if letter in guessed else "_" for letter in word)


def play():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0

    print("=== HANGMAN GAME ===")
    print(f"Guess the word one letter at a time. You have {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG:
        print("Word:", show_progress(word, guessed))
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")
        print("Guessed letters:", " ".join(sorted(guessed)) if guessed else "none")

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.append(guess)

        if guess in word:
            print("Correct!\n")
        else:
            wrong += 1
            print("Wrong!\n")

        if all(letter in guessed for letter in word):
            print("Word:", show_progress(word, guessed))
            print("Congratulations! You won!")
            return

    print(f"Game over! The word was: {word}")


if __name__ == "__main__":
    while True:
        play()
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Thanks for playing. Goodbye!")
            break
        print()
