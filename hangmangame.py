import random

# Predefined list of words
word_list = ["apple", "robot", "train", "green", "chair"]
chosen_word = random.choice(word_list)  # Randomly select a word

# Setup game variables
guessed_letters = []  # To store guessed letters
tries_left = 6
display = ["_" for _ in chosen_word]  # Hidden word display

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Main game loop
while tries_left > 0 and "_" in display:
    print("Word: ", " ".join(display))
    guess = input("Guess a letter: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabetic character.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Good guess!\n")
        # Reveal the guessed letter(s)
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
    else:
        tries_left -= 1
        print(f"❌ Incorrect guess. You have {tries_left} tries left.\n")

# Final result
if "_" not in display:
    print("🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("💀 Game over. The word was:", chosen_word)
