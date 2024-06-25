from random import randint
from textwrap import dedent

def read_file():
    # Open the file in read mode.
    with open('dictionary1.txt', 'r') as dict1:
        # Assign the file in to another variable to read every line.
        dict2 = dict1.readlines()
         # word.strip remove any leading or trailing white space.
        list_dict = [word.strip() for word in dict2]
    return list_dict

def dictionary(list_dict):
   
    # Randomly choose a number between 0 and length of list as index number.
    choose_word = list_dict[randint(0, len(list_dict) - 1)]
    # convert every choose in to upper case.
    return choose_word.upper()


def image(chance):
    # Images are included in a list so that the required image can be printed using index number.
    list_image = ["""
                 _______
                |      
                |      
                |     
                |         """, """
                _______
                |      |
                |      0
                |     /|\\
                |     / \\""", """
                _______
                |      |
                |      0
                |     /|\\
                |     /    """, """
                _______
                |      |
                |      0
                |     /|\\
                |         """, """
                _______
                |      |
                |      0
                |     /|
                |         """, """
                _______
                |      |
                |      0
                |      |
                |         """, """
                _______
                |      |
                |      0
                |     
                |         """, """
                _______
                |      |
                |      
                |   
                |         """]
    
    if chance == 7:
        print(list_image[0])
    elif chance == 6:
        print(list_image[-1])
    elif chance == 5:
        print(list_image[-2])
    elif chance == 4:
        print(list_image[5])
    elif chance == 3:
        print(list_image[4])
    elif chance == 2:
        print(list_image[3])
    elif chance == 1:
        print(list_image[2])
    elif chance == 0:
        print(list_image[1])
    else:
        print("Something went wrong")
        

def hang_man():
    # list_dict has a list of words
    list_dict = read_file()
    
    random_word = dictionary(list_dict)
    # Coverting the choosen word in to a list.
    random_word_list = list(random_word)
    # A list is made of '_' itrating in random_word_list
    mask_word_list = ['_' for item in random_word_list]
    print("Your masked word is here: ")
    # Covert the list of '_' in to a string.
    print(' '.join(mask_word_list))
    guessed_letters = []
    chance = 7

    while chance > 0 and '_' in mask_word_list:
        prompt2 = input("Please guess a letter: ")
        prompt2 = prompt2.upper()
        # Conditions given are the input should be a single letter and it should be an alphabet.
        if prompt2.isalpha() and len(prompt2) == 1:
            # Check whether the guessed letter is already guessed or not
            if prompt2 in guessed_letters:
                print("This letter is already guessed. Try another one.")
                
            elif prompt2 not in random_word_list:
                print("Sorry... Your guess is wrong...")
                # If guessed word is wrong, the chance is reduced by one.
                chance -= 1
                print("Chances left:", chance)
                # Every guessed letter is appended in to an empty list called guessed_letters.
                guessed_letters.append(prompt2)
                print("Guessed letters:", guessed_letters)
                print(' '.join(mask_word_list))
                image(chance)
            else:
                print("Hooray!! Your guess is right.")
                print("Chances left:", chance)
                guessed_letters.append(prompt2)
                # To get the index number of the letter in random_word_list.
                indices = [index for index, letter in enumerate(random_word_list) if letter == prompt2]
                for index in indices:
                    mask_word_list[index] = prompt2
                print(' '.join(mask_word_list))

        else:
            # If the prompted input is not an alphabet or multiple letters.
            print("Your guess is not valid.")
               

    if '_' not in mask_word_list:
        print(f"The word was: {random_word}")
        print("\nCongrats! You unmasked the word. You won!!!")
    else:
        
        print(f"The word was: {random_word}")
        print("\nYou ran out of chances. Sorry, You loose the game")

            
def start_game():
    print("Would you like to play a game? Y/N?")
    prompt = input("> ").lower()
    if prompt == "n":
        print("Ok, hope to see you later!")
        exit(0)
    elif prompt == "y":
        print("Welcome to Hangman out!")
        # Strips leading white spacefrom the begining of lines in astring.
        print(dedent("""
                    The game is between you and a goblin.
                    Goblin will give you a word which is masked.
                    You should guess the word by guessing one letter at a time.
                    You can make 7 mistakes. For every mistake you will be one step ahead of your death.
                    Finally after your 7th mistake you will be hanged by the goblin.
                    Goblin loves brilliant brains. If you win the game "The treasure" is yours! :-)
                    Do your level best!
                     """))
        print("Press ok to continue")
        
        prompt1 = input("> ").lower()
        if prompt1 == "ok":
            return hang_man()
        else:
            print("Let's end the game. Hope to see you next time...")
    else:
        print("Invalid input.")    


if __name__ == '__main__':
    start_game()