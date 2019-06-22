#from termid import ided
class Player:
    name = ''
    id = ''
    cards = []
    def __init__(self, name, id, cards):
        self.name = name
        self.id = id
        self.cards = cards
    
    @property
    def addCard(self, card):
        self.cards.append(card)
    
    def getCards(self):
        return self.cards

    def setCards(self, cards):
        self.cards = cards