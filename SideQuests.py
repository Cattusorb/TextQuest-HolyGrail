# Roslyn Parker
# Start Date: 30 Nov. 2019
# End Date:

# This file contains the classes
# for each side-quest in the 
# game TextQuest-HolyGrail

from Quest import Quest
import time

class KingArthur(Quest):
    def __init__(self, player): 
        '''
            Constructor function for side quest
            of Sir Robin
        '''
        Quest.__init__(self, player)
        self.dialog(player)
        
    def dialog(self, player):  
        print(f"\n{player.name}, an old man approaches you and give you a clue")
        print("to finding the Holy Grail. 'The bridge of death leads to the grail,'")
        print("he says in a quiet whisper.")
        print(f"\nYou forage on through the foggy forest and come accross a tall, ")
        print("dark knight about 4 feet taller than you. They greet you with:")
        print(f"\tKnight: 'We are the knights who say 'Ni'! '")
        print("You notice more of them standing behind the tall knight.")
        print(f"\tKnight: 'We demand a sacrifice or you must bring us a shrubbery!'")
        print(f"Do you:\n\t1) Sacrifice yourself\n\t2) Search for a Shrubbery")
        print(f"\t3) Try and fight\n\t4) Run away!")
        q1 = self.answer_question1(player)
        if q1:
            ss = self.shrub_search()
            if ss:
                print("The knights who say 'Ni' are pleased but they want another one!")
                
            else:
                print("You failed your quest... Game Over...")
                time.sleep(3)
                exit()
        else:
            time.sleep(3)
            exit()
        
    def answer_question1(self, player):
        '''
            Method to answer the question from 
            the dialog method.
        '''
        while(True):
            try: 
                answer = int(input("Answer: "))
                if answer in range(1, 5):
                    if answer == 1:
                        player.health = 0
                        print(f"{player.name}, you sacrifice yourself.")
                        print("Game Over...")
                        return False
                    elif answer == 2:
                        return True
                    elif answer == 3: 
                        print("You valiantly try to fight the knights who say 'Ni', but")
                        print("you are no match for them. You lose.")
                        print("Game Over...")
                        player.health = 0
                        return False
                    elif answer == 4:
                        print("In choosing to run away, you fail your search for the Holy Grail.")
                        print("Game Over...")
                        player.health = 0
                        return False
                else:
                    print("Invalid Input.")
            except: 
                print("Invalid Input.")
    def shrub_search(self):
        '''
            Search for a shurbbery, if you find one return True
            else return False
        '''
        print("You have chosen to search for the shubbery. At first,")
        print("you decide to babble with an old woman about buying a")
        print("shrubbery from her, but she will not bargin with you.")
        print("\nA man with a cart full of shrubberies rides up to you")
        print("and tells you he will give you a shrubbery for free!")
        print(f"Do you:\n\t1) Take the shubbery\n\t2) Don't take the shrubbery") 
          while(True):
            try: 
                answer = int(input("Answer: "))
                if answer in range(1, 3):
                    if answer == 1:
                        player.health = 0
                        print(f"You, {player.name}, decide to take the shrubbery back to")
                        print("the knights who say 'Ni'!")
                        return True
                    elif answer == 2:
                        return False
                else:
                    print("Invalid Input.")
            except: 
                print("Invalid Input.")
        
class SirGalahad(Quest):
    def __init__(self, player): 
        '''
            Constructor function for side quest
            of Sir Robin
        '''
        Quest.__init__(self, player)
        self.dialog(player)
        
    def dialog(self, player):  
        print(f"\n Thunder rolls in as you search for the grail. You get caught")
        print("in a rainstorm. In the distance you see a Holy Grail appear above")
        print("a castle. You are excited because you have found what you have been")
        print("searching for! You wander towards it and enter the castle. You are")
        print("greeted by a woman named Zute and tell her you are on a quest for")
        print("the Holy Grail. Zute asks, 'Would you like to stay the night?'")
        print(f"Do you:\n\t1) Refuse to stay\n\t2) Stay the night")
        self.answer_question(player)
        
    def answer_question(self, player):
        '''
            Method to answer the question from 
            the dialog method.
        '''
        while(True):
            try: 
                answer = int(input("Answer: "))
                if answer in range(1, 3):
                    if answer == 1:
                        print("You refused to stay the night and get kicked out of the castle.")
                        print("The rain outside is cold and you get a litte lost. Lose 2 health.")
                        player.health = player.health - 2
                        return
                    elif answer == 2:
                        print("You have chosen to stay the night and health is restored to 10.")
                        player.health = 10
                        self.crazy_ladies()
                        return
                        
                else:
                    print("Invalid Input.")
            except: 
                print("Invalid Input.")
                
    def crazy_ladies(self):
        '''
            The women of the castle of Anthrax go crazy with
            excitment and you don't know what to do! Lancelot
            and the other knights of the round table save you 
            from them and bring you to a warm place.
        '''
        print(f"\n The ladies of the Castle of Anthrax become crazed with you.")
        print("You don't know what to do and the women are crawling all over you.")
        print("Out of nowhere the knights of the round table grab you and save you")
        print("from the women and take you to a warm place. \nOnward...")
        
class SirLancelot(Quest):
    def __init__(self, player): 
        '''
            Constructor function for side quest
            of Sir Lancelot
        '''
        Quest.__init__(self, player)
        self.dialog(player)
        
    def dialog(self, player):  
        print(f"\n{player.name}, as valiant the knight you are, you wander off")
        print("to rescue a prince who does not want to get married. The prince")
        print("falls out of his bedroom window and seemingly falls to his death...")
        print("BUT! He survives thanks to your loyal servant Concord, sweet Concord.")
        

class SirRobin(Quest):
    def __init__(self, player): 
        '''
            Constructor function for side quest
            of Sir Robin
        '''
        Quest.__init__(self, player)
        self.dialog(player)
        
    def dialog(self, player):  
        print(f"\n{player.name}, you come wandering in the wood and see")
        print("three dead knights kabab'd on a lance. A three-headed knight")
        print("greets you with 'Hault!' Fear rushes through you but you gain")
        print(f"some confidence back.\n Do you:\n\t1) Run away")
        print(f"\t2) Listen to the three headed monster jabber")
        print(f"\t3) Roll to kill the knight with a fatal strike")
        self.answer_question(player)
        
    def answer_question(self, player):
        '''
            Method to answer the question from 
            the dialog method.
        '''
        while(True):
            try: 
                answer = int(input("Answer: "))
                if answer in range(1, 4):
                    if answer == 1:
                        print("You have chosen to run away to your next quest.")
                        return
                    elif answer == 2:
                        print("You continue listening and your next quest is delayed...")
                        print("Wait 10 seconds.")
                        time.sleep(10)
                        return
                    elif answer == 3:
                        print("You have chosen to roll a dice to decide your fate.")
                        dice_roll = Quest.roll20(self)
                        if player.strength + dice_roll >= 15:
                            print("You have killed the three headed knight with a fatal blow!")
                            print("+2 strength")
                            player.strength = player.strength + 2
                            return
                        else: 
                            print("Your strength and dice roll was not enough to kill the knight.")
                            print("You lose 2 health.")
                            player.health = player.health - 2
                            return
                        
                else:
                    print("Invalid Input.")
            except: 
                print("Invalid Input.")