from card import Card
import random
class CardSet:
    cards = []
    colors = [
        'red',
        'green',
        'blue',
        'yellow'
    ]
    specials = [
        'add2',
        'add4',
        'reverse'
    ]
    def __init__(self):
        for i in range(0, 3):
            self.cards.append(Card('+4', 'black', 'add4'))
            self.cards.append(Card('+2', self.colors[i], 'add2'))
            self.cards.append(Card('+2', self.colors[i], 'add2'))
            self.cards.append(Card('&', self.colors[i], 'reverse'))
            self.cards.append(Card('&', self.colors[i], 'reverse'))
            for v in range(0, 9):
                self.cards.append(Card(v, self.colors[i], 'number'))
                if (v != 0):
                    self.cards.append(Card(v, self.colors[i], 'number'))
    
    def extractOne(self):
        pos = random.randrange(0, len(self.cards))
        valueToSend = self.cards[pos]
        self.cards = self.cards[:pos] + self.cards[pos+1:]
        return valueToSend
    
    def getAll(self):
        return self.cards

    def getCount(self):
        return len(self.cards)