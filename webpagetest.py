from grab import Grab

g = Grab ()

g.go('http://livejournal.com')
print g.xpath_text('/ / title')

#//*[@id="login"]



#//*[@id="password"]


#//*[@id="bLogin"]


