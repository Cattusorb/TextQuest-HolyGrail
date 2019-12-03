# Roslyn Parker
# Start Date: 25 Nov. 2019
# End Date: 2 Dec. 2019

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
        print(f"\t{player_name}: 'What? I have no quarrel with you, good Sir Knight,")
        print(f"\tbut I must cross this bridge.'")
        print(f"\t{bn}: 'Then you shall die. I move for no man.'\n")

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
            time.sleep(3)
            exit()
        
    def dialog(self, player_name):
        print("\nYou see a few guards sitting at the top of a castle and you ask")
        print("for them to tell their master if you can have")
        print("food and shelter for the night. You tell them he can")
        print("join you in your quest for the Holy Grail.")
        print(f"\tFrench Guard: 'Well, I'll ask him, but I don't think he'll be")
        print(f"\t\tvery keen. He's already got one, you see.")
        print(f"\t{player_name}: 'What?'")
        print(f"\tFrench Guard: 'He says they've already got one!'")
        print(f"\t{player_name}: 'Are you sure he's got one?'")
        print(f"\tFrench Guard: 'Oh, yes. It's very nice-a.'")
        print(f"\t{player_name}: 'Can we come up and have a look?'")
        print(f"\tFrench Guard: 'Of course not! Mind your own business!'")
        print(f"\t{player_name}: 'If you won't show me, then I shall take")
        print(f"\t\tyour castle by force!'")
        print(f"\tFrench Guard: 'You don't frighten us! I fart in your general")
        print(f"\t\tdirection!'")
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
                        print(f"This has led you to your death via flying animals!")
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
        f = self.follow(player.name)
        if f:
            pass
        else:
            exit()
        
    def dialog(self, player_name):   
        print(f"\nAs you ride forward on your quest for the Holy Grail")
        print("an Enchanter by the name of Tim greets you as he shoots fireballs")
        print("on the mountians that surround you.")
        print(f"\tTim: 'Greetings, {player_name}!'")
        print(f"\t{player_name}: 'You know my name?'")
        print(f"\tTim: 'I do! You seek the Holy Grail!'")
        print(f"\t{player_name}: 'That is our quest. You know much that is hidden, O Tim.'")
        print(f"\nAs you continue talking with Tim, he informs you that he has")
        print("information for you regarding the Holy Grail you seek.")
        print(f"\tTim: 'To the North there lies a cave- the cave of Caerbannog-")
        print(f"\t\twherein, carved in mystic runes upon the very living rock, the")
        print(f"\t\tlast words of Olfin Bedwere of Rheged... make plain the last")
        print(f"\t\tresting place of the most Holy Grail.'")
        print(f"\t{player_name}: 'Where could we find this cave, O Tim?'")
        print(f"\tTim: 'Follow. Follow only if ye be men of valour, for the entrance")
        print(f"\t\tto this cave is guarded by a creature so foul, so cruel...")
        print(f"\t\tIf you doubt your courage or strength, come no further for death")
        print(f"\t\tawaits you all with nasty, big, pointy teeth.")
        print("\nTim starts to walk and show you to where the cave entrance is.")
     
    def follow(self, player_name):
        '''
            Decide whether or not you want to follow Tim.
        '''
        print(f"Do you:\n\t1) Follow Tim\n\t2) Run back to Camelot to get drunk")
        while(True):
            answer = input("Answer:")
            if answer == '1': 
                print(f"{player_name}, you have chosen to follow Tim to the cave.")
                return True
            elif answer == '2':
                print(f"{player_name}, you have chosen to go back to Camelot to get drunk.")
                print("Game Over...")
                time.sleep(3)
                return False
            else: 
                print("Invalid Input.")

