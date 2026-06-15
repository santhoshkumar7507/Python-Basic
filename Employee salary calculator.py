class Employee:

    def __init__(self, salary):
        self.salary = salary

    def yearly_salary(self):
        return self.salary * 12

emp = Employee(50000)

print(emp.yearly_salary())