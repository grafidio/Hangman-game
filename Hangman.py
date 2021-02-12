import random
from listofwords import words
def hangman():
    guesses = []
    lives = 7
    count = 0 
    secret_word = random.choice(words)
    print("The word has " + str(len(secret_word)) + " characters.")
    #print(secret_word)
    while lives >= 1 and count < len(secret_word):
        guess = input("pick a letter ")
        guesses.append(guess)
        #if guess in guesses:
        #    print("You already picked that letter boiii, try again")
        print(guesses)
        if len(guess) > 1:
            print("you entered more than one letter, try again")
        elif guess in secret_word:
            print(f"Well done, {guess} is in the secret word")
            character_numbers_index0 = [pos for pos, char in enumerate(secret_word) if char == guess] 
            character_numbers_index = [x+1 for x in character_numbers_index0]
            count += len(character_numbers_index)
            print("Chosen character is in position: " + str(character_numbers_index))
        elif guess not in secret_word:
            lives -= 1
            print(f"Wrong choice, you have {lives} lives remaining.")
    if count == len(secret_word):
                print(f"you win! The word was '{secret_word}' ")
    if lives == 0:
        print(f"You ran out of lives! The word was '{secret_word}''. Run to try again")
    

    
#glitch - can just spam a correct character and win by entering one correct character 
hangman()



