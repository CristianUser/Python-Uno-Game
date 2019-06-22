class Player:
    name = ''
    id = ''
    cards = []
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
        return valueToSend
    
    def getCards(self):
        return self.cards

    def setCards(self, cards):
        self.cards = cards
    
    def drawCards(self):
        array = []
        for val in self.cards:
            val.printCard()
    def getCardsCount(self):
        return len(self.cards)
