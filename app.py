import os
from player import Player
from cardSet import CardSet
from card import Card
players = []
cards = CardSet()
cardsPlayed = []
actualPlayer = 0
direction = 1

def executeSpecialCard(action):
    if('add2'):
        for i in range (2):
            players[nextPlayer()].addCard(cards.extractOne())
    elif('add4'):
        print 'add4'
        for i in range (4):
            players[nextPlayer()].addCard(cards.extractOne())
    elif('reverse'):
        direction *= -1


def nextPlayer():
    value = actualPlayer + direction
    if (value > len(players)-1):
        value = 0
    return value

def canPlay(player):
    for card in player.getCards():
        if(cardsPlayed[-1].canPutItOverMe(card)):
            return True
    return False

def playing():
    actualPlayer = 0    
    while True:
        while (canPlay(players[actualPlayer])):# verify if the player can play
            os.system('clear')
            print 'Actual Player is: ' + players[actualPlayer].name # print the actual player
            print cardsPlayed[-1].printCard()
            print '\n'
            print 'here 1'
            players[actualPlayer].drawCards()
            posToPlay = input('Card to Throw: ') # input to play
            if(cardsPlayed[-1].canPutItOverMe(players[actualPlayer].getOne(posToPlay))): # verify if the player select the correct one
                if(players[actualPlayer].getOne(posToPlay).type!= 'number'):
                    executeSpecialCard(players[actualPlayer].getOne(posToPlay).type) # executes the specials cards to the next player
                cardsPlayed.append(players[actualPlayer].extractOne(posToPlay))
                break
            actualPlayer = nextPlayer()
    
def startGame():
    numPlayers = input('How many players gonna play?\n')
    for i in range(0, numPlayers):
        cardsToPlayer = []
        for j in range(7):
            cardsToPlayer.append(cards.extractOne())
        players.append(Player('player ' + str(i+1), i+1, cardsToPlayer))
    cardsPlayed.append(cards.extractOne())
    playing()
    input()
    

def menu():
    option = ''
    while (option !='2'):
        os.system('clear')
        print '''
        1- Start
        2- Exit
        '''
        option = raw_input()
        
        if(option == '1'):
            startGame()
            menu()
        elif (option == '2'):
            print 'Good Bye'
menu()