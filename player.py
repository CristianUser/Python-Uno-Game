from colorama import init, Fore, Back, Style
init()

class Player:
    name = ''
    id = ''
    cards = []
    colors = [
        'red',
        'green',
        'blue',
        'yellow'
    ]
    def __init__(self, name, id, cards):
        self.name = name
        self.id = id
        self.cards = cards
    
    def addCard(self, card):
        self.cards.append(card)

    def getOne(self, pos):
        return self.cards[pos]
    
    def extractOne(self, pos):
        valueToSend = self.cards[pos]
        self.cards = self.cards[:pos] + self.cards[pos+1:]
        if(valueToSend.type == 'add4'):
            for val in self.colors:
                color = val.upper()
                style = getattr(Fore, 'WHITE') + getattr(Back, color)
                print style + '| |' + Style.RESET_ALL,
            pos = input('Select color')
            valueToSend.setColor(self.colors[pos])
        return valueToSend
    
    def getCards(self):
        return self.cards

    def setCards(self, cards):
        self.cards = cards
    
    def drawCards(self):
        array = []
        for val in self.cards:
            val.printCard()
        print ''
        for i in range(len(self.cards)):
            print ' ', str(i), ' ',
    def getCardsCount(self):
        return len(self.cards)
