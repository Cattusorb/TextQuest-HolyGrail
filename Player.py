# Roslyn Parker
# Start Date: 13 Nov. 2019
# End Date:

class Player:
	def __init__(self, name):
    '''
        Constructor for class sets specific 
        characteristics for a given character
    '''
    if name == "King Arthur":
	self.name = name
	self.strength = 8
	self.health = 6
	self.wits = 8
    elif name == "Sir Lancelot":
	self.name = name
	self.strength = 10
	self.health = 7
	self.wits = 5
    elif name == "Sir Bedivere": 
	self.name = name
	self.strength = 5
	self.health = 7
	self.wits = 6
    elif name == "Sir Robin":
	self.name = name
	self.strength = 4
	self.health = 5
	self.wits = 8
    elif name == "Sir Galahad":
	self.name = name
	self.strength = 8
	self.health = 5
	self.wits = 4
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

    def set_strength(self, value): 
        '''
            Sets strength of character to given value
        '''
	if value < 0:
		self.strength = 0
	elif value > 10: 
		self.strength = 10
        else: 
		self.strength = value
    
    def set_health(self, value):
        '''
            Sets health of character to given value
        '''
        if value < 0:
		self.health = 0
	elif value > 10: 
		self.health = 10
        else: 
		self.health = value
        
    def set_wits(self, value):
        '''
            Sets wits of character to given value
        '''
        if value < 0:
		self.wits = 0
	elif value > 10: 
		self.wits = 10
        else: 
		self.wits = value
