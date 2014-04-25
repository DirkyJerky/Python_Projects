##################################
#  Ian Roth
#
#  Shapes.py
#
#  more shapes yay.png
###################################

### Module imports ###
import math
import turtle as t
###  Global Variables  ###
### Classes ###

class Point:    
    """Represents a two-dimensional point"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def move(self,dx,dy):
        self.x += dx
        self.y += dy
    def distance(self,p2):
        dx = self.x - p2.x
        dy = self.y - p2.y
        return math.sqrt(dx*dx+dy*dy)

class Rectangle:
    """Repersents a rectangle by upper left corner and size"""
    def __init__(self,width= 100,height= 100,x=0,y=0):
        self.corner = Point(x,y)
        self.width = width
        self.height = height
    def center(self):
        c = Point()
        c.x = self.corner.x+self.width/2.0
        c.y = self.corner.y+self.height/2.0
        return c
    def move(self,dx,dy):
        self.corner.move(dx,dy)
    def area(self):
        rect_area = self.width*self.height
        return rect_area
    def perimeter(self):
        perimeter = self.width*2+self.height*2
        return perimeter
    def draw(self,fill_color="black",pen_color="red",pen_width=2,colormode256 = False):
        setup(colormode256)
        t.color(pen_color,fill_color)
        t.pensize(pen_width)
        t.penup()
        t.goto(self.corner.x,self.corner.y)
        t.pendown()
        fill_t()
        for i in range(2):
            t.forward(self.width)
            t.left(90)
            t.forward(self.height)
            t.left(90)
        fill_f()

class Line():
    """Represents a line with a start and end point"""
    def __init__(self,x1=0,y1=0,x2=0,y2=0):
        self.start = Point(x1,y1)
        self.end = Point(x2,y2)
    def size(self):
        dx = self.start.x - self.end.x
        dy = self.start.y - self.end.y
        return math.sqrt(dx*dx+dy*dy)

class Triangle():
    """Represents a triangle based on three vertices , 'b' is the vertice with the 90 degree angle"""
    def __init__(self,x1=0,y1=100,x2=0,y2=0,x3=100,y3=0):
        self.a = Point(x1,y1)
        self.b = Point(x2,y2)
        self.c = Point(x3,y3)
        self.sideA = self.b.distance(self.c)
        self.sideB = self.a.distance(self.c)
        self.sideC = self.b.distance(self.a)
    def area(self):
        return (self.sideA*self.sideC)/2
    def perimeter(self):
        return self.sideA+self.sideB+self.sideC
    def draw(self,fill_color="black",pen_color="red",pen_width=2,colormode256 = False):
        setup(colormode256)
        t.color(pen_color,fill_color)
        t.pensize(pen_width)
        t.penup()
        t.goto(self.b.x,self.b.y)
        fill_t()
        t.pendown()
        t.goto(self.a.x,self.a.y)
        t.goto(self.c.x,self.c.y)
        t.goto(self.b.x,self.b.y)
        fill_f()

class Circle():
    """Represents circle by center and radius"""
    def __init__(self,x=0,y=0,r=100):
        self.center = Point(x,y)
        self.radius = r
    def circumference(self):
        return math.pi*(2*self.radius)
    def area(self):
        return math.pi*(self.radius**2)
    def draw(self,fill_color="black",pen_color="red",pen_width=2,colormode256 = False):
        setup(colormode256)
        t.color(pen_color,fill_color)
        t.pensize(pen_width)
        fill_t()
        t.penup()
        t.goto(self.center.x,self.center.y-self.radius)
        t.pendown()
        t.circle(self.radius)
        fill_f()

### Function Definitions ###
def fill_t():
    t.begin_fill()
def fill_f():
    t.end_fill()
def setup(colormode256):
    t.hideturtle()
    t.speed(10)
    if colormode256 == True:
        t.colormode(255)
### Main body ###
