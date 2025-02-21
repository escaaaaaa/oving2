from src.DeckOfCards import DeckOfCards

Deck=DeckOfCards()
Check=0

print('')
print('Welcome to this cardgame!')
print('The rules are as follow:')
print('Rule 1')
print('')
print('Good luck!')
print('')


def menu():   
    global Check 
    global Cards
    while True:
        print('')
        print('Choose an option from the menu by entering a number:')
        print('1: Deal a new hand of cards')
        print('2: See the cards I currently have')
        print('3: Check for a flush')
        print('4: Exit the game')
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
        #User input for ending the function
        elif x == '4':
            print('Thank you for playing my card game!')
            print('')
            break
        else:
            print('That is not a valid option, please choose again:')

menu()



