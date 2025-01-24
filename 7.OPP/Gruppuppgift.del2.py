# # Fråga 1

# class Vehicle:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.moddel = model
#         self.year = year

#     def start(self):
#         return "har startat"
#     def stop(self):
#         return "har stannat"
#     def honk(self):
#         return "och tutar"
#     def fuel_up(slef):
#         return "behöver tanka"
#     def __str__(self):
#         return f"{self.brand} {self.moddel} {self.year}"

# class Car(Vehicle):
#     def __init__(self,brand,model,year, num_door):
#         super().__init__(brand,model,year)
#         self.num_door = num_door
    
#     def rev(self):
#         return "och varavar motorn"

#     def __str__(self):
#         return f"{super().__str__()} bilen har {self.num_door} dörrar"

# class Bicycle(Vehicle):
#     def __init__(self,brand,model,year, num_gear):
#         super().__init__(brand,model,year)
#         self.num_gear = num_gear
#     def honk(self):
#         return "ringer i klockan"
    
#     def start(self):
#         return "börjar trampa"
#     def stop(self):
#         return "bromsar"
#     def fuel_up(slef):
#         return "behöver fylla på energi"

#     def __str__(self):
#         return f"{super().__str__()} cyckeln har {self.num_gear} växlar"

# class Mc(Vehicle):
#     def __init__(self,brand,model,year,engine_size, ):
#         super().__init__(brand,model,year)
#         self.engine_size = engine_size

#     def __str__(self):
#         return f"{super().__str__()} med {self.engine_size} cc"

# bil1 = Vehicle("Toyota", "Corolla", 2009)
# bil2 = Car("BMW", "M3", 2024, 4)

# cyckel1 = Bicycle("Canyon","Areo", 2020,21)

# mc1 = Mc("Yamaha", "R1", 2022, 1000)

# print(bil1, bil1.start())
# print(bil1,bil1.honk())
# print(bil2)
# print(bil2, bil2.rev())
# print(cyckel1, cyckel1.start())
# print(cyckel1, cyckel1.honk())
# print(cyckel1,cyckel1.fuel_up())
# print(cyckel1, cyckel1.stop())
# print(mc1)
# print(mc1,mc1.stop(),mc1.honk())
# print(mc1, mc1.fuel_up())

# Fråga 2

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Squere(Shape):
    def __init__(self, lenth, whith):
        self.lenth = lenth
        self.whith = whith

    def area(self):
         return self.lenth * self.whith

    def perimeter(self):
        return self.lenth * 2 + self.whith * 2


class Circle(Shape):
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * self.pi * self.radius


class Triangel(Shape):
    def __init__(self, hight, bas, side1,side2):
        self.hight = hight
        self.bas = bas
        self.side1 = side1
        self.side2 = side2

    def area(self):
       return self.bas * self.hight / 2
    
    def perimeter(self):
        return self.bas + self.side1 + self.side2


shapes = [
    Squere(5,10),
    Circle(5),
    Triangel(5,3,2,6)
]

def shape():
    for i in shapes:
        print(f"Form: {i.__class__.__name__}")
        print(f"Arean: {i.area():.2f}")
        print(f"Omkretsen: {i.perimeter()}")
        print()
    

shape()

# print(s,s.area(), s.perimeter())
# print(c,c.area(), c.perimeter())
# print(t,t.area(), t.perimeter())

# print(Squere.mro())
# print(Circle.mro())
# print(Triangel.mro())