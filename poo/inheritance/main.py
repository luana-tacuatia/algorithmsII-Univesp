from employee import Employee
from manager import Manager

employee = Employee()
employee.set_salary(5000)
print(employee.get_salary())

manager = Manager()
manager.set_salary(10000, 300)
print(manager.get_salary())