class Person:
# class has one attribute 'name' defined as a property   
 
    # getter
    @property           
    def name(self):
        print('getter was called')
        return self.__name
    
    # setter
    @name.setter        
    def name(self, value):
        print('setter was called')
        self.__name=value
        
person = Person()
person.name = "Vlad"
print(person.name)