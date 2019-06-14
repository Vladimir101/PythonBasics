import math

class Point:    # all points are in the first and fourth quadrants 
          
    totalPoints = 0     # class attribute 
    
# constructor   
    def __init__(self, xx = 0, yy = 0):       
        self.x = xx     # public instance attribute               
        self.y = yy     # public instance attribute
        Point.totalPoints += 1

    def distanceFromOrigin(self):
        return math.sqrt(self.x * self.x + self.y * self.y )

    @staticmethod
    def totalOnPlane():
        print("Total points on plane:", Point.totalPoints, "\n")
        
# for printing objects    
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    