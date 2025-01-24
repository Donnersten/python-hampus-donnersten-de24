

# Operationer

# + = Plus
# - = Minus
# / = Divition
# % = Modelus
# ** = Upphöjt
# // = Heltalsdivition
# == = Likamed
#  
# Exempel 1
# print(5+2)
# def adder(num1,num2):  #Addition mellan 2 parametrar.
#     return num1+num2

# # Rör ej

# print(adder(2,5))  
# print(adder(7,9))

# --------------------------------------
# Inbyggda Metoder 
# len() = 
# .upper = 
# .lower =
#
#
# 
#  x = "Hello"
# # print(len(x))

# def length(x):
#     return len(x)

# print(length("Hello"))


# print(x.upper())
# print(x.lower())
# print(x.split("e")) #delar upp strängen vid e men e kommer försvinna

# --------------------------------------
# Variabler

# namn = "Alice" #Deklarear och initsialiserar
# ålder = 30

# print("Namn", namn)
# print("Ålder", ålder)


# ålder = ålder + 1
# ålder += 1 #Båda funkar bra med denna är bätter. 

# print(f"Uppdaterad ålder: {ålder}")

# --------------------------------------
# Andvänadandet av hakparatecer []
# Index

# Stängmetoder

# a = "Hello world"
# print(a[0]) #Bara Första Bokstaven 
# print(a[1]) #Bara Andra bokstaven 
# print(a[1:]) #Hela order förutom Fösta bokstaven
# print(a[:3]) #Bara 3 första 
# print(a[:]) #Hela strängen
# print(a[-1]) # Bara sista
# print(a[-3:]) # bara 3 sista 
# print(a[::2]) # Stegar varranat ord 

# --------------------------------------
# Muteble och Inmuteble

# Stäng = inmuteble
# Lista = Muteble
# Tuple = Inmuteble

# a = "Hello world"

# # a[0] = "x" Funkar inte att byta ut H mot x

# a = a + "!" #konkatinera 
# print(a)

# --------------------------------------

# f stäng / Formaterade stängar
# name = "Alice"
# age = 30
# print(f"My name is {name} and I'm {age} years old")

# --------------------------------------
# 
# If, elif och else

# if 1 < 2:
#     print("YES")
# else:
#     print("NO")

#Exemple tenta:
# def comparer(num1,num2):
#     if num1 < num2:
#         return "Yes!"
#     else:
#         return "No!"

# # Rör Ej!!!
# print(comparer(1,2)) #["Yes!"] - Vad som förväntas
# print(comparer(4,3)) #["No!"] - Vad som förväntas

# # Exempel 2
# if 1 == 2:
#     print("first")
# elif 3 == 3:
#     print("middel")
# else:
#     print("last")


# --------------------------------------
#  And, or

# name = "Alice"
# age = 35

# if age == 35 and name == "Alice":
#     print("Välkommen")
# elif age == 35 or name == "Alice":
#     print("Något av kaven uppfylls inte")
# else:
#     print("Inga krav uppfylls")

# --------------------------------------

# For - Loopar

# for i in range(10):
#     print(i)

# for i in range(2,10): #Från 2 till 9 
#     print(i)

# for i in range(2,10,2): #Från 2 till 9 och hopper varannan siffra
#     print(i)

# --------------------------------------
# Lista = []
#print(lista[0]) #Bara Första i listan 
# print(lista[1]) #Bara Andra i listan 
# print(lista[1:]) #Hela listan förutom Fösta i listan
# print(lista[:3]) #Bara 3 första 
# print(lista[:]) #Hela listan
# print(lista[-1]) # Bara sista
# print(lista[-3:]) # bara 3 sista 
# print(lisat[::2]) # Stegar varranat i listan 
# 
# lista = [1, True,None, "Sträng", 2.5]

# for i in lista:
#     print(i)    # Kommer skiva ut allt i listan

# Exempel Tenta func:
# def lister(lista):
#     my_list = []
#     for i in lista:
#         my_list.append(i)
#     return my_list
    

# print(lister([1, True,None, "Sträng", 2.5])) # Förväntas [1,True,None,"Sträng,2.5"]

# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Loopen Avslutades")

# --------------------------------------
# While - Loop

# guess = input("Vilken är den mest populära Pizzatoppingen?\n")

# while guess != "ost":
#     print("Fel! Inte rätt toppping")
#     guess = input("Vilken är den mest populära Pizzatoppingen?\n")

# print("Rätt svar! Ost är den populäraste toppingen!")

#Exempel Tenta func:
# def gissa_topping(guess):
#     while guess != "ost":
#         return "Fel! Det är inte rätt svar."
    
#     return "Rätt svar! Ost är den mest populära toppingen!"

# #Rör Ej!
# test1 = gissa_topping("skinka") # [Fel! Det är inte rätt svar.]
# print(test1)

# test2 = gissa_topping("ost") #[Rätt svar! Ost är den mest populära toppingen!]
# print(test2)

# --------------------------------------
#

# my_list = [0,1,2,"0", "text", True]

# print(my_list +["new item"])

# print(my_list)

# my_list += ["new item"] # Lägger till permanent

# print(my_list)

# print(my_list * 2) #Skirver ut samma lista 2 gånger i samma lista

# lista = [1,2,3]

# lista.append("append me")
# lista.pop(0) # Ta bort inligt index
# print(lista[1:]) #Skiver bara ut 2,3 och "append me" som vi la till itidigare
# lista.remove("append me") # Ta bort specifikt VAD 
# print(lista)

# new_list = ["a", "e", "x", "b", "c"]

# new_list.reverse()
# print(new_list)

# new_list.sort()
# print(new_list)

# --------------------------------------
# Dictionary

# my_dictionary = {
#     1: "value one",
#     2: "value two",
#     3: "value tree"
# }

# print(my_dictionary[2])
# print(my_dictionary[3].upper())
# print(my_dictionary[1].title())

# new_dict = {}

# new_dict["animal"] = "cat"

# print(new_dict)

# Exempel tenat func
# def ceratedict(new_dictionary,animal,typeanimal):   #Står det 3 olika parametrar så måste jag andvända 3.
#     new_dictionary[animal] = typeanimal
#     return new_dictionary

# # #Rör Ej !!!
# print(ceratedict({}, "animal", "cat"))   # Förväntas {"animal":"cat"}

# dictionary = {
#     "key one": 1,
#     "key two": 2,
#     "key tree": 3
# }

# for key,value in dictionary.items():
#     print(f"{key}:{value}")
    

# print(dictionary.keys())
# print(dictionary.values())
# print(dictionary.items())

def filter_greater_than_five(lst):
        sum = []
        for i in lst:
            if i > 5:
                  sum.append(i)
        return sum 
    

print(filter_greater_than_five([1, 6, 3, 7, 5]))