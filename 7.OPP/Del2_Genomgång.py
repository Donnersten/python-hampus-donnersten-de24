
# Metoder

# class Point:
#     def __init__(self, x,y):
#         self.x = x
#         self.y = y
    
#     def __repr__(self):
#         return f"point(x = {self.x} y ={self.y})"
    
#     def __str__(self):
#         return f"point-objekt med (x = {self.x} y = {self.y})"

# point1 = Point(10,20)
# point2 = Point(30,150)
# print(point1.x, point1.y)

# print(point1)
# print(point2)

#------------------------------------------

# class Point:
#     def __init__(self, x,y):
#         self.x = x
#         self.y = y

#     def __eq__(self,other):
#         return self.x == other.x and self.y == other.y


# point1 = Point(10,20)
# point2 = Point(10,20)

# print(point1 == point2)

# ------------------------------------------

# class Point:
#     def __init__(self, x,y):
#         self.x = x
#         self.y = y

#     def swap_xy(self):
#         self.x, self.y = self.y, self.x

# point1 = Point(10,20)

# point1.swap_xy()
# print(point1.x, point1.y)

# ------------------------------------------

# Arv

# class A:
#     def __init__(self,value):
#         print(f"A.__init__ has value = {value}")
#         self.valeu = value

# class B(A):
#     def __init__(self,value):    
#         print(f"B.__init__ has value = {value}")
#         super().__init__(value)
#         self.valeu += 10

# class C(A):
#     def __init__(self,value):    
#         print(f"C.__init__ has value = {value}")
#         super().__init__(value)
#         self.valeu *= 4

# class D(C,B):
#     def __init__(self,value):    
#         print(f"D-__init__ has value = {value}")
#         super().__init__(value)

# d = D(10)

# print(d.valeu)
# print(D.mro())
# # MRO metodlösningsordning.
# # D till B till C till A

# -----------------------------------------------------


# # Bas-klass (Föreälder)
# class Animals:
#     def __init__(self):
#         print("Djur skapat")
#     def WhoImI(self):
#             print("Djur")
#     def eat(self):
#          print("äter ")

# # Avledd klass (Drive class)
# class Dog(Animals):
#     def __init__(self,):
#        print("Hund skapat")

#     def WhoImI(self):
#             print("Hund")
#     def bark(self):
#          print("Voff")

# d = Dog()
# d.WhoImI()
# d.eat()
# d.bark()

# -----------------------------------------------------

# class Employee:
#     increase = 1.04
#     def __init__(self,first,last,salary):
#         self.first = first
#         self.last = last
#         self.salary = salary
    
#     def __str__(self):
#         return f"{self.first} {self.last} tjänar {self.salary} kr"

#     def increase_salary(self):
#         self.salary = int(self.salary * self.increase)

# class Developer(Employee):
#     increase = 1.10
#     def __init__(self,first,last,salary, prog):
#         super().__init__(first,last,salary)
#         self.prog = prog

#     def __str__(self):
#         return f"{super().__str__()} och kodar i {self.prog}"

# class Marketing(Employee):
#     def __init__(self,first,last,salery, depart):
#         super().__init__(first, last,salery)
#         self.depart = depart

#     def __str__(self):
#         return f"{super().__str__()} och jobbar på {self.depart}"
    
# emp1 = Employee("Alice", "Svensson", 45000)
# emp2 = Employee("Olle", "Ollesson", 42000)
# dev1 = Developer("Bob", "Bobsson", 60000, "Pyhton")
# mark1 = Marketing("Eva", "Ohlsson", 35000, "Marknadsföring")

# print(emp1)
# print(emp2)
# print(dev1)
# print(mark1)

# # Alla får löneökning
# emp1.increase_salary()
# emp2.increase_salary()
# dev1.increase_salary()
# mark1.increase_salary()

# print(emp1)
# print(emp2)
# print(dev1)
# print(mark1)

# -----------------------------------------------------
# Pollymorfism (Metodöverskuggning)
# 
# class Animal:
#     def speak(self):
#         return "Ett ljud"
    

# class Dog(Animal):
#     def speak(self):
#         return "Voff"

# class Cat(Animal):
#     def speak(self):
#         return "Mjau"

# dog = Dog()
# cat = Cat()
# animals = [dog,cat]

# for i in animals:
#     print(i.speak())

# -----------------------------------------------------
# Pollymorfism genom Duck Typing

# class Bird:
#     def make_sound(self):
#         return "Ett Ljud"
    
# class Duck(Bird):
#     def make_sound(self):
#         return "Kvack"

# class Crow(Bird):
#     def make_sound(self):
#         return "Kra"

# def lett_bird_make_sound(bird):
#     return bird.make_sound()

# duck = Duck()
# crow = Crow()

# print(lett_bird_make_sound(duck))
# print(lett_bird_make_sound(crow))

