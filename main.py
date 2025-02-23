from DeckOfCards import DeckOfCards
import pickle
import tkinter as tk


Deck=DeckOfCards()
Check=0
file_exist=False
confirm_exit=False
filename_standard="my_hand.pkl"
total_score=0

print('')
print('Welcome to this cardgame!')
print('The rules are as follow:')
print('1. You want to get as many points as possible.')
print('2. The number value of the cards are added up, ace is 1 point, king is 13 points.')
print('3. If any of your cards are of the heart suit you get 5 points extra')
print('4. A full flush of a suit will give you 50 points extra')
print('5. If you draw the queen of hearts, you immediately loose all points and have to start over.')
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


#Function to display the hand of cards graphically
def display_hand(hand):
    #Arguments:
        #hand: The HandOfCards object to be displayed
    root = tk.Tk()
    root.title("Your Hand")
    for i, card in enumerate(hand.cards):
        filename = f"CardImages/{card.get_as_string()}.gif"       
        try:
            photo = tk.PhotoImage(file=filename)
            photo=photo.subsample(2)
            label = tk.Label(root, image=photo)
            label.image = photo 
            label.grid(row=0, column=i)
        except tk.TclError:
            print(f"Image not found or unsupported format: {filename}")
    root.mainloop()


#Function to count points
def count_points(Hand):
    global total_score
    Count=Hand.count_points()
    total_score=total_score+Count
    Flush=Hand.is_flush()
    if Flush==True:
        total_score=total_score+50
    else:
        pass
    Hearts=Hand.is_hearts()
    if Hearts == False:
        pass
    else:
        total_score=total_score+5
    Ladyspade=Hand.is_ladyspade()
    if Ladyspade == True:            
        total_score=0
    else:
        pass


#The menu function for the game
def menu():   
    global Check 
    global confirm_exit
    global file_exist
    global total_score
    while True:
        if confirm_exit==True:
            break
        else:
            pass
        print('')
        print('Choose an option from the menu by entering a number:')
        print('1: Deal a new hand of cards')
        print('2: See the total score and my current hand of cards')
        print('3: Check my hand for a flush')
        print('4: Save your hand of cards to a file')
        print('5: Upload a hand of cards from a file')
        print('6: Exit the game')
        x=input('I want to: ')
        print('')

        # User input for dealing a hand of cards
        if x == '1':
            Hand=Deck.deal_hand(5)
            print(Hand)
            Check=1
            count_points(Hand)

        # User input for seeing the cards in the players hand
        elif x == '2':
            if Check==0:
                print("You haven't dealt a hand yet!")
            else:
                print('Your score is ', total_score)
                print('Remember to close the display window to coninue the game!')
                display_hand(Hand)


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
                    choose_filename=input("Do you want to use the standard savefile (yes) or write a filename you have created (no)?")
                    if choose_filename.lower()=="yes":
                        filename = filename_standard
                        Hand = load_hand(filename)
                        count_points(Hand)
                        break
                    elif choose_filename.lower()=="no":
                        filename_input = input("Write the filename you wish to load from (without extensions):")
                        filename=filename_input+".pkl"
                        Hand = load_hand(filename)
                        count_points(Hand)
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