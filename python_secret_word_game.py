from random import randint

# Have a list of secret words.

secret_dictionary = ['rubber']
size_of_dictionary = len(secret_dictionary) - 1

# Randomly choose a word from the random dictionary
secret_word = secret_dictionary[randint(0, size_of_dictionary)]

size_secret_word = len(secret_word)
number_of_guesses = 6
guess_list = []
letter_array = []


print("Hello! Let's guess a word: ")

# Creates the _ _ _ of a blank hangman board
for each in range(0, size_secret_word):
    letter_array.append("_")

for each in range(0, size_secret_word):
    print(letter_array[each], end=" ")

while number_of_guesses > 0:
    multiple_letter_check = 0
    player_guess = input("\n\nGuess a letter! ").lower()
    while player_guess in guess_list:
        player_guess = input("\n\nGuess a different letter! ").lower()

    if player_guess == secret_word:
        print("Good guess! YOU WIN!!")
        break
    if player_guess not in guess_list:
        guess_list.append(player_guess)
        number_of_guesses -= 1
        for each in range(0, size_secret_word):
            if (player_guess == secret_word[each]):
                letter_array[each] = player_guess
                multiple_letter_check += 1

    if multiple_letter_check > 0:
        number_of_guesses += 1

    for each in range(0, size_secret_word):
        print(letter_array[each], end=" ")

    print(guess_list)
    print(f'You have {number_of_guesses} guesses left!')
    if letter_array.count('_') == 0:
        print("You WIN!")
        break
