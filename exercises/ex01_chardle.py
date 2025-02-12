"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730475322"

five_char_word: str = input("Enter a 5-character word: ")
if len(five_char_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_character + " in " + five_char_word)

if five_char_word[0] == single_character:
    print(single_character + " found at index 0")

if five_char_word[1] == single_character:
    print(single_character + " found at index 1")

if five_char_word[2] == single_character:
    print(single_character + " found at index 2")

if five_char_word[3] == single_character:
    print(single_character + " found at index 3")

if five_char_word[4] == single_character:
    print(single_character + " found at index 4")

number_of_matching_characters = 0
if five_char_word[0] == single_character:
    number_of_matching_characters = number_of_matching_characters + 1

if five_char_word[1] == single_character:
    number_of_matching_characters = number_of_matching_characters + 1

if five_char_word[2] == single_character:
    number_of_matching_characters = number_of_matching_characters + 1
            
if five_char_word[3] == single_character:
    number_of_matching_characters = number_of_matching_characters + 1

if five_char_word[4] == single_character:
    number_of_matching_characters = number_of_matching_characters + 1

if number_of_matching_characters == 0:
    print("No instances of " + single_character + " found in " + five_char_word)
else:
    if number_of_matching_characters == 1:
        print("1 instance of " + single_character + " found in " + five_char_word)
    else: 
        print(str(number_of_matching_characters) + " instances of " + single_character + " found in " + five_char_word)
