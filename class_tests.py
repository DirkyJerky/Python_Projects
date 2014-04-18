from shapes import *

p = Point()
p.move(2,3)
print p.x, p.y
p = Point(4,10)
p.move(3,5)
print p.x, p.y
r = Rectangle()
print r.area()
r = Rectangle(20,30)
print r.area()

l1 = Line()
print l1.end.y