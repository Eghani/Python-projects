# Mad Libs Game in Python

# Function to play Mad Libs
def play_madlibs():
    # Template for the story
    story_template = """
    Once upon a time in a {adjective1} land, there was a {adjective2} {noun1} named {name}. 
    {name} loved to {verb1} and {verb2} all day long. One day, {name} met a {adjective3} 
    {noun2} who told {name} about a hidden treasure in a {adjective4} cave. Together, 
    they {verb3} and {verb4} until they found the treasure. They lived happily ever after.
    """

    # Collecting user input
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    noun1 = input("Enter a noun: ")
    name = input("Enter a name: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    adjective3 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    adjective4 = input("Enter one more adjective: ")
    verb3 = input("Enter one more verb: ")
    verb4 = input("Enter one last verb: ")

    # Filling in the template with user input
    story = story_template.format(
        adjective1=adjective1,
        adjective2=adjective2,
        noun1=noun1,
        name=name,
        verb1=verb1,
        verb2=verb2,
        adjective3=adjective3,
        noun2=noun2,
        adjective4=adjective4,
        verb3=verb3,
        verb4=verb4
    )

    # Printing the story
    print("\nHere is your Mad Libs story:\n")
    print(story)

# Start the game
play_madlibs()
