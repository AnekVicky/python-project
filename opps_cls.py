class Employee:
    EMP_COUNT = 0
    def __init__(self,first_name,last_name,pay):
        self.first_name  = first_name
        self.last_name = last_name
        self.salary = pay
        Employee.EMP_COUNT += 1


    def full_name(self):
        return self.first_name+self.last_name

    @classmethod
    def from_str(cls,emp_str:str):
        emp_list = emp_str.split('-')
        cls.first_name,cls.last_name,cls.salary = emp_list
        print(type(emp_list),emp_list)
        return cls(cls.first_name,cls.last_name,cls.salary)

emp_1 = Employee('anek','singh',10000)
print(emp_1.EMP_COUNT)
print(f'Employee Object dict : {emp_1.__dict__}')
print(f'Employee Class dict : {Employee.__dict__}')

emp = Employee.from_str('Vicky-Singh-90000')
print(Employee.EMP_COUNT)