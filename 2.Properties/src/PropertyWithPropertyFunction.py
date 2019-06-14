class Person:
    
    def __init__(self, name):
        self.name = name
        
    def setName(self, name):
        print('setName() called')
        self.__name = name
        
    def getName(self):
        print('getName() called')
        return self.__name
    
    def delName(self):
        print('delName() called')
        del self.__name
        
    name = property(getName, setName, delName)
    
person = Person("Vlad")
person.name = "Tony"
print(person.name)
del person.name