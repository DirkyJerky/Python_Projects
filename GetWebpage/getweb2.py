import urllib2
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
        def __init__(self):
                self.reset()
                self.fed = []
        def handle_data(self, d):
                self.fed.append(d)
        def get_data(self):
                return ''.join(self.fed)
class Strip():
        """docstring for strip"""
        def __init__(self,name):
                self.file_ = name+".txt"
                self.strip_tag()
                self.remove_spaces()
        def strip_tag(self):
                temp = open(self.file_,"r+")
                self.data = strip_tags(temp.read())
                temp.close()
                self.write_to(self.data)
        def write_to(self,data):
                temp2 = open(self.file_,"w")
                temp2.write(data)
                temp2.truncate()
                temp2.close()
        def remove_spaces(self):
                buffer_ = ""
                with open(self.file_,"r+") as fpa:
                        for line in fpa:
                                if line.strip():
                                        buffer_ = buffer_+line
                self.write_to(buffer_)
        def get_data(self,servers):
                self.staff_online = {}
                self.player_count = {}
                restart_count = servers[0]
                restart = False
                switch_dic = False
                save_next = False
                temp = open(self.file_,"r")
                print servers
                for line in temp:
                        if save_next == True:
                                self.staff_online[temp2] = line.strip()
                                save_next = False
                                print line
                        if line.strip() in servers:
                                temp2 = line.strip()
                                save_next = True
                                print "help"
                                

def strip_tags(html):
        s = MLStripper()
        s.feed(html)
        return s.get_data()\

def fetch_update():
        user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
        headers = { 'User-Agent' : user_agent }
        req = urllib2.Request('https://oc.tc/play', None, headers)
        response = urllib2.urlopen(req)
        page = response.read()
        fout = open("page.txt","w")
        fout.write(page)
        fout.close()

        fout = open("page.txt","r")
        fpa= open("pa.txt","w")
        fb = open("blitz.txt","w")
        fgs = open("gs.txt","w")
        fl =open("lobby.txt","w")
        add_pa = False
        add_blitz = False
        add_gs = False
        add_lobby = False

        for line in fout:
                if "<div class='tab-pane' id='us-project-ares'>" in line:
                        add_pa = True
                elif "<div class='tab-pane' id='us-blitz'>" in line:
                        add_pa = False
                        add_gs = False
                        add_blitz = True
                elif "<div class='tab-pane' id='us-ghost-squadron'>" in line:
                        add_pa = False
                        add_gs = True
                        add_blitz = False
                elif "<div class='tab-pane' id='us-lobby'>" in line:
                        add_lobby = True
                        add_gs = False
                elif "<div class='tab-pane' id='eu'>" in line:
                        add_pa = False
                        add_blitz = False
                        add_gs = False
                        add_lobby = False
                if add_pa == True:
                        fpa.write(line)
                elif add_blitz == True:
                        fb.write(line)
                elif add_gs == True:
                        fgs.write(line)
                elif add_lobby == True:
                        fl.write(line)

        fpa.close()
        fb.close()
        fgs.close()
        fl.close()
        fout.close()
        pa = Strip("pa")
        b = Strip("blitz")
        gs = Strip("gs")
        l = Strip("lobby")
        pa.get_data(["Alpha","Beta","Gamma","CTW1","CTW2","DTC1","DTC2","TDM","Gear","Mini01","Mini02","Mini03","Mini04","Mini05","Mini06","Mini07","Mini08","Mini09","Mini10","Nostalgia"])
        print pa.staff_online
fetch_update()
