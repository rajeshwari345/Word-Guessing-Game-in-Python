import random

# List of words to guess from
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

def word_guessing_game():
    # Choose a random word from the list
    word_to_guess = random.choice(word_list)
    
    # Initialize the guessed word with underscores
    guessed_word = ["_"] * len(word_to_guess)
    
    # Initialize the number of attempts
    attempts = 0
    
    # Initialize the maximum number of attempts
    max_attempts = 6
    
    print("Welcome to the word guessing game!")
    print("I'm thinking of a word with", len(word_to_guess), "letters.")
    print("You have 6 attempts to guess it.")
    
    while attempts < max_attempts:
        # Print the current state of the guessed word
        print(" ".join(guessed_word))
        
        # Ask the player for their guess
        user_guess = input("Enter a letter: ").lower()
        
        # Check if the input is a single letter
        if len(user_guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
        
        # Check if the letter is in the word
        if user_guess in word_to_guess:
            # Reveal the correct letters
            for i, letter in enumerate(word_to_guess):
                if letter == user_guess:
                    guessed_word[i] = user_guess
        else:
            # Increment the number of attempts
            attempts += 1
            print("Incorrect! You have", max_attempts - attempts, "attempts left.")
        
        # Check if the player has guessed the word
        if "_" not in guessed_word:
            print(" ".join(guessed_word))
            print("Congratulations! You guessed the word.")
            return
    
    # If the player runs out of attempts, reveal the word
    print("Sorry, you didn't guess the word. The correct answer was", word_to_guess)

if __name__ == "__main__":
    word_guessing_game()
