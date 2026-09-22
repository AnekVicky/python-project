class Employee:
    raise_amount = 1.5
    employee_count = 0
    def __init__(self,first_name,last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = pay
        Employee.employee_count += 1

    def full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
        return self

emp = Employee(first_name='anek',last_name='singh',pay=1000)
print(emp.first_name)
print(emp.last_name)
print(emp.salary)
print(emp.full_name())
print('by class name ',Employee.full_name(emp))

emp2 = Employee('vicky','singh',90000)

raised_emp = emp.apply_raise()
print(f'raised salary  : {raised_emp.__dict__}')

print(emp.__dict__)
print(emp.apply_raise().salary)
print(emp2.__dict__)
emp2.raise_amount = 2.0
print(emp2.apply_raise().salary)
print('Class Employee \n',Employee.__dict__)

print(emp2.employee_count)






