##################################
#  Ian Roth
#
#  Shapes.py
#
#  more shapes yay.png
###################################

### Module imports ###
import math
###  Global Variables  ###

### Classes ###

class Point:    
    """represents a two-dimensional point"""
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
    """Modles a rectangle by upper left corner and size"""
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
class Line():
    """represents a line with a start and end point"""
    def __init__(self,x1=0,y1=0,x2=0,y2=0):
        self.start = Point(x1,y1)
        self.end = Point(x2,y2)
    def size(self):
        dx = self.start.x - self.end.x
        dy = self.start.y - self.end.y
        return math.sqrt(dx*dx+dy*dy)
class Triangle():
    """Represents a triangle based on three vertices , 'b' is the vertice with the 90 degree angle"""
    def __init__(self,x1=0,y1=10,x2=0,y2=0,x3=10,y3=0):
        self.a = Point(x1,y1)
        self.b = Point(x2,y2)
        self.c = Point(x3,y3)
        self.sideA = 0
        self.sideB = 0
        self.sideC = 0
        self.size()
    def size(self):
        dx = self.b.x - self.c.x
        dy = self.b.y - self.c.y
        self.sideA = math.sqrt(dx*dx+dy*dy)
        dx = self.a.x - self.c.x
        dy = self.a.y - self.c.y
        self.sideB = math.sqrt(dx*dx+dy*dy)
        dx = self.b.x - self.a.x
        dy = self.b.y - self.a.y
        self.sideC = math.sqrt(dx*dx+dy*dy)
    def area(self):
        return (self.sideA*self.sideC)/2
    def perimeter(self):
        return self.sideA+self.sideB+self.sideC
class Circle():
    """Circle by center and rad"""
    def __init__(self,x=0,y=0,r=100):
        self.center = Point(x,y)
        self.radius = r
    def circumference(self):
        return math.pi*(2*self.radius)
    def area(self):
        return math.pi*(self.radius**2)
### Main body ###

### Function Definitions ###