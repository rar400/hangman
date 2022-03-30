# lab 3
# hangman
# CAS a function that allows the user to play hangman
# (no graphical element required)

correct_guessed_list = set()  # create empty list to include the correct guessed letter inside


def hangman(word, guesses, tries):
    guessed_word = set(word)

    while len(guessed_word) > 0 and guesses > 0:
        print()
        print('word has ', len(word), ' number of letters')
        guess = input("guess letter: ")

        # guess letter in words, increase number of guesses
        if guess in word:
            if guess in correct_guessed_list:
                print("already picked letter")

            correct_guessed_list.add(guess)
            tries = tries + 1  # used to reduce number of _ in hangman
            print((*correct_guessed_list, ' _ ' * (len(word) - tries)), "You have", guesses, "guesses, good luck.")
            if guess in guessed_word:
                guessed_word.remove(guess)

        # guess letter not in word, winds down the guesses
        else:
            print("no, letter not in word")

            guesses = guesses - 1  # reduces # of guess
            print((*correct_guessed_list, ' _ ' * (len(word) - tries)), "You have", guesses, "guesses, good luck.")

    #end of loop after guess word right or end of guesses
    if guesses == 0:
        print("no more guesses, the correct word is: ", word)
    else:
        print("guessed the word correctly: ", word)

hangman('abc', 4, 0)  # first is the word, second is the number of guesses alowed,
# third is to reduce number of dash _


