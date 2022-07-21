class Employee:
    def __init__(self, first, last, id, hpay):
        self.first = first
        self.last = last
        self.id = id
        self.hpay = pay
    def pay(self, hours):
        return "{:.2f}".format(self.hpay * hours) if hours <= 40 else "{:.2f}".format(self.hpay * 40 + ((hours - 40) * 1.5 * self.hpay)) 
        
id = int(input("Please enter the Employee's ID: "))
first = input("Please enter the Employee's First Name: ")
last = input("Please enter the Employee's Last Name: ")
pay = float(input("Please enter the Employee's Hourly Pay Rate: "))
hours = float(input(f"How many hours did {first} work this week? "))
employee = Employee(first, last, id, pay)
print(f"{first} {last}'s paycheck amount is ${employee.pay(hours)}")