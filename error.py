age = int(input("Enter your age: "))
print("Next year you will be", age + 1)

#try and except error
try:
    age = int(input("Enter your age: "))
    print("Next year you will be", age + 1)
except ValueError:
    print("Please enter a number, not letters")
print("The program keeps running")

try:
    a = (input("First Name:"))
    b = (input("Second Name:"))
   
    if not a or not b:
        raise ValueError("empty name")
    print(f"Welcome back {a} {b} to the team")
except ValueError:
    print("Please type full name, both first and second name.")

try:
    print(10 / 0)
except ZeroDivisionError as error:
    print("oops:", error)        

#finally 
try:
    number = int(input("Enter a number:"))
except ValueError:
    print("That is not a number.")
else:
    print("Good! You entered", number)
finally:
    print("Thank you for using the program")        


try:
    with open("notes.txt") as file:
     print(file.read())
except FileNotFoundError:
    print("notes.txt does not exist.")
finally:
    print("Done")        

#raise statement
def set_age(age):
    if age < 20:
        raise ValueError("Age must be 20 and above")
    return age
try:
    set_age(5)
except ValueError as error:
    print("Error:", error)    

#exception using class method

class InsufficientFunds(Exception):
    pass
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFunds("Your balance is too low")
    return balance - amount

try:
    withdraw(2000, 5000)
except InsufficientFunds as error:
    print(error) 

#ask_until_valid
while True:
    try:
        age = int(input("Enter your age:"))
        if age < 18:
            raise ValueError
        break
    except ValueError:
        print("Invalid age. Try again")
        
print("Your age is", age)



#age validation
try:
    age = int(input("Enter your age:"))
    if age < 18 or age > 35:
        raise ValueError("Opps, You are not eligible")
    print(" You are  qualified")

except ValueError as e:
    print(e)

#score
try:
    score = int(input("Enter your score:"))
    if score <= 50:
        raise ValueError("Yoooo, You failed")    
    print("Excellent result ")  

except ValueError as error:
    print(error)    



    
     


