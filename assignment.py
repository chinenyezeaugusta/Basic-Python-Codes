#book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(self.title, "by", self.author)

book1 = Book("Rich Dad Poor Dad", "Robert kiyosaki")
book2 = Book("The Alchemist", "Paulo Coelho") 



print(book1.title)
print(book2.title)
book1.describe()
book2.describe()

#movie
class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director
    def describe(self):
        print(self.title, "directed by", self.director)

movie1 = Movie("Black Panther", "Ryan Coogler") 
movie2 = Movie("Barbie", "Greta Gerwig")

print(movie1.title)
print(movie2.director)      
movie1.describe()
movie2.describe()   

#phones
class Phones:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def describe(self):
        print("This is", self.brand,  self.model, "it costs", self.price)

p1 = Phones("Tecno", "Spark 30C", 160000)
p2 = Phones("Apple", "iphone 13 pro", 350000 )

print(p1.brand, p1.model)
print(p2.model)
p1.describe()
p2.describe()

#area of rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width  
       
print(Rectangle(10, 4).area())

#player
class Player:
    def __init__(self, name, club):
        self.name = name
        self.club = club

    def describe(self):
        print("My name is", self.name, "I play for", self.club) 

player1 = Player("Ronaldo", "Chelesa") 
player2 = Player("Lamine Yamal", "Barcelona")
player3 =Player ("Messi", "Man City")

player1.describe()
player2.describe()
player3.describe()

#inheritance
class Person:
    def __init__(self, name,faculty):
        self.name = name
        self.faculty = faculty
        

    def regsiter(self):
        print("I register my courses every semester") 

class Student(Person):
    def study(self):
        print("I'm studying computer science.")

student = Student("Augusta", "Physical Science")
print(student.name, "is a student in the faculty of", student.faculty) 
student.regsiter()
student.study()                 
        


        


        

     
        