class CaveRabbit(Quest):

    def __init__(self, player): 
        '''
            Constructor function for Cave Rabbit class.
            Calls the super class constructor.
        '''
        Quest.__init__(self, player)
        self.dialog(player.name)
        r = self.rabbit(player)
        if r:
            pass
        else:
            time.sleep(3)
            exit()
        
    def dialog(self, player_name):  
        print(f"\n\tTim: 'Behold the cave of Caerbannog!'")
        print("\nAs you approach the cave along side Tim, you see a rabbit")
        print("sitting at the entrance to the cave.")
        print(f"\tTim: 'That's no ordinary rabbit! That's the most foul, cruel,")
        print(f"\t\tand bad-tempered rodent you ever set eyes on! That rabbit's got")
        print(f"\t\ta vicous streak a mile wide! It's a killer!")
        print(f"\t{player_name}: You motion for your servant to go to the rabbit, 'Go on,")
        print(f"\t\t chop his head off!")
        print(f"\tServant: 'Right! One rabbit stew comin' right up!'")
        print(f"\nAs the servant goes in to attack the rabbit it viciously attacks his")
        print("neck and he dies quickly! You are scared out of your armor and don't")
        print(f"know what to do.\n\tTim: 'Oh, it's just a harmless bunny isn't it?'")
        print(f"\t{player_name}: 'Oh shut up!'")
        print("\nYou have 4 options to defeat this rabbit.")
     
    def rabbit(self, player):
        '''
            Method to choose how to defeat the rabbit
        '''
        print(f"\nDo you:\n\t1) Try to chop off it's head")
        print(f"\t2) Run away\n\t3) Taunt it\n\t4) Use the Holy Hand Grenade")
        while(True):
            answer = input("Answer:")
            if answer == '1':
                print("You go to try and chop off it's head, but you end up like")
                print(f"your servant. You, {player.name}, die.")
                print("Game Over...")
                player.health = 0
                return False
            elif answer == '2':
                print("You have chosen to run away. In turn you fail your quest for")
                print("the Holy Grail. God sentences you to death.")
                print("Game Over...")
                player.health = 0
                return False
            elif answer == '3':
                print("Based on your wits and the roll of a 20 sided dice")
                print("The sum of those much be greater than or equal to 12 to taunt and")
                print("kill the rabbit.")
                dice_roll = Quest.roll20(self)
                print(f"You rolled {dice_roll} and you have {player.wits} wits.")
                if dice_roll + player.wits >= 12:
                    print("You have successfully taunted the rabbit, you go in to kill")
                    print("it and make a nice stew!\n+2 health\n+2 wits")
                    player.health = player.health + 2
                    player.wits = player.wits + 2
                    return True
                else: 
                    print("You lost the fight against the rabbit. You have died.")
                    print("Game Over...")
                    return False
            elif answer == '4':
                print("You have chosen to use the Holy Hand Grenade. You throw it at the")
                print("rabbit and it instantly kills him upon explosion! Good job!")
                return True
            else:
                print("Invalid Input.")

class TheCave(Quest):

    def __init__(self, player): 
        '''
            Constructor function for The Cave class.
            Calls the super class constructor.
        '''
        Quest.__init__(self, player)
        self.dialog(player.name)
        bb = self.black_beast(player)
        if bb:
            pass
        else:
            exit()
        
    def dialog(self, player_name): 
        print(f"\n{player_name}, you enter the cave with courage. As you")
        print("walk through the cave with your sword out, you come across")
        print("some writing on the wall. It reads: 'Here may be found the")
        print("last words of Joseph of Arimathea. He who is valiant and")
        print("pure of spirit may find the Holy Grail in the Castle of ")
        print("Aaaarrrrggghhh.' After reading this you ponder what it means")
        print(f"when suddenly the Legendary Back Beast appears!")

    def black_beast(self, player):
        '''
            What to do about the black beast
        '''
        print(f"\nDo you:\n\t1) Fight it\n\t2) Run!!!")
        while(True): 
            answer = input("Answer: ")
            if answer == '1':
                print("As you try to fight the beast, he opens his mouth wide")
                print("and eats you whole! You have died.")
                print("Game Over...")
                time.sleep(3)
                return False
            elif answer == '2':
                print("You have chosen to run as fast as you can! While you are")
                print("running away the moster magically disappears and you")
                print("are now safe... for now.")
                return True
            else:
                print("Invalid Input.")
    
class BridgeOfDeath(Quest):

    def __init__(self, player): 
        '''
            Constructor function for Bridge of Death class.
            Calls the super class constructor.
        '''
        Quest.__init__(self, player)
        self.dialog(player.name)
        bp = self.bridge_pass(player)
        if bp: 
            print("You have successfully passed the test, you cross the bridge!")
        else:
            print("You are flung to your doom! Game Over...")
            time.sleep(3)
            exit()
        
    def dialog(self, player_name):    
        print(f"\n{player_name}, you have arrived at the bridge of death!")
        print("You see a man guarding the bridge.")
        print(f"\tBridge Keeper: 'Stop! Who would cross the Bridge of Death")
        print(f"\t\tmust answer me these questions three, ere the other side")
        print(f"\t\the see'")
        print(f"\t{player_name}: 'Ask me the questions, bridgekeeper. I am")
        print(f"\t\tnot afraid.'")
    
    def bridge_pass(self, player):
        '''
            To pass the bridge the player must answer
            questions specific to their character
            if they guess wrong, they get thrown off the 
            bridge and fall to their doom!
        '''
        print(f"\n{player.name}, you must answer the 3 questions from the")
        print("bridgkeeper to get across the bridge to find the Holy Grail.")
        q1 = input("Question 1: What is your full name? ")
        name = player.name
        if name.lower() in q1.lower():
            print("Successfully passed the first question!")
        else: 
            print("Your answer is incorrect...")
            return False
        
        q2 = input("Question 2: What is your quest? ")
        answer1 = "holy grail"
        if answer1.lower() in q2:
            print("Successfully passed the second question!")
        else: 
            print("Your answer is incorrect...")
            return False
        
        if player.name == "King Arthur":
            print("What... is the air-speed velocity of an unladen")
            q3 = input("swallow:")
            answer3 = "african or european swallow?"
            if answer3 in q3.lower():
                print("Successfully passed the third question!")
                return True
            else:
                print("Your answer is incorrect...")
                return False
        elif player.name == "Sir Galahad":
            q3 = input("Question 3: What is your favorite color? ")
            answer3 = "yellow"
            if answer3 in q3.lower():
                print("Successfully passed the third question!")
                return True
            else:
                print("Your answer is incorrect...")
                return False
        elif player.name == "Sir Bedivere":
            q3 = input("Question 3: What is your favorite color? ")
            answer3 = "blue"
            if answer3 in q3.lower():
                print("Successfully passed the third question!")
                return True
            else:
                print("Your answer is incorrect...")
                return False
        elif player.name == "Sir Lancelot":
            q3 = input("Question 3: What is your favorite color? ")
            answer3 = "blue"
            if answer3 in q3.lower():
                print("Successfully passed the third question!")
                return True
            else:
                print("Your answer is incorrect...")
                return False
        else: # lines for Sir Robin
            q3 = input("Question 3: What... is the capital of Assyria? ")
            answer3 = "assur"
            if answer3 in q3.lower():
                print("Successfully passed the third question!")
                return True
            else:
                print("Your answer is incorrect...")
                return False
            
    
