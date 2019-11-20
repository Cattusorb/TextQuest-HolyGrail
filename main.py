# Roslyn Parker
# Start Date: 4 Nov. 2019
# End Date: 

# This file is the main program
# for the Holy Grail Search game

from Player import Player

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
        
   
# RUN GAME HERE OR CREATE A FUNCTION TO DO SO
character = setup_character()
if character.name == "End":
    exit()