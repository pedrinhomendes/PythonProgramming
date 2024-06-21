import random
def get_difficulty():
    while True:
        difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
        if difficulty in ['easy', 'medium', 'hard']:
            return difficulty
        print("Invalid input. Please choose 'easy', 'Medium', or 'hard'.")

def get_word(difficulty):
    words = {
        'easy': ["salt", "roof", "left"],
        'medium': ["heart", "sports", "levels"],
        'hard': ["computer", "vancouver", "university"]
    }
    return random.choice(words[difficulty])

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def get_guess(all_guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in all_guessed_letters:
                print("You already guessed this letter, Try again!")
            else:
                return guess
        else:
            print("Invalid input. Please enter a single letter.")

def update_state(word, guessed_letters, guess, attempts):
    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        print(f"Good guess! '{guess}' is in the word")
        guessed_letters.add(guess)
    else:
        print("Incorrect guess.")
        attempts -= 1
    return attempts

def check_win(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

def play_game():
    print("Welcome to Hangman!")

    difficulty = get_difficulty()
    word = get_word(difficulty)
    guessed_letters = set()
    all_guessed_letters = []
    attempts = 6

    while attempts > 0:
        print(f"\nCurrent word: {display_word(word, guessed_letters)}")
        print(f"Attempts remaining: {attempts}")
        print(f"Guessed letters: {', '.join(all_guessed_letters)}")

        guess = get_guess(all_guessed_letters)
        all_guessed_letters.append(guess)
        attempts = update_state(word, guessed_letters, guess, attempts)

        if check_win(word, guessed_letters):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Game over. The word was: {word}")


if __name__ == "__main__":
    play_game()









