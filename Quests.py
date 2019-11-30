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
        if lc: 
            print(f"{player.name} has won the fight! Bravo!")
        else: 
            print(f"{player.name} has been defeated by the Black Knight...")
            player.health = player.health - 2
            print(f"You loose two health.")
            
    
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
        print(f"\n{player_name}, you need to roll 6-sided dice to see if you")
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
                time.sleep(2)
                exit()
            else: 
                print("Invalid Input")
                
class God(Quest): 

    def __init__(self, player): 
        '''
            Constructor function for God class.
            Calls the super class constructor.
        '''
        Quest.__init__(self, player)
        self.dialog(player.name)
        quest = self.question()
        if quest:
            pass
        else: 
            exit()
    
    #Overriding abstract method
    def dialog(self, player_name):
        print(f"\n{player_name} continues riding towards Camelot.")
        print("After a while of riding you see God!")
        print("God shows you the a beautiful image and says,")
        print(f"\t'{player_name}, this is the Holy Grail. Look well,")
        print(f"\t {player_name}, for it is your sacred task to seek")
        print(f"\t this grail. That is your purpose: the quest for the Holy Grail'")
        time.sleep(20)
        
    def question(player_name): 
        '''
            The question of the quest for the Holy Grail answered!
        '''
        while(True):
            try: 
                print(f"Do you:\n\t1) Accept the Quest\n\t2) Go to Camelot to get drunk")
                answer = int(input("Answer:"))
            
                while(True): 
                    if answer in range(1, 3):
                        if answer == 1: 
                            print("Sir valiant knight, you have accepted the quest! Continue on!")
                            return True
                        elif answer == 2: 
                            print("You have denied your quest... Game Over...")
                            return False
            except: 
                print("Invalid Input.")
                
class FlyingAnimals(Quest):

    def __init__(self, player): 
        '''
            Constructor function for Flying Animals class.
            Calls the super class constructor.
        '''
        Quest.__init__(self, player)
        self.dialog(player.name)
        fa = self.fly_minigame(player)
        if fa: 
            print("You have successfully passed the flying animals.")
            print("You run away into the forest.")
        else: 
            print(f"{player.name} you have died.")
            print("Game Over...")
            time.sleep(4)
            exit()
        
    def dialog(self, player_name):
        print("\nYou see a few guards sitting at the top of a castle and you ask")
        print("for them to tell their master if you can have")
        print("food and shelter for the night. You tell them he can")
        print("join you in your quest for the Holy Grail.")
        time.sleep(15)
        print(f"\tFrench Guard: 'Well, I'll ask him, but I don't think he'll be")
        print(f"\t\tvery keen. He's already got one, you see.")
        time.sleep(8)
        print(f"\t{player_name}: 'What?'")
        time.sleep(2)
        print(f"\tFrench Guard: 'He says they've already got one!'")
        time.sleep(3)
        print(f"\t{player_name}: 'Are you sure he's got one?'")
        time.sleep(3)
        print(f"\tFrench Guard: 'Oh, yes. It's very nice-a.'")
        time.sleep(2)
        print(f"\t{player_name}: 'Can we come up and have a look?'")
        time.sleep(3)
        print(f"\tFrench Guard: 'Of course not! Mind your own business!'")
        time.sleep(3)
        print(f"\t{player_name}: 'If you won't show me, then I shall take")
        print(f"\t\tyour castle by force!'")
        time.sleep(6)
        print(f"\tFrench Guard: 'You don't frighten us! I fart in your general")
        print(f"\t\tdirection!'")
        time.sleep(6)
        print("The French Guards start to get angry at you and start throwing")
        print("random animals at you!")
    
    def fly_minigame(self, player):
        '''
            Dodge the animals to win the game. If you 
            get hit, you lose one health. 
        '''
        print(f"\n{player.name}, you need to dodge the animals that come flying")
        print("at you in order to win. You will lose 1 health for each animal")
        print("that hits you.")
        animals = 5
        while(True):
            try:
                if player.health <= 0: 
                    return False
                if animals <= 0: 
                    return True
                    
                d = input("Type 'd' to dodge or 'q' to quit:")
                if d == "d":
                    animals = animals - 1
                    dice_roll = Quest.roll6(self)
                    if (player.wits + dice_roll) >= 10:
                        print("Successfully dodged an animal!")
                    else:
                        print("You got hit with a flying animal!")
                        player.health = player.health - 1
                        print(f"Health: {player.health}.")
                elif d == "q": 
                    return False
                else: 
                    print("Invalid Input.")
            except:
                print("Invalid Input.")


class GiantRabbit(Quest):

    def __init__(self, player): 
        '''
            Constructor function for Giant Rabbit class.
            Calls the super class constructor.
        '''
        Quest.__init__(self, player)
        self.dialog(player.name)
        
    def dialog(self, player_name): 
        print(f"\nOh brave knight, the night is closing in on you and you")
        print(f"need a place to stay.\nDo you:\n\t1) Build a decoy rabbit")
        print(f"\t2) Go back to the castle and fight")
        print(f"\t3) Turn around and go to the next quest")
        aq = self.answer_question()
        if aq:
            pass
        else:
            exit()
    
    def answer_question(self):
        '''
            Method to answer the question 
            from the dialog method
        '''
        while(True):
            try: 
                answer = int(input("Answer: "))
                if answer in range(1, 4):
                    if answer == 1:
                        print(f"\nYou have chosen to build a decoy rabbit to infiltrate")
                        print(f"the castle but on execution of this plan, you forget to ")
                        print(f"hop in the rabbit... Continue onward.")
                        return True
                    elif answer == 2:
                        print(f"\nYou have chosen to go back to the castle and fight!")
                        print(f"This has led you to your death via Giant Rabbit!")
                        print("Game Over...")
                        time.sleep(3)
                        return False
                    elif answer == 3:
                        print(f"\nYou have decided to turn around and go to your next quest.")
                        print("Good choice, carry on.")
                        return True
                else:
                    print("Invalid Input.")
            except: 
                print("Invalid Input.")
        
    

class EnchanterTim(Quest):

    def __init__(self, player): 
        '''
            Constructor function for Enchanter Tim class.
            Calls the super class constructor.
        '''
        Quest.__init__(self, player)
        self.dialog(player.name)
        fa = self.fly_minigame(player.name)
        
    def dialog(self, player_name):   
        pass

class CaveRabbit(Quest):

    def __init__(self, player): 
        '''
            Constructor function for Cave Rabbit class.
            Calls the super class constructor.
        '''
        Quest.__init__(self, player)
        self.dialog(player.name)
        
    def dialog(self, player_name):  
        pass

class TheCave(Quest):

    def __init__(self, player): 
        '''
            Constructor function for The Cave class.
            Calls the super class constructor.
        '''
        Quest.__init__(self, player)
        self.dialog(player.name)
        
    def dialog(self, player_name): 
        pass

class BridgeOfDeath(Quest):

    def __init__(self, player): 
        '''
            Constructor function for Bridge of Death class.
            Calls the super class constructor.
        '''
        Quest.__init__(self, player)
        self.dialog(player.name)
        
    def dialog(self, player_name):    
        pass
    
class CastleOfAargh(Quest):

    def __init__(self, player): 
        '''
            Constructor function for Castle of Aargh class.
            Calls the super class constructor.
        '''
        Quest.__init__(self, player)
        self.dialog(player.name)
        
    def dialog(self, player_name):
        pass