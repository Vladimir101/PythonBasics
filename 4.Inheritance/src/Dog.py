from Animal import Animal

class Dog(Animal):
    
    def __init__(self, aType, aName, aBreed):
        super().__init__(aType)     # in Python 3
        self.__name = aName
        self.__breed = aBreed
        
    def bark(self):
        print("barking...")
        
    def get_name(self):
        return self.__name
    
    def get_breed(self):
        return self.__breed