import math

class Point:    # all points are in the first and fourth quadrants 
          
    totalPoints = 0     # class attribute 
    
# constructor   
    def __init__(self, xx = 0, yy = 0):       
        self.x = xx     # property               
        self.y = yy     # public instance attribute
        Point.totalPoints += 1

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if (value < 0):
            print("All points must be in the first or fourth quadrants")
            self.__x = 0
        else:
            self.__x = value

    def distanceFromOrigin(self):
        return math.sqrt(self.__x * self.__x + self.y * self.y )
        
# for printing objects    
    def __str__(self):
        return "(" + str(self.__x) + "," + str(self.y) + ")"
    