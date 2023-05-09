from employee import Employee

class Manager(Employee):

    def set_salary(self, salary, bonus):
        salary += bonus
        super().set_salary(salary)
