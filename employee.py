"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary=0, commission=0, bonus=0, contractsCompleted=0, hoursContracted=0, payPerHour=0):
        self.name = name
        self.salary = salary
        self.commission = commission
        self.bonus = bonus
        self.contractsCompleted = contractsCompleted
        self.hoursContracted = hoursContracted
        self.payPerHour = payPerHour

    def get_pay(self):
        if self.salary > 0:
            pay = self.salary
        else:
            pay = (self.payPerHour * self.hoursContracted)
        pay += self.bonus
        pay += (self.commission * self.contractsCompleted)
        return pay

    def __str__(self):
        string = self.name
        if self.salary:
            string += " works on a monthly salary of " + str(self.salary)
        else:
            string += " works on a contract of " + str(self.hoursContracted) + " hours at " + str(self.payPerHour) + "/hour"
        if self.bonus:
            string += " and receives a bonus commission of " + str(self.bonus)
        if self.commission:
            string += " and receives a commission for " + str(self.contractsCompleted) + " contract(s) at " + str(self.commission) + "/contract"
        string += ". Their total pay is " + str(self.get_pay()) + "."
        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary=4000)
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hoursContracted=100, payPerHour=25)
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary=3000, commission=200, contractsCompleted=4)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hoursContracted=150, payPerHour=25, commission=220, contractsCompleted=3)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary=2000, bonus=1500)
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', bonus=600, hoursContracted=120, payPerHour=30)
