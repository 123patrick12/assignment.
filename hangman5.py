#murokore patrick 223015792
#mukamfizi gisele 223017533


import random
import string

# List of English words for the game
words = ["python", "hangman", "computer", "programming", "developer", "algorithm"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to initialize the game
def initialize_game():
    word = choose_word()
    word = word.lower()
    guessed_word = "-" * len(word)
    guessed_letters = set()
    guesses_remaining = 6
    warnings_remaining = 3
    return word, guessed_word, guessed_letters, guesses_remaining, warnings_remaining

# Function to display the current game state
def display_game(word, guessed_word, guessed_letters, guesses_remaining, warnings_remaining):
    print("\nWord:", " ".join(guessed_word))
    print("Guesses remaining:", guesses_remaining)
    print("Warnings remaining:", warnings_remaining)
    print("Unused letters:", " ".join(sorted(set(string.ascii_lowercase) - guessed_letters)))

# Function to check if the game is won
def is_game_won(guessed_word):
    return "-" not in guessed_word

# Function to play the game
def play_hangman():
    print("Welcome to Hangman!")
    word, guessed_word, guessed_letters, guesses_remaining, warnings_remaining = initialize_game()

    while guesses_remaining > 0:
        display_game(word, guessed_word, guessed_letters, guesses_remaining, warnings_remaining)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Invalid input. You have", warnings_remaining, "warnings left.")
            else:
                guesses_remaining -= 1
                print("Invalid input. You have no warnings left. You lose a guess.")
            continue

        if guess in guessed_letters:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("You've already guessed that letter. You have", warnings_remaining, "warnings left.")
            else:
                guesses_remaining -= 1
                print("You've already guessed that letter. You have no warnings left. You lose a guess.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word = guessed_word[:i] + guess + guessed_word[i + 1:]
            if is_game_won(guessed_word):
                score = guesses_remaining * len(set(word))
                print("Congratulations! You've won the game with a score of", score)
                break
        else:
            if guess in "aeiou":
                guesses_remaining -= 2a
            else:
                guesses_remaining -= 1

    if not is_game_won(guessed_word):
        print("Sorry, you've run out of guesses. The word was:", word)

if __name__ == "__main__":
    play_hangman()