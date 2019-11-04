# Roslyn Parker
# Start Date: 4 Nov. 2019
# End Date: 

# This file contains the characters 
# of this game they each have 
# unique characteristics that 
# make them who they are

class Player: 
    name = ""
    strength = 0
    health = 0
    wits = 0
 
    def __init__(self, name):
        '''
            Constructor for class sets specific 
            characteristics for a given character
        '''
        if name == "King Arthur":
        elif name == "Sir Lancelot":
        elif name == "Sir Bedivere": 
        elif name == "Sir Robin":
        elif name == "Sir Galahad":
        elif name == "Sir Not Appearing in this Game": 
            self.name = "End"
        else: 
            self.name = "End"
      
    def get_strength(self): 
        '''
            Returns strength of character
        '''
        return self.strength
    
    def get_health(self):
        '''
            Returns health of character
        '''
        return self.health
        
    def get_wits(self):
        '''
            Returns wits of character 
        '''
        return self.wits
        
    
    