
# Test
# def any_name(parameter, parameter2 = "default"):
#     """
#     Docstring, inget av detta kommer skrivas ut.
#     """
#     print(parameter)

# ----------------------------------
# Hello Funktion

# def hello():
#     print("Hello")


# hello()

# ----------------------------------

# def giveMeHello():
#     return "hello you!"

# res = giveMeHello()
# print(res)
# ----------------------------------

# def giveMeHello():
#     return "hello you!"

# res = giveMeHello()
# print(giveMeHello())

# ----------------------------------
# number = 3

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# 
# Jobbigt att reppetera flera gånger DRY DRY DRY

# def evenCheck(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "odd"
    
# print(evenCheck(10))
# print(evenCheck(5))
# print(evenCheck(2))

# Samma som ovan men singel line expression. 
# def evenCheck(number):
#     print(number%2 == 0)
    
# evenCheck(10)
# evenCheck(5)
# evenCheck(2)

# ----------------------------------


# def helloYou(name = "John"):
#     return("Hello " + name)
# res = helloYou("Bob")
# tes = helloYou()
# print(res)
# print(tes)

# ----------------------------------

# def addEvenOnly(num1, num2):
#     if (num1 % num2 != 0) or (num2 % num2 != 0):
#         return False
#     else:
#         return num1 + num2


# x = addEvenOnly(4,4)
# y = addEvenOnly(3,6)
# print(x)
# print(y)

# ----------------------------------

# def func(a,b,c=10,d=11):
#     print(a,b,c,d)

# func(2,5)
# func(2,5,7)
# func(2,5,7,9)
# func(c= "c", a = "a", d="d", b= "b")
# func(2,5,d=9)
# # kommer gå i ordning a,b,c,d
# # Kommer let upp a,b,c,d i ordning och skiva ut det

# ----------------------------------
# # Global Variabel
# x = 10
# # Lokal variabel
# def myFunc():
#     x=5
#     print(x)

# myFunc()
# print(x)

# ----------------------------------

# # Överkurs!
# # args med stjärna. Kan lägga in hur mång värden som helst. skriver ut det i en tuple. 
# def func(*args):
#     print(args)

# func(1,2,3,4,56,6,45)

# ----------------------------------

# kwargs med dubbel stjärnor.

# def func2(a,b,**kwargs):
#     print(a,b, kwargs["c"], kwargs["d"])
# func2(1,2,c=23,)

# ----------------------------------
# om inte C eller D skriv
# def func2(a,b,**kwargs):
#     print(a,b)
#     if "c" in kwargs:
#         print(kwargs["c"])
#     if "d" in kwargs:
#         print(kwargs["d"])

# func2(1,2,c=14)
# ----------------------------------

# def func3(a,b,*args,name="john", **kwargs):
#     print(f"a = {a}")
#     print(f"b = {b}")
#     print(f"args = {args}")
#     print(f"name = {name}")
#     print(f"kwargs = {kwargs}")

# func3(1,2,3, name="anna", age = 25, email = "anna@gmail.com")
