#from termcolor import colored
from colorama import init, Fore, Back, Style
init()

def cprint(msg, foreground = "black", background = "white"):
    fground = foreground.upper()
    bground = background.upper()
    style = getattr(Fore, fground) + getattr(Back, bground)
    print(style + msg + Style.RESET_ALL)

# cprint("colorful output, wohoo", "red", "black")
class Card:
    value = ''
    color = ''
    type = '' 
    def __init__(self, value, color, type):
        self.value = value
        self.color = color
        self.type = type
    
    def canPutItOverMe(self, card):
        if(card.color == self.color or card.value == self.value or card.type == 'add4'):
            return True
        return False
    
    def printCard(self):
        color = self.color.upper()
        style = getattr(Fore, 'WHITE') + getattr(Back, color)
        print style + '|',self.value,'|' + Style.RESET_ALL,
    
    def setColor(self, color):
        self.color = color