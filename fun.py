#greet
def greet(name):
    print("Welcome to our website " + name )

greet("Augusta")
greet("Divine")

#addition
def add(a, b):
    print(a + b)

add(3, + 7 )
add(16, + 4)

#courses
def courses(course_name):
    print("Register " + course_name, "On Your Portal")

courses("CSC 201")
courses("SEN 211")
courses("IFT 212")

#cart
def cart(items):
    print("Add " + items, "To cart")
   
cart("Electric Fan")
cart("Airpod")
cart("Laptop")

def introduce(name, age):
    print(name, "is", age, "years old")

introduce("Esther",  30 )    

#return
def add(a, b):
    return a + b
result = add(2, 3)
print(result)
print(add(10, 5) * 2)

#print vs return
def add_print(a, b):
   
    print(a + b)

def add_return(a, b):
    return a + b

x = add_print(2, 3)
y = add_return(2, 3)

print(x)
print(y)

#early_return

def check_age(age):
    if age >= 18:
        return "Adult"
    return "Minor"

print(check_age(25))
print(check_age(12))

#default
def greet(name, greeting="Hello"):
    print(greeting + "," + name + "!")

greet("Ada")
greet("Precious", "Good morning")

#keywords arg
def describe_pet(animal, name):
    print("I have a", animal, "called", name)
describe_pet("dog", "Esther")    
describe_pet(name="Esther", animal="dog")

#local variable
def make_message():
    message = "I live inside the function"
    print(message)

make_message()

#global variable
school = "TechRise"

def show_school():
    print("I study at", school)

show_school()

#grades
def average(scores):
    return sum (scores) / len(scores)

def get_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"
    
def report(name, scores, school="TechRise"):
        avg = average(scores)
        grade = get_grade(avg)
        print(name, "from", school)
        print("Average:", round(avg, 2), "Grade", grade)

report("Augusta", [40, 80, 68])    
report("Miriam", [45, 90, 70], school="Ashpot")
report("Divine", [90, 80, 50])

#assessment
def name(name):
    print("my name is", name)

name("Augusta") 

#
def square(a, b):
    return a * b
result = square(7, 7)
print(result)

#
def is_even(even):
    if even <= 10:
        return "True"
    return "False"

print(is_even(6))
print(is_even(15))

#
def area(l, w):
    return l + w
result =(add(5, + 3) * 2)
print(result)

#
def welcome(name, city ="Kano"):
    print("Welcome ",  name, "from ", city )

welcome("Splendour")
welcome("Gabriel", city="Damaturu")

#
def double(x):
    return x * 2
#2 is not assigned ; x cannot multiply 2

#
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))




     

    
