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
CURRENT_CHOICE_LEVEL = 0
CUREENT_CHOICE_SET = 0
### Choice Layers Defs ###
Level1 = [{"A)" : "value"}]
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
def choice_chooser():
    
    print "null"
def introduction():
    intro = "Gaa, you appear to have fallen asleep in Mr. Stoddard's class again, You look at the computer infront of you, then at the clock which reads '7:55', You sigh, 6 hours of school left and you are already falling asleep. You start thinking about what you should do..."
    fan_print(intro)
def main():
    introduction()
### MAIN BODY ###
redraw_screen()
main()
ti.sleep(1)
