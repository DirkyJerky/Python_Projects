##################################
# Ian Roth
#
#  Words.py
#
#  Files opening :)
###################################

### Module imports ###

###  Global Variables  ###

### Function Definitions ###
def get_start_letter():
        fin = open("words.txt")
        start = {}
        for line in fin:
                word = line.strip()
                start[word[0]] = start.get(word[0], 0) + 1
        fout = open("letter_counts.txt","w")
        items = start.keys()
        items.sort()
        for item in items:
                fout.write("%s: %d\n"%(item,start.get(item,0)))
        print "Done"
        fout.close()
        fin.close()
def get_percen_e():
        fin = open("words.txt")
        count = 0
        total = 0
        for line in fin:
                total += 1
                if "e" not in line:
                        count += 1
        percent = (float(count)/total)*100
        print ('The percentage of words with no "E" is %d percent.'%(percent))
### Main body ###
get_start_letter()
#get_percen_e()
