

import random
from hangman_words import word_list  #all the words are imported from hangman_words file
from hangman_art import stages  # all the arts are imported from hangman_art file


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6



#Testing code
for position in chosen_word:
print(f"the letter in the word is {chosen_word[0]} ")

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess end_of_game = True
            not in chosen_word:
        
        lives -= 1
        if lives == 0:
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    print(stages[lives])