class CastleOfAargh(Quest):

    def __init__(self, player): 
        '''
            Constructor function for Castle of Aargh class.
            Calls the super class constructor.
        '''
        Quest.__init__(self, player)
        self.dialog(player.name)
        hg = self.holy_grail(player)
        if hg:
            time.sleep(3)
            pass
        else:
            time.sleep(3)
            exit()
        
    def dialog(self, player_name):
        print(f"{player_name}, you have arrived at your last destination!")
        print("The Castle of Aargh.")
        print(f"\t{player_name}: 'Our quest is at an end! God be praised!")
        print(f"\t\tAlmighty God, we thank Thee that Thou hast vouchsafed to us the most holy--")
        print(f"\t\tJesus Christ!'")
        print(f"\nA french man throws an object at you from the castle.")
        print(f"\tFrench Guard: 'Allo, {player_name}, who has the brain of a duck. So, we French")
        print(f"\t\tfellows outwit you a second time!'")
        print(f"\t{player_name}: 'If you do not open this door, we shall take this")
        print(f"\t\tcastle by force! In the name of God and the glory of our--")
        print("\nThe french man throws a pie at you twice! Then laughs at you.")
        print("The holy grail is in this castle and you need to defeat the french")
        print("guard in order to get it. An army comes from beyond the lands to assist you")
        print("in your quest for the Holy Grail!")
     
    def holy_grail(self, player):
        '''
            Final quest to achieve the holy grail
        '''
        fight = 0
        while(True):
            answer = input("Would you like to fight with 'strength' or 'wits'?: ")
            if answer == 'wits':
                fight = player.wits
                break
            elif answer == 'strength': 
                fight = player.strength
                break
            else: 
                print("Invalid Input.")
        
        print("\nYou must roll a 20-sided dice to decide your fate.")
        print("The sum of the roll plus your choice of fight will")
        print("determine the outcome. If you get greater than or equal to")
        print("15 from the sum you will defeat the french guards and achieve your quest!")
        while(True):
            answer = input("Type 'roll' to roll the dice: ")
            if answer.lower() == "roll":
                dice_roll = Quest.roll20(self)
                print(f"You rolled {dice_roll}. You have {fight} fight.")
                if dice_roll + fight >= 15:
                    print(f"\n{player.name}, you have defeated the french man and")
                    print("go into the castle. A beautiful object sits before you.")
                    time.sleep(2)
                    print("The Holy Grail.")
                    time.sleep(3)
                    print("You have completed your quest for the Holy Grail.")
                    time.sleep(3)
                    print("Thanks for playing!")
                    time.sleep(3)
                    print("Created by: Roslyn Parker VTC Class 2021")
                    return True
                else: 
                    print("\nYou have failed to defeat the french man, but the army of")
                    print("people come to your rescue! They hep you defeat the french man")
                    print("who will not taunt you a third time-a!")
                    print(f"\n{player.name}, you have defeated the french man and")
                    print("go into the castle. A beautiful object sits before you.")
                    time.sleep(2)
                    print("The Holy Grail.")
                    time.sleep(3)
                    print("You have completed your quest for the Holy Grail.")
                    time.sleep(3)
                    print("Thanks for playing!")
                    time.sleep(3)
                    print("Created by: Roslyn Parker, VTC Class 2021")
                    return True
                    
                    
                    