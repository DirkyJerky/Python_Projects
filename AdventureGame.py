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
HEALTH = 10
### FUNCTION DEFINITIONS ###
def fan_print(text):
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
    if len(str(number)) == 1:
        return "0"+str(number)
    else:
        return str(number)
    
def redraw_screen():
    print "+"+"-"*78+"+"
    print "|"
    print "|  HEALTH: %s/10" %(add_leading0(HEALTH))
    print "|"
    print "+"+"-"*78+"+"
    if len(SCREENTEXT) <= 34:
        print "\n"*(33-len(SCREENTEXT))
        for item in SCREENTEXT:
            print item
    else:
        for i in range(34):
            print SCREENTEXT[len(SCREENTEXT)-34+i]
    
### MAIN BODY ###
redraw_screen()
ti.sleep(1)

