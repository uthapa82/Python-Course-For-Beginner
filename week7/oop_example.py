class Employee:
    
    # class variable
    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay 
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    

emp_1 = Employee("Anup", 'Thapa', 50000)

# same as running 
# Employee.set_raise_amt = 1.05

Employee.set_raise_amt(1.05)


print(Employee.raise_amt)
print(emp_1.raise_amt)