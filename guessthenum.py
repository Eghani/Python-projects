# number guessing game 

import random 
ran_number = random.randint(1,1000)
attempts = 10 
print("The game is ON ")


while attempts > 0:
    try:
        #taking input 
        user_num = int(input("ENter your guess : "))
    #check if the guess is righ or wrong 
        if user_num == ran_number:
           print("Congratulation, you have guessed the number . ")
           break
        elif user_num > ran_number:
            print("Too high ")
        elif user_num < ran_number:
            print("Too low ")
        # decreasing the attempts 
        attempts -= 1
        print(f"Attempts left : {attempts}")
        # ran out of attempts 
        if attempts == 0:
            print(f"sorry, you got no attempts left. try next time, random number is {ran_number}")
            break
    except ValueError:
        print("invalid guess try agian")
    


    """
    Sure! Here's a summary of the number guessing game script:

1. **Initialization**:
   - A random number between 1 and 1000 is generated.
   - The player has 10 attempts to guess the number.
   - The game starts with the message "The game is ON."

2. **Game Loop**:
   - The player inputs a guess.
   - If the guess is correct, the player is congratulated, and the game ends.
   - If the guess is too high or too low, a corresponding message is displayed.
   - The number of remaining attempts is shown.
   - If attempts reach zero, the game informs the player they have run out of attempts and reveals the random number.
   - If the input is invalid (not an integer), the player is prompted to try again.

3. **End of Game**:
   - The game ends either when the player guesses correctly or runs out of attempts.
    """