##################################
# Ian Roth
#
#  RandomGeometry.py
#
#  RandomGeometry using shapes.py
###################################

### Module imports ###
import shapes as shape
import random as r
###  Global Variables  ###

### Function Definitions ###
def Draw_circle(fill,pen):
	ci.center.x = r.randint(-400,400)
	ci.center.y = r.randint(-400,400)
	ci.radius = r.randint(25,200)
	ci.draw(fill,pen,r.randint(2,10),True)

def Draw_Rectangle(fill,pen):
	re.corner.x = r.randint(-400,400)
	re.corner.y = r.randint(-400,400)
	re.width = r.randint(0,400)
	re.height =r.randint(0,400)
	re.draw(fill,pen,r.randint(2,10),True)

def Draw_Triangle(fill,pen):
	x = r.randint(-400,400)
	y = r.randint(-400,400)
	t1.b.x= x
	t1.b.y= y
	t1.c.x= x+r.randint(0,400)
	t1.c.y= y
	t1.a.x= x
	t1.a.y= y+r.randint(0,400)
	t1.draw(fill,pen,r.randint(2,10),True)

def get_color():
	fill = (r.randint(0,255),r.randint(0,255),r.randint(0,255))
	pen = (r.randint(0,255),r.randint(0,255),r.randint(0,255))
	return fill,pen

### Main body ###
re = shape.Rectangle()
ci = shape.Circle()
t1 = shape.Triangle()
# Main Loop
while 1 != 2:
	pick = r.randint(1,3)
	if pick == 1:
		fill,pen = get_color()
		Draw_circle(fill,pen)
	if pick == 2:
		fill,pen = get_color()
		Draw_Rectangle(fill,pen)
	else:
		fill,pen = get_color()
		Draw_Triangle(fill,pen)
t.mainloop()