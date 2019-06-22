import os
class Menu:
    open = False
    def run(self):
        self.open = True
        while (self.open):
            os.system('clear')
            print '''
            1- Start
            2- Exit
            '''
            option = raw_input()
            
            if(option == '1'):
                self.open = True
            elif (option == '2'):
                self.open = False
        