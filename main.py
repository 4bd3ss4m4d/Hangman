import random
# Function definitions

# Function index that determines character's index
def index(userchar, randomlist):
    randomlist = randomlist
    indices = []
    for i in range(len(randomlist)):
        if randomlist[i] == userchar:
            indices.append(i)
    return indices
#Hangman ASCII Art
abdessamad = '''
██╗  ██╗██████╗ ██████╗ ██████╗ ███████╗███████╗██╗  ██╗███╗   ███╗██╗  ██╗██████╗     
██║  ██║██╔══██╗██╔══██╗╚════██╗██╔════╝██╔════╝██║  ██║████╗ ████║██║  ██║██╔══██╗    
███████║██████╔╝██║  ██║ █████╔╝███████╗███████╗███████║██╔████╔██║███████║██║  ██║    
╚════██║██╔══██╗██║  ██║ ╚═══██╗╚════██║╚════██║╚════██║██║╚██╔╝██║╚════██║██║  ██║    
     ██║██████╔╝██████╔╝██████╔╝███████║███████║     ██║██║ ╚═╝ ██║     ██║██████╔╝    
     ╚═╝╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝     ╚═╝╚═╝     ╚═╝     ╚═╝╚═════╝  
'''
h1 = '''
 +---+
  |   |
      |
      |
      |
      |
=========
'''
h2 = '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
'''
h3 = '''
 +---+
  |   |
  O   |
  |   |
      |
      |
=========
'''
h4 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''
h5 = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''
h6 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''
h7 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
'''
hangman_cicle = [h1, h2, h3, h4, h5, h6, h7]

# This is a Prototype of the Hangman Game.
print("Welcome to the Hangman Game!\n")
print(h1+ "\n")

# A list of words
words = ["Book", "Pencil", "School"]

# Choose a random word from the list of words
maximum_number_of_word = len(words)-1

try_again = 'y'

while try_again == 'y' or try_again == 'Y':
    lifecounter = 0
    x = random.randint(0, maximum_number_of_word)
    randomword = words[x]

    # Create a list contaiting blank spaces equal to the word chosen.
    randomword = randomword.lower()
    randomwordlist = list(randomword)
    blankwordlist = []
    for character in randomwordlist:
        blankwordlist.append("_")
    blankwordlist.append(".")

    # Prompt the user the blankword
    blankword = "".join(blankwordlist)
    number_of_char = len(randomword)
    print(f"\nThe word you need to guess contains {number_of_char} characters!")
    print("Try to guess the characters of the word before the Hangman Dies!!\n")
    print(blankword + "\n")
    
    while lifecounter < 7:
        if blankword.lower() == ((randomword) + '.'):
            print("\nCongrats! You've saved the Hangman!")
            print(f"\nCreated by \n{abdessamad}")
            break
        user_char_choice = input("")
        user_char_choice = user_char_choice.lower()
        if user_char_choice in randomwordlist:
            indexation = index(user_char_choice, randomwordlist)
            for i in range(len(indexation)):
                blankwordlist[indexation[i]] = user_char_choice
            blankword = "".join(blankwordlist)
            blankword = blankword.capitalize()
            print(blankword)
        elif user_char_choice not in randomwordlist:
            if lifecounter >= 6:
                print(hangman_cicle[6])
                print("The Hangman died! Shame on you")
                break
            else:
                print(hangman_cicle[lifecounter + 1])
                print("Careful! The Hangman is dying!")
                lifecounter += 1
    try_again = input("\nPress 'y' to play again.\nPress 'q' to quit.\n")



