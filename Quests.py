# Roslyn Parker
# Start Date: 25 Nov. 2019
# End Date:

# This file contains the classes
# for each quest in the 
# game TextQuest-HolyGrail

from Quest import Quest

class BlackKnight(Quest):
    def __init__(self, player):
        Quest.__init__(self, player)
        self.limbs = 4
    
    