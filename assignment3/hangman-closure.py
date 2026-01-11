# Task 4: Closure Practice

def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        if letter not in guesses:
            guesses.append(letter)

        display = ""
        for x in secret_word:
            if x in guesses:
                display += x 
            else:
                display += "_"

        print(display)

        if "_" not in display:
            return True
        else:
            return False
    return hangman_closure

secret_word = input("Enter a secret word: ")
game = make_hangman(secret_word)

guessed = False
while not guessed:
    letter = input("Guess a letter: ")
    guessed = game(letter)

print(f"Congrats! you've guessed correct '{secret_word}' .")

