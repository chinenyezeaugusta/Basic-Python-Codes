# #formatting
name = "Augusta"
age = 45
gpa = 4.59
is_active: bool = True
print(f"{name} is {age} years old with a GPA of {gpa:.2f}")

# #conditionals
if gpa >= 4.5:
    grade_class = "First Class"
elif gpa >= 3.5:
    grade_class = "Second Class Upper"   
elif gpa >= 2.4:
    grade_class = "Second Class Lower"  
else :
    grade_class = "Third Class or Pass"  


# #Lists
Courses = ["CSC 201", "CSC 205"]
Courses.append("IFT 212")
print(Courses)

#dictionaries

user = {"id": 7, "username": "Augusta", "roles": ["student"]}
user["email"] = "augusta@gmail.com"
print(user.get("phone", "not found"))
for key, value in user.items():
    print(key, "=>", value)

#sets
tags = {"python", "django", "python"}
required = {"python" ,"Sql"}
print(required - tags)

#functions
def calculate_total (prices: list[float], discount: float = 0.0):
    """ Return the total after applying a percentage discount"""
    subtotal = sum(prices)
    return round(subtotal * (1 - discount / 100),2)
calculate_total([1000, 2500])
calculate_total([1000, 2500], discount=10)
