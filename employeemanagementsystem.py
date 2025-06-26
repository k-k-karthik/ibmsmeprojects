class employee:
    def __init__(self, name, age, salary, id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

    def display(self):
        print(f" name :{self.name}")
        print(f" age :{self.age}")
        print(f" salary :{self.salary}")
        print(f" id :{self.id}")


    def yearly_CTC_salary(self):
        return self.salary * 12
    
    def cut_salary(self, cut):
        self.salary -= cut
        return self.salary
    
    def take_salary(self, add):
        self.salary += add
        return self.salary
    

Emp1 = employee("Karthik ", 30, 5000, "24153")
Emp1.display()
kkk = Emp1.yearly_CTC_salary()
print(f"Yearly CTC salary: {kkk}")
cut_salary = Emp1.cut_salary(500)
print(f"Cut Salary: {cut_salary}")
take_salary = Emp1.take_salary(1000)
print(f"Take Salary: {take_salary}")
