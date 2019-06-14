class Person:
    
    def __init__(self, aName):
        self._name = aName      # protected attribute
        
    def get_name(self):
        return self._name