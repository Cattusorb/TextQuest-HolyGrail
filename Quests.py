# Roslyn Parker
# Start Date: 4 Nov. 2019
# End Date: 

# The file contains the quests 
# (as classes) for the main
# Holy Grail Search game

class BlackKnight:
    status = ""
    success = False
    player_strength = 0
    
    def __init__(self, player): 
        '''
            Documentation 
        '''
        self.status = "incomplete"
        self.success = False
        self.player_strength = player.get_strength()
        
class FlyingAnimals: 

