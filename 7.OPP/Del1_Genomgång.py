
# Genomgång 16/9 2024

# ------------------------------------

# x = [1,2,3]

# print(type(x))
# print(type([]))
# print(type())
# print(type({}))
# ------------------------------------

# class Sample:
#     pass

# x = Sample()

# print(type(x))

# ------------------------------------

# class Dog:
#     def __init__(self, breed):
#         self.breed = breed

# milo = Dog(breed = "Labrador")
# frank = Dog(breed = "Huskie")

# print(milo.breed)
# print(frank.breed)
# ------------------------------------

# class Dog:
#     # calss object atributes:
#     species = "däggdjur"
#     def __init__(self, breed,name):
#         self.breed = breed
#         self.name = name

# milo = Dog("Labrador", "Milo")
# frank = Dog("Huskie", "Frank")

# print(milo.breed)
# print(milo.name)
# print(milo.species)
# print(frank.breed)
# print(frank.name)
# print(frank.species)

# ------------------------------------
# Exempel på hur man INTE GÖR i Python!!!

# class Circle:
#     pi = 3.14
#     # Cirkel initsierad med en radie (standard 1)
#     def __init__(self, radius = 1):
#         self.radius = radius
    
#     # Metod för att beräkna arian (Tänk på self)
#     def aria(self):
#         return self.radius * self.radius * Circle.pi
    
#     # metod för att Sätta radien
#     def setRadius(self,radius):
#         self.radius = radius

#     # Metod för att Hämta radien
#     def getRadius(self):
#         return self.radius
    
# c = Circle()
# c.setRadius(2.5)

# print("radien är ", c.getRadius())
# print("area är ", c.aria())

# Alternativ 2

# class Circle:
#     pi = 3.14

#     def __init__(self, radius=1):
#         self._radius = radius  # Vi använder _radius som privat attribut
    
#     # Getter för radius
#     @property
#     def radius(self):
#         return self._radius

#     # Setter för radius
#     @radius.setter
#     def radius(self, radius):
#         self._radius = radius

#     # Metod för att beräkna arean
#     def area(self):
#         return self._radius * self._radius * Circle.pi

# # Användning
# c = Circle()
# c.radius = 2  # Här används settern
# print("Radien är: ", c.radius)  # Här används gettern
# print("Arean är: ", c.area())


# ------------------------------------

# class Person:
#     def __init__(self, name,email,age):
#         self.name = name
#         self.email = email
#         self.age = age
    
#     def __str__(self):
#         return f"{self.name} är {self.age} år gammal och har e-post {self.email}"
    
# p1 = Person("Alice", "alice@email.com", 35)
# p2 = Person("Bob", "bob@email.com", 38)

# print(p1)
# print(p2)

# p1.phone = "070-123 45 67"

# print(p1.phone)
# # print(p2.phone) detta kommer inte funka

# ------------------------------------

# class Person:
#     def __init__(self, **kwargs):
#         self.__dict__ = kwargs
    
#     def __str__(self):
#         return f"{self.name} är {self.age} år gammal"

# p1 = Person(name = "Alice", age = 25)
# p2 = Person(name = "Bob", age = 38)

# print(p1)
# print(p2)

# ------------------------------------

# class SomeThing:
#     def __init__(self, data:dict):
#         self.__dict__ = data

#     def __str__(self):
#         str_rep = ""
#         for key,value in self.__dict__.items():
#             str_rep += f"{key} = {value} "
#         return str_rep

# data_dict1 = {
#     "a" : 10,
#     "b" : 20,
#     "name" : "One"
# }

# data_dict2 = {
#     "c" : 15,
#     "d" : 25,
#     "name" : "two"
# }


# s1 = SomeThing(data_dict1)
# s2 = SomeThing(data_dict2)

# print(s1)
# print(s2)