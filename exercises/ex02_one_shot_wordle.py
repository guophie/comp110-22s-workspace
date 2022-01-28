"""Example of Wordle Game with one word."""

__author__ = "730475322"

secret_word: str = "python"
word_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

while len(word_guess) != len(secret_word):
    word_guess: str = input(f"That was not {len(secret_word)} letters! Try again: ")

test_index = 0
emoji_results: str = ""
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

while test_index < len(secret_word):
    guessed_letter_in_secret_word: bool = False
    alternate_indices = 0
    if secret_word[test_index] == word_guess[test_index]:
        emoji_results = emoji_results + green_box + " "
        test_index += 1
    else:  # testing if guessed letter is in any place in the secret word
        while alternate_indices < len(secret_word) and not guessed_letter_in_secret_word:
            if word_guess[test_index] == secret_word[alternate_indices]:
                guessed_letter_in_secret_word: bool = True
            else:
                alternate_indices += 1
        if guessed_letter_in_secret_word:
            emoji_results = emoji_results + yellow_box + " "
            test_index += 1
        else:  # guessed letter was not found in secret word
            emoji_results = emoji_results + white_box + " "
            test_index += 1

    
print(emoji_results)

if word_guess != secret_word:
    print("Not quite. Play again soon!")
else: 
    print("Woo! You got it!")