###################################
#   Ian Roth
#
#   AdventureGame.py
#
#   ihniwtphy
###################################

### MODULE IMPORTS ###
import time as ti
import random as r
### GLOBAL VARIBALES ###
SCREENTEXT = []
## Player Data ###
player = {"health" : 100,"c_c_l" : 1, "c_c_s" : 0,"c_on_1": "","c_on_2" : "", "c_on_3": "","c_on_4": ""}
### Choice Layers Defs ###
Level1 = {"A)Run out the door screaming" : {"res": "You run out the door screaming and run right into the principal,You get detention...", "meta" : "Game_over"},"B)Open trapdoor next to your desk and enter." : {"res": "You open the trapdoor and look down. there is a ladder below,you climb down and find yourself in a long tunnel. There is a lights going to the left and the right. In addition there is a large knife hanging on the wall. ", "meta" : "next"},"C)Jump through the window like a badass" : {"res": "You look super badass jumping through that window... its too bad you will now have detention for the rest of your life...", "meta" : "Game_over"},"D)Do your work in class." : {"res": "You begin doing your work and boom! you fall asleep again... and get detention this time.", "meta" : "Game_over"}}
Level2 = [{},{"A)Climb back up the ladder" : {"res": "You get back into class but not before Mr. Stoddard notices that you have gone and, guess what you now have detention again", "meta" : "Game_over"},"B)Go down the tunnel to the left" : {"res": "You go down the tunnel to the left and find yourself in a White cube, you turn around to exit but find that the enterace has vanished. You are now stuck.", "meta" : "next"},"C)Sacrifce yourself to the gods of dark." : {"res": "You take the knife and stab yourself in the heart. At least you don't have to worry about detention...", "meta" : "Game_over"},"D)Go down the tunnel to the right" : {"res": "You walk for a while and then all of a sudden find yourself in a circular room with no exits, even the entrance has closed behind you the only thing in the room is a large red button on a pedastel...", "meta" : "next"}},{},{}]
Level3 = [[],[{},{"A)Puke in terror beacuse you are clastrophobic" : {"res": "You choke on your own vomit and die.", "meta" : "Game_over"},"B)Sit in the middle of the floor and wait to be rescued" : {"res": "You are only there for 4 hours before you run out of oxegen and die.", "meta" : "Game_over"},"C)Pray to the gods of dark to rescue you." : {"res": "As a form of rescue they kill you. At leaset you are no longer stuck in the room.", "meta" : "Game_over"},"D)Walk over and press your hand against the wall accross from you." : {"res": "The wall ripples and then all the walls start getting closer and closer. they slowly smash you into a small cube... ", "meta" : "Game_over"}},{},{"A)Look for an exit." : {"res": "You are so focused on looking for an exit that you fail to notice a countdown start underneath the button.. when it finishes the button sinks into the floor and the room start to fill with water, it doesnt take very long for you to drown.", "meta" : "Game_over"},"B)Press the Button" : {"res": "Nothing happens for a few moments, then without any warning you appear to be teleported into a large areana.", "meta" : "next"},"C)Press the button and hold it down." : {"res": "Spikes shoot out of the walls and before you can let go of the button they stab you. You die shortly after.", "meta" : "Game_over"},"D)Pull the button off the stand..." : {"res": "A large needle comes out and stabs you and injects you with a fluid. You have terrible pain and you die.", "meta" : "Game_over"}}],[],[]]
Level4 = [[],[[],[],[],[{},{"A)Take a step forward" : {"res": "A monster appears, it looks sorta like a troll..... You have no choice but to fight it now.", "meta" : "Commence_Fight"},"B)Take a step back" : {"res": "A monster appears it looks kinda like a troll... You have no choice but to fight it now", "meta" : "Commence_Fight"},"C)Turn around and look at the wall." : {"res": "The monster sheers your head off.", "meta" : "Game_over"},"D)Yell 'HELLO!!'" : {"res": "Your voice breaks the dead air and before you know it a great moster that looks like a troll appears and stabs you in the heart.", "meta" : "Game_over"}},{},{}]],[],[]]


