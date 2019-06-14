class Employee:
    
    def __init__(self, aSalary, aCompany):
        self._salary = aSalary
        self._company = aCompany
        
    def get_salary(self):
        return self._salary
    
    def get_company(self):
        return self._company