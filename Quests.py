# Roslyn Parker
# Start Date: 25 Nov. 2019
# End Date:

# This file contains the classes
# for each quest in the 
# game TextQuest-HolyGrail

from Quest import Quest
import time

class BlackKnight(Quest):
    def __init__(self, player):
        '''
            Constructor function for Black Knight class.
            Calls the super class constructor and sets 
            the limbs left to chop off!
        '''
        Quest.__init__(self, player)
        self.limbs = 4
        self.dialog(player.name)
        lc = self.limb_chop(player.name, player.strength)
    
    #Overriding abstract method
    def dialog(self, player_name):
        bn = "Black Knight"
        print(f"\t{bn}: 'None shall pass.'")
        time.sleep(2)
        print(f"\t{player_name}: 'What? I have no quarrel with you, good Sir Knight,")
        print(f"\tbut I must cross this bridge.'")
        time.sleep(5)
        print(f"\t{bn}: 'Then you shall die. I move for no man.'\n")
        time.sleep(2)
        
    def limb_chop(self, player_name, player_strength):
        '''
            Limb chop game. If you chop of 3 out of 4 of the
            Black Knight's limbs then you win the game.
            If the you strength plus the dice roll is greater
            than or equal to 10 then you chop off the limb!
        '''
        print(f"{player_name}, you need to roll 6-sided dice to see if you")
        print("can chop off each of the Black Knight's four limbs. If you chop")
        print("off at least 3 of his 4 limbs, you win!")
        roll_count = 0
        while(True):
            if self.limbs <= 1: 
                print(f"\tBlack Knight: 'Oh? All right, we'll call it a draw.'")
                return True
            if roll_count > 4 and self.limbs > 1:
                print("\nYou are out of rolls.\nThe Black Knight has defeated you.")
                return False
                
            player_roll = input("\nType 'roll' to roll the dice of 'q' to quit: ")
            
            if player_roll.upper() == "ROLL":
                dice_roll = Quest.roll6(self)
                roll_count = roll_count + 1
                print(f"\n{player_name}, you rolled {dice_roll}!")
                print(f"Strength {player_strength} + Dice roll {dice_roll}")
                if dice_roll + player_strength >= 10:
                    self.limbs = self.limbs - 1
                    print("\nLimbs successfully chopped off! Aah!")
                    print(f"\tBlack Knight: 'Tis but a flesh wound!'")
                else: 
                    print("\nYou missed! Roll again!")
            elif player_roll.upper() == "Q":
                print("\nYou run away from the fight and fail your quest.")
                print("The Black Knight chases you and kills you!")
                print("Game Over...")
                exit()
            else: 
                print("Invalid Input")
        