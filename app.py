import os
from player import Player
players = []

def startGame():
    numPlayers = input('How many players gonna play?')
    for i in range(0, numPlayers):
        players.append(Player(raw_input('The Name'), i+1, []))

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