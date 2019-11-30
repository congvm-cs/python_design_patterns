# Interface
class EmployeeAbstract():

    @property
    def name(self):
        raise NotImplementedError

    @property
    def salary(self):
        raise NotImplementedError

    @property
    def roles(self):
        raise NotImplementedError


class Employee(EmployeeAbstract):
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        self._roles = None

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @property
    def roles(self):
        return self._roles


class Developer(Employee):
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        self._roles = None

class Designer(Employee):
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        self._roles = None

class Organization():
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
    
    def get_net_salary(self):
        total_net_salary = sum(map(lambda employee: employee.salary, self.employees))
        return total_net_salary
        
if __name__ == "__main__":
    john = Developer('John', 20)
    jane = Designer('Jane', 10)

    organization = Organization()
    organization.add_employee(jane)
    organization.add_employee(john)

    print(organization.get_net_salary())

    