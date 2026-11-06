#first_class

class Dog:
    pass    # leave it empty for now
dog1 = Dog()
dog2 = Dog()
dog3 = Dog()

#__init__

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

Student1 = Student("Ada", 20,  "ENT 212")
Student2 = Student("Bayo", 16, "CSC 226")

print(Student1.name, Student1.age)
print(Student2.age, Student2.course)

#attributes
class Car:
    def __init__(self, brand, colour):
        self.brand = brand
        self.colour = colour
        self.speed = 0

my_car = Car("Toyota", "red")
print(my_car.brand)
print(my_car.speed)
print(my_car.colour)


my_car.colour = "blue"
print(my_car.colour)

#methods
class Car:
    def __init__(self, brand, colour):
        self.brand = brand
        self.colour = colour
        self.speed = 10
    

    def accelerate (self, amount):
        self.speed += amount
        print(self.brand, "is now going", self.speed, "km/h")

    def brake(self):
        self.speed = 10
        print(self.brand, "has stopped")

car1 = Car("Toyota", "red")
car2 = Car("BMW", "black")

car1.accelerate(50)
car2.accelerate(30)
car1.brake()   
print(car2.speed)       

#__str__
class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name + "(is " + str(self.age) + "years old)" 
      
s = Students("Ada", 20)
s1 = Students("Esther", 19)
print(s)     
print(s1)
        
#Mini project
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):  
        self.balance += amount
        print("Deposited", amount, " balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")     
        else:
            self.balance -= amount
            print("Withdrew", amount, " balance:", self.balance)

account = BankAccount("Divine", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(5000)                 
                
#encapsulation
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance   #_ means private

    def get_balance(self):
        return self._balance
        
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            
account = BankAccount(1000)
account.deposit(500)
account.get_balance()

#inheritance
class Animal:
    def __init__(self, name, names):
        self.name = name
        self.names = names

    def eat(self):
        print(self.name, "is eating")
        print(self.names, "is eating")

class Dog(Animal):
    def bark(self):
        print(self.name, "says woooooofffffffff")

rex = Dog("Rex", "billy")
rex.eat()
rex.bark()  

#polymorphism,same method name that behaves differnetly
class Dog:
    def speak(self):
        print("Wooooooofffffff")
class Cat:
    def speak(self):
        print("Meeeoooowwww")        
for animal in [Dog(), Cat()]:
    animal.speak()
            

