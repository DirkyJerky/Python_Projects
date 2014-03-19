KEY = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c','q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k','y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S','G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A','O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I','W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
def C_Cipher():
    exit_ = 1
    while exit_ != 0:
        temp = ""
        input_ = raw_input("Type what you would like to encrypt/decrypt: ")
        if input_ == "0":
            exit_ = 0
            print "Goodbye"
            exit
        else:
            for letter in input_:
                temp = temp+str(KEY.get(letter,letter))
            print temp
def histogram_2(s):
    d = dict()
    for c in s:
        d[c] = d.get(c , 0)+1
    return d
def print_hist(h):
    temp = h.keys()
    temp.sort()
    for c in temp:
        print c, h[c]
h = histogram_2('brontosaurus')
print h
print_hist(h)
C_Cipher()
