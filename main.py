from DeckOfCards import DeckOfCards
import pickle

Deck=DeckOfCards()
Check=0
file_exist=False
confirm_exit=False
filename_standard="my_hand.pkl"

print('')
print('Welcome to this cardgame!')
print('The rules are as follow:')
print('Rule 1[...]')
print('')
print('Good luck!')
print('')


#Function to save a hand of cards to a file for later use
def save_hand(hand, filename):
    #Arguments:
        #hand: HandOfCards object to be saved
        #filename (str): The name of the save file
    with open(filename, 'wb') as file:
        pickle.dump(hand, file)
    print(f"Hand saved to {filename}")


#Function to load a hand of cards from a file
def load_hand(filename):
    #Arguments:
        #filename (str): The name of the savefile
    try:
        with open(filename, 'rb') as file:
            hand = pickle.load(file)
        print(f"Hand loaded from {filename}")
        return hand
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except pickle.PickleError:
        print(f"Could not read the file {filename}. The file might be corrupted")
    return None


#The menu function for the game
def menu():   
    global Check 
    global confirm_exit
    global file_exist
    while True:
        if confirm_exit==True:
            break
        else:
            pass
        print('')
        print('Choose an option from the menu by entering a number:')
        print('1: Deal a new hand of cards')
        print('2: See the cards I currently have')
        print('3: Check for a flush')
        print('4: Save you hand of cards to a file')
        print('5: Upload a hand of cards from a file')
        print('6: Exit the game')
        x=input('I want to: ')
        print('')

        # User input for dealing a hand of cards
        if x == '1':
            Hand=Deck.deal_hand(5)
            print(Hand)
            Check=1

        # User input for seeing the cards in the players hand
        elif x == '2':
            if Check==0:
                print("You haven't dealt a hand yet!")
            else:
                print(Hand)

        # User input for checking the users hand for points and other things
        elif x == '3':
            if Check==0:
                print("You haven't dealt a hand yet!")
            else:
                Flush=Hand.is_flush()
                if Flush==True:
                    print("Congraulations! It's a flush!")
                else:
                    print("Unfortunately it's not a flush :(")
                Hearts=Hand.is_hearts()
                if Hearts == False:
                    print("No hearts for you I'm afraid :(")
                else:
                    print("These are the cards of the Heart suit: ", Hearts)
                Count=Hand.count_points()
                print("This is the number value of your cards all together: ", Count)
                Ladyspade=Hand.is_ladyspade()
                if Ladyspade == True:
                    print("Gasp! You have the Queen of spades!")
                else:
                    print('No Queen of spades for you!')
 
        #User input for saving a dealt hand of cards
        elif x == '4':
            if Check==0:
                print("You haven't dealt a hand yet!")
            else:
                while True:
                    choose_filename=input("Do you want to use the standard savefile (yes) or write a filename to save to (no)?")
                    if choose_filename.lower()=="yes":
                        filename = filename_standard
                        save_hand(Hand, filename)
                        file_exist=True
                        break
                    elif choose_filename.lower()=="no":
                        filename_input = input("Write a filename to save the hand to:")
                        filename=filename_input+".pkl"
                        save_hand(Hand, filename)
                        file_exist=True
                        break  
                    else: 
                        print('That is not a valid option, please type yes or no!')                      

        #User input for loading a saved hand of cards
        elif x == '5':
            if file_exist==False:
                print('You have not yet saved a hand to load!')
            else:
                while True:
                    choose_filename.lower()=input("Do you want to use the standard savefile (yes) or write a filename you have created (no)?")
                    if choose_filename=="yes":
                        filename = filename_standard
                        Hand = load_hand(filename)
                        break
                    elif choose_filename.lower()=="no":
                        filename_input = input("Write the filename you wish to load from (without extensions):")
                        filename=filename_input+".pkl"
                        Hand = load_hand(filename)
                        break
                    else:
                        print('That is not a valid option, please type yes or no!') 

        #User input for ending the function
        elif x == '6':
            while True:
                answer=input("Are you sure? (yes/no)")
                if answer.lower() == "yes":
                    print('')
                    print('Thank you for playing my card game!')
                    print('')
                    confirm_exit=True
                    break
                elif answer == "no":
                    break
                else:
                    print('That is not a valid option, please type yes or no!')
        else:
            print('That is not a valid option, please write yes or no!')

menu()



