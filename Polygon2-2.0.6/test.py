import Polygon
a=Polygon.Polygon(((0.0,0.0),(10.0,0.0),(0.0,10.0)))
b=Polygon.Polygon(((0.0,0.0),(-20.0,0.0),(0.0,-20.0)))
x=a&b
print(x.area())