# set of question get it from ai
questions = [
    {
        "question": "What is the value of π (Pi) rounded to two decimal places?",
        "choices": ["A. 3.12", "B. 3.14", "C. 3.16", "D. 3.18"],
        "answer": "B"
    },
    {
        "question": "What is the square root of 144?",
        "choices": ["A. 10", "B. 12", "C. 14", "D. 16"],
        "answer": "B"
    },
    {
        "question": "What is the formula for the area of a circle?",
        "choices": ["A. 2πr", "B. πr^2", "C. πd", "D. 2πr^2"],
        "answer": "B"
    },
    {
        "question": "Solve for x: 2x + 3 = 11",
        "choices": ["A. 4", "B. 5", "C. 6", "D. 7"],
        "answer": "A"
    },
    {
        "question": "What is the sum of the angles in a triangle?",
        "choices": ["A. 90 degrees", "B. 180 degrees", "C. 270 degrees", "D. 360 degrees"],
        "answer": "B"
    }

]

# main work 
def quiz():
    score = 0 
    # asking user all the questions and taking answers
    for q in questions:
        print(q["question"])
        for choice in q["choices"]:
            print(choice)
        answer = input ("your answer (A,B,C, or D): ").upper()    
        # checking the answer based on that we will show the result 
        if answer == q["answer"]:
            print("Correct!\n")
            # each question is for  1 mark 
            score += 1
        else:
            print(f"Wrong ! the correct answer is {q['answer']} \n ")    
    # showing the final result 
    print(f"Your final score is {score} out of {len(questions)}")        

# calling the function
if __name__ == "__main__":
    quiz()






#Questions Setup:

#A list of questions is defined, each with a question, multiple-choice options, and the correct answer.



#Main Function - quiz():

#Initializes the player's score to 0.
#Iterates through each question, presenting it and its choices to the player.
#Takes the player's answer and checks if it's correct.
#If the answer is correct, the player is informed, and the score is incremented.
#If the answer is incorrect, the player is informed of the correct answer.
#After all questions are answered, the final score is displayed.



#Game Execution:

#The quiz() function is called if the script is run as the main module.

