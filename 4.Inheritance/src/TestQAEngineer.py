from QAEngineer import QAEngineer

qaEng = QAEngineer("Anthony", 120000, "Kaiser", 5000)

print("The best QA Engineer: " + qaEng.get_name())
print("Salary:", qaEng.get_salary())
print("Company:", qaEng._company)       # not recommended
print("SignInBonus:", qaEng.get_bonus())