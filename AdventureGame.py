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
MAINCOUNT = 0
SCREENTEXT = []
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
    
def redraw_screen():
    print "+"+"-"*78+"+"
    print "|"
    print "|"
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
fan_print("You Find yourself in a class room filled with slighty nerdy looking people awdlawhbnklawjhdkaljwhdakjwhdakwjhdakwjdhakwjhdakwjhdakjwdhakjwhdakwjhdakjwdhakwjhkljahkajshdgkjawhdakwjhdak\
jwhdkajwhdakjwhdkajwhdkjawhdhdakwjhdakjwdh")
ti.sleep(1)
fan_print("You Find yourself in a class room filled with slighty nerdy looking people awdlawhbnklawjhdkaljwhdakjwhdakwjhdakwjdhakwjhdakwjhdakjwdhakjwhdakwjhdakjwdhakwjhkljahkajshdgkjawhdakwjhdak\
jwhdkajwhdakjwhdkajwhdkjawhdhdakwjhdakjwdh")




#"a","b","c","4","b","c","7","b","c","10","b","c","13","b","c","16","b","c","19","b","c","22","b","c","25","b","c","28","b","c","31","b","c","34","b","c","37","b","c","40"
