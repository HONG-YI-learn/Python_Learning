class Employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id

    def print_employee(self):
        print(f"员工名字: {self.name} , 工号: {self.id}")

class FulltimeEmployee(Employee):
    def __init__(self , name , id , monthly_salary):
        super().__init__(name , id)
        self.monthly_salary = monthly_salary

    def calculate_salary_pay(self):
        return self.monthly_salary

class ParttimeEmployee(Employee):
    def __init__(self , name , id , daily_salary , work_days):
        super().__init__(name , id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_salary_pay(self):
        return self.daily_salary * self.work_days

hongyi = FulltimeEmployee("hongyi" , "P161858" , 25000)
hongyiyi = ParttimeEmployee("hongyiyi" , "P161888" , 800 , 22)

hongyi.print_employee()
hongyiyi.print_employee()

print(hongyi.calculate_salary_pay())
print(hongyiyi.calculate_salary_pay())
