
# for i in range(1,21):
#     if i % 2 == 1: 
#         continue
#     print(i)


# successful = False
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times anf fail")

# Nessted-loop
# for x in range(5):
#     for y in range(3):
#         print(f"({x},{y})")

# Komplex type
# range = type range

# for x in "python":
#     print(x)

# for y in [1,2,3,4,5]:
#     print(y)
# count = 0 
# for i in range(1,10):
#     if i % 2 == 0:
#         count += 1
#         print(i)
# print(f"We have {count} even numbers")

# ---------------------------------------
# Fråga 3

# for i in range(1,11):
#     print(i)
# user_input = int(input("Enter number: \n"))
# summa = 0
# for i in range(1,user_input +1,1): 
#     summa += i
# print(summa)
# Totalen av 1+2+3+4+5+6+7+8+9+10
# -----------------------------------------
# Fråga 4
# 2ans multiplikationstabell 

# n = 2

# for i in range(1,11):
#     p = n*i
#     print(p)
# --------------------------------------------
# While - Loop youtube

# name = input("Enter namne\n")

# while name == "":
#     print("you dident put in a namn")
#     name = input("Enter namne:\n")
# else:
#     print(f"hello {name}")

# age = int(input("Whats your age?: "))

# while age < 21:
#     print("Du är för ung för att handla på Systemet!")
#     age = int(input("Whats your age?: "))
# print(f"Du är {age} år, du kan handla på Systemet!")

# food = input("vad gilla du för med (q to quit)\n")

# while food != "q":
#     print(f"du gillar {food}")
#     food = input("vad gilla du för med (q to quit)\n")

# num = int(input("ange ett tal mellan 1-10: \n"))

# while num < 1 or num > 10:
#     print(f"{num} inte gilltigt")
#     num = int(input("ange ett tal mellan 1-10: \n"))
# print(f"ditt nummer {num}")