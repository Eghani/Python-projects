secret_word = "python"
list_of_hint = ["game", "python", "coding", "computer", "java", "microsoft", "meta", "google", "coffee", "cpp"]

chance = 3
print("Guess the Word from the Below list wisely :-\n")
print(list_of_hint)

while(chance > 0):
    user_guess = input("\nEnter the word you think is the secret word from the given words :- ")
    
    if user_guess == secret_word:
        print("Congratulations! You have guessed the word.")
        break
    else:
        chance -= 1
        if chance > 0:
            print("You have guessed the word wrong!\n")
            print(f"You have {chance} chance(s) left.")
        else:
            print("Sorry! You have no chances left. Restart the game.")



"""


This Python project features a simple word guessing game where players attempt to identify a secret word from a list of hints. The game initializes with a set number of chances, and players input their guesses to determine the secret word. Each incorrect guess reduces the number of remaining chances, while correct guesses lead to a congratulatory message and end the game. If all chances are exhausted without a correct guess, the game prompts the user to restart. This project demonstrates basic game logic and user interaction in Python.

Instructor: Ehteshamul Ghani (aka Kabir)



"""