# Roslyn Parker
# Start Date: 4 Nov. 2019
# End Date: 

# This file is the main program
# for the TextQuest-HolyGrail game

from Player import Player
from Quest import Quest
from Quests import * 
from SideQuests import * 
import time

def select_player():
    '''
        Returns the player's character selection choice
    '''
    player = Player("initial") # create initial player variable
    player_list = ["King Arthur", "Sir Galahad", "Sir Bedivere", "Sir Lancelot", "Sir Robin", "Sir Not Appearing in this Game"]
    
    while (True): 
        try: 
            player_pick = int(input("Input your selection 1-6: "))
                
            if player_pick <= 0 or player_pick >= 7: 
                # if the player_pick is outside the range of the list
                # tell them their pick is invalid and ask them to
                # choose another selection
                print("Invalid input.")
                
            # if the player_pick is in the range of choices
            if player_pick in range(1, 7): 
                # set the player to the player_pick - 1 
                # to get the right list element
                player = Player(player_list[player_pick - 1]) 
                return player
        except:
           print("Invalid input.")
    

def setup_character():
    '''
        Asks the user questions about which
        player they would like to be and 
        welcomes them to the game
    '''
    print("Welcome to TextQuest-HolyGrail!")
    print("Oh valiant player, which character would you like to play")
    print("for your quest today?")
    
    player_list = ["King Arthur", "Sir Galahad", "Sir Bedivere", "Sir Lancelot", "Sir Robin", "Sir Not Appearing in this Game"]
    i = 1
    
    # display player options
    for player in player_list:
        print(f"\t{i}) {player}")
        i+=1
    
    # get the character selection
    player = select_player()
    
    
    # if the player name = "End" ask the user
    # if they are sure they want to play that character
    while player.name == "End":
        answer = input("Are you sure you want to play this character? (Y/N) ")
        if answer.upper() == "Y": 
            print("Game Over...")
            return player
        if answer.upper() == "N":
            player = select_player()
    
    print("You have chosen:")
    player.display_player()
    return player
  
def swallow_chat():
    '''
        Answer question for swallow quest
    '''
    print(f"{character.name}, you are in England 932 AD. There is smoke surrounding you.")
    print(f"A castle comes into view as your servant clicks coconuts together pretending")
    print(f"he is your trusty-steed. A french man greets you vigorously at the castle as")
    print(f"you approach.")
    print(f"\tSoldier #1: 'Halt! Who goes there?'")
    print(f"\t{character.name}: 'It is I, {character.name}!'")
    print(f"\tSoldier #1: 'Pull the other one!'")
    print(f"\t{character.name}: You introduce your servant then say, 'I have come to join my fellow knights of Camelot.'")
    print(f"\tSoldier #1: 'What? Ridden on a horse? --those are just coconuts!'")
    print(f"\t{character.name}: 'What?'")
    print(f"\tSoldier #1: 'You've got two empty halves of coconut and you're bangin' 'em together.'")
    print(f"\t{character.name}: 'So? We have ridden since the snows of winter covered this land...'")
    print(f"\tSoldier #1: 'Where'd you get the coconuts?'")
    print(f"\t{character.name}: 'We found them.'")
    print(f"\tSoldier #1: 'Found them? in Mercia? The coconut's tropical! Are you suggesting coconuts migrate?'")
    print(f"\t{character.name}: 'Not at all. They could be carried.'")
    print(f"\tSoldier #1: 'What? A swallow carrying a coconut? It's a simple question of weight ratios!'")
    print(f"\t{character.name}: 'Well, it doesn't matter. Will you tell your master that {character.name}")
    print(f"\tis here from the Court of Camelot?'")
    print(f"\tSolier #1: 'Listen. In order to maintain the air-speed velocity a swallow needs...'")
    print(f"\t{character.name}: 'Please!'")
    print(f"\tSoldier #1: 'Am I right?'")
    print(f"\t{character.name}: 'I'm not interested!'")
    print(f"\tSoldier #2: 'It could be carried by an African Swallow!'")
    print(f"\nYou become frustrated with the chatter about swallow nonsense...")
    while(True):
        try: 
            answer = int(input(f"Do you: \n\t1) Walk away \n\t2) Continue listening \n\t3) Research swallows\nAnswer:"))
            if answer in range(1, 4): 
                return answer
            else: 
                print("Invalid Input")
        except:
            print("Invalid Input")
  
def check_health(player): 
    '''
        Checks the health of the player, if the player's 
        health is = 0 the game is over.
    '''
    exit = False
    try: 
        if player.health <= 0:
            print(f"{player.name} has no health left. Game over...")
            time.sleep(2)
            exit = True
        else: 
            player.display_player()
    except: 
        print("Invalid player.")
    
    if exit:
        exit()

def check_continue():
    '''
        Checks to see if the user wants to continue
        on to the next quest or quit the game
    '''
    print(f"\nWould you like to continue to the next task?")
    while(True):
        answer = input("Type 'c' to continue or 'q' to quit: ")
        if answer.lower() == 'c':
            print("\nYou continue onward!")
            return
        elif answer.lower() == 'q':
            print("\nExiting game...")
            time.sleep(3)
            exit()
        else: 
            print("Invalid Input.")
 
def reset(player):
    '''
        Resets the game and player stats
        TODO
    '''
    pass
 
def reset_at_checkpoint(player):
    '''
        Resets the game to the last completed quest
        TODO
    '''
    pass
 
# RUN GAME
#CHARACTER SELECTION
character = setup_character()
 
if character.name == "End":
    time.sleep(2)
    exit()

# CHARACTER COPY FOR RESETS
init_character = character

print("\n***")
print("At any point in the game if you press 'q' to quit, the game will end.")
print("***\n")
#Test area
check_health(character)
BridgeOfDeath(character)

'''
#INTRO DIALOG
swallow_answer = swallow_chat()
if swallow_answer == 1: 
    print(f"You walk away and move on to the next quest.")
elif swallow_answer == 2: 
    print(f"You continue listening and your next quest gets delayed...")
    time.sleep(10)
else:
    print(f"You decide to go research swallows and quit your quest.")
    print("Game Over...")
    time.sleep(2)
    exit()
check_continue()

#BRING OUT YOUR DEAD
print("\n'Bring out your dead', you hear in the distance as you walk")
print("by an anonymous collective... You continue walking as your")
print("servant clicks his coconuts together. As you enter the forest")
print("you come accross an opening, the Black Knight stands before you.")
check_continue()
 
#THE BLACK KNIGHT
BlackKnight(character)
check_health(character)
check_continue()

#THE LORD
God(character)
check_health(character)
check_continue()

#FLYING ANIMALS
FlyingAnimals(character)
check_health(character)
check_continue()

#GIANT RABBIT
GiantRabbit(character)
check_health(character)
check_continue()

#CHARACTER SPECIFIC SIDE-QUESTS
if character.name == "King Arthur":
    KingArthur(character)
elif character.name == "Sir Galahad":
    SirGalahad(character)
elif character.name == "Sir Bedivere":
    pass
elif character.name == "Sir Lancelot":
    SirLancelot(character)
else:
    SirRobin(character)
    
check_health(character)
check_continue()

#ENCHANTER TIM
EnchanterTim(character)
check_health(character)
check_continue()

#THE CAVE RABBIT
CaveRabbit(character)
check_health(character)
check_continue()

#THE CAVE
TheCave(character)
check_health(character)
check_continue()

#THE BRIDGE OF DEATH
BridgeOfDeath(character)
check_health(character)
check_continue()
'''