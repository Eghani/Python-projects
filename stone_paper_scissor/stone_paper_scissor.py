''''
1 -> stone
2 -> paper
3 -> scissor
'''


#CODE -> 

import random

computer = random.choice([1,2,3])
user_str = input("Enter\n st -> stone\n pa -> paper\n sc -> scissor\nyour choice :- ")
user_dict = {"st" : 1 , "pa" : 2 , "sc" : 3}
reversedict = {1 : "Stone" , 2 : "Paper" , 3 : "Scissor"}

user = user_dict[user_str]

print(f"You chose:- {reversedict[user]}\nComputer choice:- {reversedict[computer]}")
print("")

if computer == user:
    print("Draw !")
else:
    if computer == 1 and user == 2:
        print("You win")
    elif computer == 1 and user == 3:
        print("Computer win")
    elif computer == 2 and user == 1:
        print("Computer win")
    elif computer == 2 and user == 3:
        print("You win")
    elif computer == 3 and user == 1:
        print("You win")
    elif computer == 3 and user == 2:
        print("Computer win")
    else:
        print("Network issue")



# you can make it short by finding small pattern in the combination 