class Animal:
    
    def __init__(self, aType):
        self.__type = aType

    def get_type(self):
        return self.__type
       
    def eat(self):
        print("eating...")    
        

