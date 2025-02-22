from DeckOfCards import DeckOfCards
import pickle

Deck=DeckOfCards()
Check=0
confirm_exit=False

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
        #hand: TenHadOfCards object to be saved
        #filmename (str): The name of the save file
    with open(filename, 'wb') as file:
        pickle.dump(hand, file)
    print(f"Hand saved to {filename}")

def menu():   
    global Check 
    global confirm_exit
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
 
 
        elif x == '4':
            pass
 
 
        elif x == '5':
            pass


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
            print('That is not a valid option, please choose again:')

menu()



