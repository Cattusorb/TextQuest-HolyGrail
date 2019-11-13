# Roslyn Parker
# Start Date: 13 Nov. 2019
# End Date:

import Player 

class Quest:
	'''
		This is an abstract class for building quests
	'''
	
	    def __init__(self, player): 
        '''
            Constructor for abstract class 
        '''
        self.isComplete = False
        self.success = False
		self.player = player
		
		
		def get_isComplete(self):
			''' 
			Method to get the isComplete status of the quest
			if the quest has been completed or not
			'''
			return self.isComplete
			
		def get_success(self):
			''' 
			Method to get the success of the quest
			if the quest was a success or failure
			'''		
			return self.success
			
		def set_isComplete(self, isComplete):
			''' 
			Method to set the isComplete status of the quest
			if the quest has been completed or not
			'''
			
			#implement code to check inputs
			
			return self.isComplete
			
		def set_success(self, success):
			''' 
			Method to set the success of the quest
			if the quest was a success or failure
			'''		
			
			#implement code to check inputs
			
			self.success = success
		
		def quest_dialog(self):
			'''
				Abstract method for quest-specific dialog
			'''
			pass
			
		def 