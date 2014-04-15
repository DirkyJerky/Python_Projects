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

def strip_tags(html):
	s = MLStripper()
	s.feed(html)
	return s.get_data()

def seek_0():
	fpa.seek(0)
	fb.seek(0)
	fgs.seek(0)
	fl.seek(0)

def trun():
	fpa.truncate()
	fb.truncate()
	fgs.truncate()
	fl.truncate()

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
fpa = open("pa.txt","r+")
fb = open("blitz.txt","r+")
fgs = open("gs.txt","r+")
fl =open("lobby.txt","r+")
fpa_ = strip_tags(fpa.read())
fb_ = strip_tags(fb.read())
fgs_ = strip_tags(fgs.read())
fl_ = strip_tags(fl.read())
seek_0()

fpa.write(fpa_)
fb.write(fb_)
fgs.write(fgs_)
fl.write(fl_)
trun()
fpa.close()
fb.close()
fgs.close()
fl.close()
buffer_ = ""
with open("pa.txt","r+") as fpa:
	for line in fpa:
		if line.strip():
			buffer_ = buffer_+line
	print buffer_
	fpa2.write(buffer_)
	fpa2.close()


