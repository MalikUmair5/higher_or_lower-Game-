#higher or lower

import random

SUIT_Tuple = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_Tuple = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8


# Pass in a deck and this function returns a random card from the deck

def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

# Pass in a deck and this function returns a shuffled copy of the deck  

def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut


print('Welcome to higher or Lower')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.') 
print('You have 50 points to start.') 
print()


startingDeckList = [] 

for suit in SUIT_Tuple:
    for thisValue, rank in enumerate(RANK_Tuple):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)
        
score = 50


while True: 
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('starding card is:', currentCardRank, 'of', currentCardSuit)
    print()
    
    for cardNumber in range(0, NCARDS): 
        answer = input(f'will the next card be higher or lower then the {currentCardRank} of {currentCardSuit}? (enter h or l)')
        answer = answer.casefold()
        
        nextCardDict = getCard(gameDeckList) 
        nextCardRank = nextCardDict['rank'] 
        nextCardSuit = nextCardDict['suit'] 
        nextCardValue = nextCardDict['value']
        
        print('Next card is:', nextCardRank + ' of ' + nextCardSuit) 
        
        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('you got it right it was higher')
                score = score + 20
            else:
                print('Sorry, it was not higher') 
                score = score - 15   
        elif answer == 'l': 
            if nextCardValue < currentCardValue: 
                score = score + 20 
                print('You got it right, it was lower') 
            else: 
                score = score - 15 
                print('Sorry, it was not lower') 

        print('Your score is:', score) 
        print()
        
        currentCardRank = nextCardRank 
        currentCardValue = nextCardValue  # don't need current suit 
    goAgain = input('To play again, press ENTER, or "q" to quit: ') 
        
    if goAgain == 'q': 
        break 
    print('OK bye')