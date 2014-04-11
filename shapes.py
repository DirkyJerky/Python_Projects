import math
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
class Line(object):
    """represents a line with a start and end point"""
    def __init__(self,x1=0,y1=0,x2=0,y2=0):
        self.start = Point(x1,y1)
        self.end = Point(x1,y1)
    def distance(self):
        dx = self.start.x - self.end.x
        dy = self.start.y - self.end.y
        return math.sqrt(dx*dx+dy*dy)
class Triangle(object):
    """Represents a triangle based on three vertices"""
    def __init__(self):
        super(Triangle, self).__init__()
        self.arg = arg
        