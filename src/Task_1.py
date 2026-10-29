import csv

class InvalidSalaryError(Exception):
    """When an employee's salary is negative this Exception Raised ."""
    pass

def bonus(salary,rate=0.1,*extras,**options):
    total_bonus=(salary*rate)+sum(extras)
    if 'cap' in options:
        total_bonus=min(total_bonus,options['cap'])
    return total_bonus
class Employee:
    def __init__(self,name,salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary : {salary}")
        self.name = name
        self.salary= salary

    def annual_salary(self):
        return self.salary*12

    def get_details(self):
        return f"Employee: {self.name},Salary: {self.salary}"

class Manager(Employee):
    def __init___(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size=team_size

    def get_details(self):
        return f"Manager: {self.name},Salary: {self.salary},Team Size: {self.team_size}"

employees_data=[]

with open("employees.csv",mode="r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        row["salary"]=int(row["salary"])
        employees_data.append(row) 

above_50000=[emp["name"] for emp in employees_data if emp["salary"]> 50000]
print(f"Above 50000: {above_50000}")

chennai_employees = list(filter(lambda emp: emp["city"]=="Chennai",employees_data))
chennai_names= [emp["name"] for emp in chennai_employees]
print(f"Chennai: {chennai_names}")

raised_salaries = list(map(lambda emp: {**emp,"salary": emp["salary"]*1.1},employees_data))

for emp in employees_data:
    if emp["salary"] == 0:
        continue
    if emp["salary"]>85000:
        break

try:
    invalid_emp = Employee("Test User", -500)
except InvalidSalaryError as e:
    print(f"Error: {e}")
finally:
    print("Transaction finished")

