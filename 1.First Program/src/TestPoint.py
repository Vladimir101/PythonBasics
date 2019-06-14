from Point import Point

p1 = Point(3, 4)
distance = p1.distanceFromOrigin()

# printing multiple values with a space as a separator
print("Distance from origin for (", 
      str(p1.x), ",", str(p1.y), ") is ", str(distance), "\n")

# print object
print(p1)

print("Distance from origin for", p1, "is", str(distance), "\n")

p2 = Point(-1, 6)
distance = p2.distanceFromOrigin()
print("Distance from origin for", p2, "is", str(distance), "\n")

# use default values for the point
p3 = Point()
distance = p3.distanceFromOrigin()
print("Distance from origin for", p3, "is", str(distance), "\n")

# calling static method
Point.totalOnPlane()