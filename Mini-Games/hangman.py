import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "science", "developer", "learning"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def get_hint(word, guessed_letters):
    remaining_letters = [letter for letter in word if letter not in guessed_letters]
    return random.choice(remaining_letters)

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6  # Set the maximum number of incorrect attempts

    print("Welcome to Hangman!")

    while attempts > 0:
        current_display = display_word(word_to_guess, guessed_letters)
        print("\nCurrent word: ", current_display)
        
        if current_display == word_to_guess:
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break

        print("Hints remaining:", attempts)
        give_hint = input("Do you want a hint? (yes/no): ").lower()

        if give_hint == "yes":
            hint = get_hint(word_to_guess, guessed_letters)
            print("Hint:", hint)
            attempts -= 1
            continue

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print("Incorrect guess. Attempts left:", attempts)
        
        if attempts == 0:
            print("Sorry, you're out of attempts. The word was:", word_to_guess)
            break

    print("\nThanks for playing Hangman!")

# Run the Hangman game with hints
hangman()
