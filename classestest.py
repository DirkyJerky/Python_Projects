import math
class Point:    
    """represents a two-dimensional point"""
    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self,dx,dy):
        self.x += dx
        self.y += dy
    def distance(self,p2):
        dx = self.x - p2.x
        dy = self.y - p2.y
        return math.sqrt(dx*dx+dy*dy)
class Rec:
    """Modles a rectangle by upper left corner and size"""
    def __init__(self):
        self.corner = Point()
        self.width = 100
        self.height = 100
    def center(self):
        c = Point()
        c.x = self.corner.x+self.width/2.0
        c.y = self.corner.y+self.height/2.0
        return c

p1 = Point()
p1.move(2,3)

p2 = Point()
p2.move(5,7)

print p1.distance(p2)

box = Rec() 
print box.corner.x, box.corner.y, box.width, box.height 
c = box.center() 
print c.x, c.y

        
        