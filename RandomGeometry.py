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
def Draw_circle():
	ci.center.x = r.randint(-400,400)
	ci.center.y = r.randint(-400,400)
	ci.radius = r.randint(25,200)
	ci.draw((r.randint(0,255),r.randint(0,255),r.randint(0,255)),(r.randint(0,255),r.randint(0,255),r.randint(0,255)),r.randint(2,10))
def Draw_Rectangle():
	re.corner.x = r.randint(-400,400)
	re.corner.y = r.randint(-400,400)
	re.width = r.randint(0,400)
	re.height =r.randint(0,400)
	re.draw((r.randint(0,255),r.randint(0,255),r.randint(0,255)),(r.randint(0,255),r.randint(0,255),r.randint(0,255)),r.randint(2,10))
def Draw_Triangle():
	x = r.randint(-400,400)
	y = r.randint(-400,400)

	t1.b.x= x
	t1.b.y= y
	t1.c.x= x+r.randint(0,400)
	t1.c.y= y
	t1.a.x= x
	t1.a.y= y+r.randint(0,400)
	t1.draw((r.randint(0,255),r.randint(0,255),r.randint(0,255)),(r.randint(0,255),r.randint(0,255),r.randint(0,255)),r.randint(2,10))
### Main body ###
re = shape.Rectangle()
ci = shape.Circle()
t1 = shape.Triangle()
while 1 != 2:
	Draw_circle()
	Draw_Rectangle()
	Draw_Triangle()

#r = Triangle()
#r.draw()

#t.mainloop()

#c.center.x
#c.center.y
#c.radius

#t1.a.x
#t1.a.y
#t1.b.x
#t1.b.y
#t1.c.x
#t1.c.y

#r.corner.x
#r.corner.y
#r.width
#r.height

