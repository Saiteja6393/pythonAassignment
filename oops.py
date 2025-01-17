#program 1
class Demo:
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2
    def Fun(self):
        print("Fun Method's First value:", self.num1)
        print("Fun Method's Second value:", self.num2)
    def Gun(self):
        print("Gun Method's First Value:",self.num1)
        print("Gun Method's Second value:",self.num2)
ob1=Demo(10,20)
ob2=Demo(30,40)
ob1.Fun()
ob1.Gun()
ob2.Fun()
ob2.Gun()

#program 2
class Bookstore():
    totalBooks=0
    def __init__(self,name,author):
        self.name=name
        self.author=author
        Bookstore.totalBooks+=1
    def display(self):
        print("Book Name:",self.name, "\nAuthor:",self.author, "\nTotal Books:", Bookstore.totalBooks)
obj1=Bookstore("Linux System Programming","Robert Love")
obj1.display()
obj2=Bookstore("C programming","Robert Love")
obj2.display()


#program 3

class Circle:
    PI = 3.14
    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0
    
    def Accept(self):
        self.radius = float(input("Enter the radius of the circle: "))
    
    def Area(self):
        self.area = Circle.PI * self.radius ** 2
    
    def Circumference(self):
        self.circumference = 2 * Circle.PI * self.radius

    def Display(self):
        print("Radius:", self.radius)
        print("Area:", self.area)
        print("Circumference:", self.circumference)

circle1 = Circle()
circle1.Accept()
circle1.Area()
circle1.Circumference()
circle1.Display()

circle2 = Circle()
circle2.Accept()
circle2.Area()
circle2.Circumference()
circle2.Display()

#program 4

class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.name = input("Enter account holder's name:")
        self.amount = float(input("Enter the amount for:"))

    def Display(self):
        print("Account Holder:", self.name)
        print("Amount:", self.amount)
    
    def Deposit(self):
        deposit_amount = int(input("Enter the amount to be depsoited:"))
        self.amount += deposit_amount
        print(deposit_amount, "has been deposited. Balance:", self.amount)
    
    def Withdraw(self):
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= self.amount:
            self.amount -= withdraw_amount
            print(withdraw_amount, "has been withdrawn. Balance:", self.amount)
        else:
            print("Insufficient Balance!")
    
    def CalculateInterest(self):
        interest = (self.amount * BankAccount.ROI) / 100
        print("Interest on the current balance", self.amount, "is", interest)

account1 = BankAccount()
account1.Display()
account1.Deposit()
account1.Withdraw()
account1.CalculateInterest()

account2 = BankAccount()
account2.Display()
account2.Deposit()
account2.Withdraw()
account2.CalculateInterest()

#program 5
class Numbers:
    def __init__(self, value):
        self.value =  value
    
    def ChkPrime(self):
        if self.value <= 1:
            return False
        for i in range(2, int(self.value ** 0.5) + 1):
            if self.value % i == 0:
                return False
        return True
    
    def ChkPerfect(self):
        if self.value <= 1:
            return False
        sum_of_factors = self.SumFactors()
        return sum_of_factors == self.value
    
    def Factors(self):
        factors = []
        for i in range(1, self.value):
            if self.value % i == 0:
                factors.append(i)
        return factors
     
    def DisplayFactors(self):
        factors = self.Factors()
        print("Factors of", self.value, "are", factors)
    

    
    def SumFactors(self):
        factors = self.Factors()
        return sum(factors)
    

num1 = Numbers(6)
print("Is", num1.value, "isPrime?", num1.ChkPrime())
num1.DisplayFactors()
print("Is", num1.value, "isPerfect?", num1.ChkPerfect())
print("Sum of factors of", num1.value, "are", num1.SumFactors())

num2 = Numbers(28)
print("Is", num2.value, "isPrime?", num2.ChkPrime())
num2.DisplayFactors()
print("Is", num2.value, "isPerfect?", num2.ChkPerfect())
print("Sum of factors of", num2.value, "are", num2.SumFactors())


#program 6
class Numbers2:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self):
        self.Value1 = float(input("Enter the first value (Value1): "))
        self.Value2 = float(input("Enter the second value (Value2): "))
    
    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return "Error! Division by zero."
        
num1 = Numbers2()
num1.Accept()
print("Addition of", num1.Value1, "and", num1.Value2, "is", num1.Addition())
print("Subtraction of {} and {}: {}".format(num1.Value1, num1.Value2, num1.Subtraction()))
print("Multiplication of {} and {}: {}".format(num1.Value1, num1.Value2, num1.Multiplication()))
print("Division of {} and {}: {}".format(num1.Value1, num1.Value2, num1.Division()))


num2 = Numbers2()
num2.Accept()
print("Addition of {} and {}: {}".format(num2.Value1, num2.Value2, num2.Addition()))
print("Subtraction of {} and {}: {}".format(num2.Value1, num2.Value2, num2.Subtraction()))
print("Multiplication of {} and {}: {}".format(num2.Value1, num2.Value2, num2.Multiplication()))
print("Division of {} and {}: {}".format(num2.Value1, num2.Value2, num2.Division()))
