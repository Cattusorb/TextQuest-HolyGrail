# Roslyn Parker
# Start Date: 4 Nov. 2019
# End Date: 

# The file contains the abstract 
# quest template class for 
# TextQuest-HolyGrail game

import random

class Quest: 
    def __init__(self, player):
        self.player = player
        self.isComplete = False
        self.isSuccess = False
        
    def dialog(self):
        '''
            Abstract Method
            Character dialog for each quest, quest specific
        '''
        pass
    
    def play_quest(self):
        ''' 
            Abstract Method
            Play the quest through returns isComplete True 
        '''
        pass
        
    def roll6(self):
        '''
            Rolls a 6 sided dice and returns the roll
        '''
        return random.randint(1, 7)
        
    def roll20(self):
        '''
            Rolls a 20 sided dice and returns the roll
        '''
        return random.randint(1, 21)