### Uhh stuffy confueded stuff ###
LevelAcc = {"1" : Level1,"2" : Level2, "3" : Level3 , "4" : Level4}
con = {1 : "c_on_1", 2 : "c_on_2", 3 : "c_on_3",  4 : "c_on_4"}
choice_dic = {"a": 0, "b" : 1, "c": 2, "d" : 3, "e": 3}
action_functions = {"Game_over" : ""}

### SCREEN FUNCTIONS ###

def fan_print(text):
    global SCREENTEXT
    lngth = len(text)
    if lngth <= 80:
        SCREENTEXT.append(text)
        redraw_screen()
    if lngth > 80:
        rem = lngth%80
        many = (lngth-rem)/float(80)
        SCREENTEXT.append(text[:80])
        for i in range(int(many)):
            SCREENTEXT.append(text[80*(i+1):((i+2)*80)])
        redraw_screen()

def add_leading0(number):
    if len(str(number)) == 2:
        return "0"+str(number)
    elif len(str(number)) == 1:
        return "00"+str(number)
    else:
        return str(number)

def redraw_screen():
    global SCREENTEXT
    print "+"+"-"*78+"+"
    print "|"
    print "|  HEALTH: %s/100" %(add_leading0(player["health"]))
    print "|"
    print "+"+"-"*78+"+"
    if len(SCREENTEXT) <= 34:
        print "\n"*(33-len(SCREENTEXT))
        for item in SCREENTEXT:
            print item
    else:
        for i in range(34):
            print SCREENTEXT[len(SCREENTEXT)-34+i]
            
### FUNCTION DEFINITIONS ###
            
def fetch_choices():
    if player["c_c_l"] == 1:
        return Level1
    elif player["c_c_l"] == 2:
        temp = Level2[player["c_on_1"]]
        return temp
    elif player["c_c_l"] == 3:
        temp = Level3[player["c_on_1"]]
        temp = temp[player["c_on_2"]]
        return temp
    elif player["c_c_l"] == 4:
        temp = Level4[player["c_on_1"]]
        temp = temp[player["c_on_2"]]
        temp = temp[player["c_on_3"]]
        return temp
def monster_att():
    choice = r.randint(0,3)
    if choice == 0:
        fan_print("The troll swings a low slash from the left")
        action = player_action()
        if action[0] == 0 and action[1] > 50:
            fan_print("You sucessfully avoided the trolls action.")
            return 0
        else:
            fan_print("The Troll delt 10 damage to you.")
            return 10
    elif choice == 1:
        fan_print("The troll slashes down from above.")
        action = player_action()
        if action[0] == 1 and action[1] > 50:
            fan_print("You sucessfully avoided the trolls action.")
            return 0
        else:
            fan_print("The Troll delt 10 damage to you.")
            return 10
    elif choice == 2:
        fan_print("The troll slashes from the right.")
        action = player_action()
        if action[0] == 2 and action[1] > 50:
            fan_print("You sucessfully avoided the trolls action.")
            return 0
        else:
            fan_print("The Troll delt 10 damage to you.")
            return 10
    elif choice == 3:
        fan_print("The troll stabs at you.")
        action = player_action()
        if action[0] == 3 and action[1] > 50:
            fan_print("You sucessfully avoided the trolls action.")
            return 0
        else:
            fan_print("The Troll delt 10 damage to you.")
            return 10
