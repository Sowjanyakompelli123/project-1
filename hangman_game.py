import random

# List of words to choose from
words = ["python", "javascript", "developer", "programming", "hangman", "computer"]

# Function to play the Hangman game
def play_hangman():
    # Select a random word from the list
    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Set a limit on incorrect guesses
    revealed_word = ["_" for _ in word]  # Hidden word representation

    print("Welcome to Hangman!")
    print("Guess the word:", " ".join(revealed_word))
    print(f"You have {max_incorrect_guesses} incorrect guesses allowed.\n")

    # Game loop
    while incorrect_guesses < max_incorrect_guesses and "_" in revealed_word:
        guess = input("Guess a letter: ").lower()

        # Check if input is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    revealed_word[i] = guess
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word. Incorrect guesses: {incorrect_guesses}")

        # Display the current state of the word
        print("Word:", " ".join(revealed_word))
        print("Guessed letters:", ", ".join(guessed_letters))

    # End game result
    if "_" not in revealed_word:
        print("\nCongratulations! You've guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)

# Run the Hangman game
play_hangman()