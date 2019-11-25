# Roslyn Parker
# Start Date: 4 Nov. 2019
# End Date: 

# This file is the main program
# for the TextQuest-HolyGrail game

from Player import Player
from Quest import Quest
from Quests import * 
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
    time.sleep(20)
    print(f"\tSoldier #1: 'Halt! Who goes there?'")
    time.sleep(2)
    print(f"\t{character.name}: 'It is I, {character.name}!'")
    time.sleep(2)
    print(f"\tSoldier #1: 'Pull the other one!'")
    time.sleep(2)
    print(f"\t{character.name}: You introduce your servant then say, 'I have come to join my fellow knights of Camelot.'")
    time.sleep(4)
    print(f"\tSoldier #1: 'What? Ridden on a horse? --those are just coconuts!'")
    time.sleep(2)
    print(f"\t{character.name}: 'What?'")
    time.sleep(2)
    print(f"\tSoldier #1: 'You've got two empty halves of coconut and you're bangin' 'em together.'")
    time.sleep(3)
    print(f"\t{character.name}: 'So? We have ridden since the snows of winter covered this land...'")
    time.sleep(3)
    print(f"\tSoldier #1: 'Where'd you get the coconuts?'")
    time.sleep(2)
    print(f"\t{character.name}: 'We found them.'")
    time.sleep(2)
    print(f"\tSoldier #1: 'Found them? in Mercia? The coconut's tropical! Are you suggecting coconuts migrate?'")
    time.sleep(3)
    print(f"\t{character.name}: 'Not at all. They could be carried.'")
    time.sleep(2)
    print(f"\tSoldier #1: 'What? A swallow carrying a coconut? It's a simple question of weight ratios!'")
    time.sleep(3)
    print(f"\t{character.name}: 'Well, it doesn't matter. Will you tell your master that {character.name} is here from the Court of Camelot?'")
    time.sleep(5)
    print(f"\tSolier #1: 'Listen. In order to maintain the air-speed velocity a swallow needs...'")
    time.sleep(3)
    print(f"\t{character.name}: 'Please!'")
    time.sleep(2)
    print(f"\tSoldier #1: 'Am I right?'")
    time.sleep(2)
    print(f"\t{character.name}: 'I'm not interested!'")
    time.sleep(2)
    print(f"\tSoldier #2: 'It could be carried by an African Swallow!'")
    time.sleep(5)
    print(f"\nYou become frustrated with the chatter about swallow nonsense...")
    while(True):
        try: 
            answer = int(input(f"Do you: \n\t1) walk away \n\t2) continue listening \n\t3) research swallows\nAnswer:"))
            if answer in range(1, 4): 
                return answer
            else: 
                print("Invalid Input")
        except:
            print("Invalid Input")
   
# RUN GAME
character = setup_character()
if character.name == "End":
    exit()
 
 #INTRO DIALOG
swallow_answer = swallow_chat()
 
quest = BlackKnight(character)
print(f"you rolled a {quest.roll20()} limbs {quest.limbs} player health {character.health}")