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
Level1 = {"A)Run out the door screaming" : {"res": "You run out the door screaming and run right into the principal,You get detention...", "meta" : "Game_over"},"B)Open trapdoor next to your desk and enter." : {"res": "You open the trapdoor and look down. there is a ladder below,you climb down and find yourself in a long tunnel.", "meta" : "next"},"C)Jump through the window like a badass" : {"res": "You look super badass jumping through that window... its too bad you will now have detention for the rest of your life...", "meta" : "Game_over"},"D)Do your work in class." : {"res": "You begin doing your work and boom! you fall asleep again... and get detention this time.", "meta" : "Game_over"}}
Level2 = [{},{"A)###" : {"res": "", "meta" : ""},"B)###" : {"res": "", "meta" : ""},"C)###" : {"res": "", "meta" : ""},"D)###" : {"res": "", "meta" : ""}},{},{}]
Level3 = [{}]
Level4 = [{}]


### Uhh stuffy confueded stuff ###
LevelAcc = {"1" : Level1,"2" : Level2, "3" : Level3 , "4" : Level4}
con = {1 : "c_on_1", 2 : "c_on_2", 3 : "c_on_3",  4 : "c_on_4"}
choice_dic = {"a": 0, "b" : 1, "c": 2, "d" : 3}
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
