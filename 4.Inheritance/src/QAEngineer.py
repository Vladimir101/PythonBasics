from Person import Person
from Employee import Employee

class QAEngineer(Person, Employee):
    
    def __init__(self, aName, aSalary, aCompany, aBonus):
        Person.__init__(self, aName)
        Employee.__init__(self, aSalary, aCompany)
        self.__signInBonus = aBonus     #private attribute
        
    def get_bonus(self):
        return self.__signInBonus
    