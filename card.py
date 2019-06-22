#from termcolor import colored
class Card:
    value = ''
    color = ''
    type = '' 
    def __init__(self, value, color, type):
        self.value = value
        self.color = color
        self.type = type
    
    @property
    def checkOverCard(self):
        return True