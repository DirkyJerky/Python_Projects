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
HEALTH = 100
CURRENT_CHOICE_LEVEL = 1
CUREENT_CHOICE_SET = 0
### Choice Layers Defs ###
Level1 = {"A)Run out the door screaming" : {"res": "You run out the door screaming and run right into the principal,You get detention...", "meta" : "Game_over"},"B)###" : {"res": "", "meta" : ""},"C)###" : {"res": "", "meta" : ""},"D)###" : {"res": "", "meta" : ""}}
Level2 = [{}]
Level3 = [{}]
Level4 = [{}]


### Uhh stuffy confueded stuff ###
LevelAcc = {"1" : Level1,"2" : Level2, "3" : Level3 , "4" : Level4}
c_on_1 = ""
c_on_2 = ""
c_on_3 = ""
c_on_4 = ""
### FUNCTION DEFINITIONS ###
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
    global HEALTH
    print "+"+"-"*78+"+"
    print "|"
    print "|  HEALTH: %s/100" %(add_leading0(HEALTH))
    print "|"
    print "+"+"-"*78+"+"
    if len(SCREENTEXT) <= 34:
        print "\n"*(33-len(SCREENTEXT))
        for item in SCREENTEXT:
            print item
    else:
        for i in range(34):
            print SCREENTEXT[len(SCREENTEXT)-34+i]
def fetch_choices():
    if CURRENT_CHOICE_LEVEL == 1:
        return Level1
    elif CURRENT_CHOICE_LEVEL == 2:
        temp = Level2[c_on_1]
        return temp
    elif CURRENT_CHOICE_LEVEL == 3:
        temp = Level3[c_on_1]
        temp = temp[c_on_2]
        return temp
    elif CURRENT_CHOICE_LEVEL == 4:
        temp = Level4[c_on_1]
        temp = temp[c_on_2]
        temp = temp[c_on_3]
        return temp


def choice_chooser():
    global CURRENT_CHOICE_LEVEL 
    global CUREENT_CHOICE_SET
    fan_print ("Do you:")
    choices_main = fetch_choices()
    choice_title = choices_main.keys()
    choice_title.sort()
    for item in choice_title:
        fan_print(item)
    choice = raw_input()
    if choice == "exit":
           exit
    elif choice.lower() == "a" or "b" or "c" or "d":
        fan_print("null")
           
def introduction():
    intro = "Gaa, you appear to have fallen asleep in Mr. Stoddard's class again, You look at the computer infront of you, then at the clock which reads '7:55', You sigh, 6 hours of school left and you are already falling asleep. You hope you can avoid getting detention today. You start thinking about what you should do first..."
    fan_print(intro)
    fan_print(intro)
def main():
    introduction()
    choice_chooser()
### MAIN BODY ###
redraw_screen()
main()
ti.sleep(1)
