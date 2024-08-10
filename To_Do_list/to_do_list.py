# How to make to do list in python easy tutorial with no voice over this 
# video is just for understanding 

# giving user the choice 
# making by using function for better understandin


# this function will show tasks
def show_task(tasks):
    if not tasks:
        print("NO task in your to-do list !")
    else:
        print("\nYour To-Do list:")
        task_number = 1
        for task in tasks:
            print(f"{task_number}. {task}")
            task_number += 1
    print()

# this function will add task
def add_task(tasks):
    task = input("Enter a new task : ")
    tasks.append(task)
    print(f"task '{task}' added !")


# this function will remove task 
def remove_task(tasks):
    show_task(tasks)
    task_number = int(input("ENter the task number to remove : "))
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' Removed ! \n")
    else:
        print("Invalid task number\n")

def main():
    tasks = [] # empty container in which we will store the
    while True:
        print("\n1. view to-do list\n2. Add task\n3. Remove task\n4. exit\n")
        choice = input("ENter the choice between (1-4) :- ")

        #checking the input
        if choice == '1':
            show_task(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Best of luck ! ")
            break
        else:
            print("invalid choice! please enter between (1-4)")

# testing 
main()


# this is a code for to-do list 
# this video will be uploaded in few min with out editting 
# this is an avg time to make a mini project 
# the code will be available in my git hub link will be in the description


# thanks for watching ! | : | 