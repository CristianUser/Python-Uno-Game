import os
import time
from player import Player
from cardSet import CardSet
from card import Card

class Game:
    players = []
    cards = CardSet()
    cardsPlayed = []
    actualPlayer = 0
    direction = 1

    def __init__(self):
        self.menu()

    def reverseDir(self, val):
        self.direction = val * -1
        return self.direction

    def executeSpecialCard(self, action):
        if(action == 'add4'):
            self.printMessage('Plus Four JAJAJAXDXD!')
            for i in range (0, 4):
                self.players[self.nextPlayer()].addCard(self.cards.extractOne())
        elif(action == 'add2'):
            self.printMessage('Plus Two JAJAJAXDXD!')
            for i in range (0,2):
                self.players[self.nextPlayer()].addCard(self.cards.extractOne())
        elif(action == 'reverse'):
            self.printMessage('game reversed!')
            self.reverseDir(self.direction)


    def nextPlayer(self):
        value = self.actualPlayer
        value += self.direction
        if (value > len(self.players)-1):
            value = 0
        return value

    def canPlay(self, player):
        for card in player.getCards():
            if(self.cardsPlayed[-1].canPutItOverMe(card)):
                return True
        return False

    def playing(self):
        self.actualPlayer = 0    
        while True:
            while (self.canPlay(self.players[self.actualPlayer])):# verify if the player can play
                os.system('clear')
                print 'Actual Player is: ' + self.players[self.actualPlayer].name # print the actual player
                print 'remaining cards: ' + str(self.cards.getCount()) # remaining cards on lobby
                print self.cardsPlayed[-1].printCard()
                print len(self.cardsPlayed)
                print '\n'
                self.players[self.actualPlayer].drawCards()
                posToPlay = input('Card to Throw: ') # input to play
                if(self.cardsPlayed[-1].canPutItOverMe(self.players[self.actualPlayer].getOne(posToPlay))): # verify if the player select the correct one
                    if(self.players[self.actualPlayer].getOne(posToPlay).type!= 'number'):
                        self.executeSpecialCard(self.players[self.actualPlayer].getOne(posToPlay).type) # executes the specials cards to the next player
                    self.cardsPlayed.append(self.players[self.actualPlayer].extractOne(posToPlay))
                    break
            self.actualPlayer += self.direction
            if (self.actualPlayer > len(self.players)-1):
                self.actualPlayer = 0
        
    def startGame(self):
        numPlayers = input('How many players gonna play?\n')
        for i in range(0, numPlayers):
            cardsToPlayer = []
            for j in range(7):
                cardsToPlayer.append(self.cards.extractOne())
            self.players.append(Player('player ' + str(i+1), i+1, cardsToPlayer))
        self.cardsPlayed.append(self.cards.extractOne())
        self.playing()
        input()
        
    def printMessage(self, msg, seconds = 2):
        os.system('clear')
        print '''
        ***************************************
                               
        ''' + msg + '''

        ***************************************
        '''
        time.sleep(seconds)
        os.system('clear')
    def menu(self):
        option = ''
        while (option !='2'):
            os.system('clear')
            print '''
            1- Start
            2- Exit
            '''
            option = raw_input()
            
            if(option == '1'):
                self.startGame()
                self.menu()
            elif (option == '2'):
                print 'Good Bye'
game = Game()