def player_att():
    fan_print("Do you?")
    fan_print("A)Slash left")
    fan_print("B)Slash right")
    fan_print("C)Slash above")
    fan_print("D)Stab")
    choice = raw_input()
    if choice.lower() == "a":
        fan_print("You slashed left at the troll")
        action = troll_action()
        if action > 50:
            fan_print("The troll evaded your attack.")
            return 0
        else:
            fan_print("You delt 10 damage to the Troll")
            return 10
    elif choice.lower() == "b":
        fan_print("You slashed right at the troll")
        action = troll_action()
        if action > 50:
            fan_print("The troll evaded your attack.")
            return 0
        else:
            fan_print("You delt 10 damage to the Troll")
            return 10
    elif choice.lower() == "c":
        fan_print("You slashed above at the troll")
        action = troll_action()
        if action > 50:
            fan_print("The troll evaded your attack.")
            return 0
        else:
            fan_print("You delt 10 damage to the Troll")
            return 10
    elif choice.lower() == "d":
        fan_print("You slabed at the troll")
        action = troll_action()
        if action > 50:
            fan_print("The troll evaded your attack.")
            return 0
        else:
            fan_print("You delt 10 damage to the Troll")
            return 10
    else:
        return 0
def troll_action():
    return r.randint(0,100)
        
def player_action():
    fan_print("Do you?")
    fan_print("A)Parry left")
    fan_print("B)Parry above")
    fan_print("C)Parry right")
    fan_print("D)Dodge right")
    fan_print("E)Dodge left")
    choice = raw_input()
    return [choice_dic.get(choice.lower(),-1),r.randint(0,100)]
def fight_troll():
    global player
    global SCREENTEXT
    SCREENTEXT = []
    monster = 100
    redraw_screen()
    fan_print("You now suddenly have armor and a sword")
    fan_print("The fight begins now...")
    while player["health"] > 0 and monster > 0:
        player["health"] = player["health"]-monster_att()
        monster = monster-player_att()
        fan_print("The Troll has %d hit points left" %(monster))
def choice_chooser():
    global player
    game_not_over = True
    while game_not_over == True:
        fan_print ("Do you:")
        choices_main = fetch_choices()
        choice_title = choices_main.keys()
        choice_title.sort()
        for item in choice_title:
            fan_print(item)
        choice = raw_input()
        if choice == "exit":
            exit
            game_not_over == False
        elif choice.lower() == "a" or choice.lower() == "b" or choice.lower() == "c" or choice.lower() =="d":
            player[con[player["c_c_l"]]] = choice_dic[choice.lower()]
            choice_ = choice_dic[choice.lower()]
            specific = choices_main[choice_title[choice_]]
            fan_print(specific["res"])
            if specific["meta"] == "Game_over":
                game_not_over = False
                exit
            elif specific["meta"] == "next":
                player["c_c_l"] = player["c_c_l"]+1
            elif specific["meta"] == "Commence_Fight":
                fight_troll()
def introduction():
    intro = "Gaa, you appear to have fallen asleep in Mr. Stoddard's class again, You look at the computer infront of you, then at the clock which reads '7:55', You sigh, 6 hours of school left and you are already falling asleep. You hope you can avoid getting detention today. You start thinking about what you should do first..."
    fan_print(intro)

def main():
    global player
    global SCREENTEXT
    play_again = True
    while play_again == True:
        player = {"health" : 100,"c_c_l" : 1, "c_c_s" : 0,"c_on_1": "","c_on_2" : "", "c_on_3": "","c_on_4": ""}
        SCREENTEXT = []
        introduction()
        choice_chooser()
        fan_print("GAME OVER")
        fan_print("would you like to play again (y/n)")
        if raw_input().lower() == "n":
            play_again = False
    
### MAIN BODY ###
redraw_screen()
main()
ti.sleep(1)
#  TEMPLATE # {"A)###" : {"res": "", "meta" : ""},"B)###" : {"res": "", "meta" : ""},"C)###" : {"res": "", "meta" : ""},"D)###" : {"res": "", "meta" : ""}}
[[{},{},{},{}],[{},{},{},{}],[{},{},{},{}],[{},{},{},{}]]
