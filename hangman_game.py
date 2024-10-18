import random
word_list = ["paper", "helicopter", "house", "parents", "peach"]

#TODO 1: Create a variable "lives" to keep track of the player lives
# Set "lives" to 6
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = "_" * len(chosen_word)
print(placeholder)


game_over = False
correct_letters = []


while not game_over:
    guess = input("Please choose a letter: ").lower()

    display = ""


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # TODO 2: If guess is not a letter in chosen_word, remove a life.
    # If lives goes down to 0, then the game should end.

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lost...")

    if "_" not in display:
        game_over = True
        print("You win")



