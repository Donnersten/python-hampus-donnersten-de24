# Övning 1. arrayCheck Funktion
# Givet en lista av heltal, returnera True om sekvensen av siffrorna 1, 2, 3 förekommer någonstans i listan.


# def arrayCheck(num):
#     for i in range(len(num)-2):
#         if num[i] == 1 and num[i+1] == 2 and num[i+2] == 3:
#             return True
#         else:
#             return False
# print(arrayCheck([1,2,3,4,5]))
        
# def arrayCheck(nums):
#     for i in range(len(nums)-2):
#         if nums[i] == 1 and nums[i+1]== 2 and nums[i+2] == 3:
#             return True
#     return False

# print(arrayCheck([1, 1, 2, 3, 1]))
# print(arrayCheck([1, 1, 2, 4, 1]))
# print(arrayCheck([1, 1, 2, 1, 2, 3]))
# ----------------------------------------------------
# Fråga 2. stringBits Funktion
# Givet en sträng, returnera en ny sträng skapad av varannan bokstav, med början från den första

# def stringBits(name):
#     return name[::2]

# print(stringBits("hello"))

# ----------------------------------------------------
# Fråga 3. doubleChar Funktion:
# Givet en sträng, returnera en sträng där varje bokstav i originalsträngen förekommer två gånger

# def doubleChar(name):
#     dubble = ""
#     for i in name:
#         dubble += i*2
#     return dubble

# print(doubleChar("the"))
# print(doubleChar("AAbb"))
# print(doubleChar('Hi-There'))

# ----------------------------------------------------
# Fråga 4. count_evens Funktion:
# Returnera antalet jämna heltal i den givna listan.

# def count_evens(number):
#     count = 0
#     for i in number:
#       if i % 2 == 0:
#          count += 1
#     return count
      
    
# print(count_evens([2, 1, 2, 3, 4]))
# print(count_evens([2, 2, 0]))
# print(count_evens([1, 3, 5]))

# ----------------------------------------------------
# Fråga 5. Spel
# Ni ska göra ett enkelt spel i kommandoraden som kombinerar vad ni har lärt er hittills om Python.
# Spelet går ut på följande:
# 1. Datorn tänker på ett tresiffrigt nummer som inte har några upprepande siffror.
# 2. Du ska sedan gissa ett tresiffrigt nummer.
# 3. Datorn kommer då att ge tillbaka ledtrådar. De möjliga ledtrådarna är:
# 4. Baserat på dessa ledtrådar kommer du att gissa igen tills du bryter koden med en perfektgissning!

import random
 
def gameGuess():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]
 
def tryAgain():
    for i in range(3):
        guess = int(input("Vad är din gissning? "))
        player.append(guess)
 
lista1 = gameGuess()
print(lista1)

player = []

        
 
def playGame():
 
    ratt_position = 0
    fel_position = 0
    attempts = 0
    
 
    for i in range(3):
        guess = int(input("Vad är din gissning? "))
        player.append(guess)
 
    while True:
        for i in range(len(lista1)):
            if lista1[i] == player[i]:
                ratt_position += 1  
            elif lista1[i] in player:
                fel_position += 1  
 
        if ratt_position == len(lista1):
            print(f"Alla tal är rätt och på rätt position! Det tog {attempts} försök!")
            break
        elif fel_position > 0 and ratt_position > 0:
            print(f"{fel_position} tal är rätt men på fel position, {ratt_position} tal är på rätt position")
            attempts += 1
            player.clear()
            ratt_position = 0
            fel_position = 0
            tryAgain()
        elif ratt_position > 0:
            print(f"{ratt_position} tal är på rätt position.")
            attempts += 1
            player.clear()
            ratt_position = 0
            fel_position = 0
            tryAgain()
        elif fel_position > 0:
            print(f"{fel_position} tal är rätt men på fel position.")
            attempts += 1
            player.clear()
            ratt_position = 0
            fel_position = 0
            tryAgain()
        elif ratt_position == 0 and fel_position == 0:
            print("Inga tal är rätt.")
            attempts += 1
            player.clear()
            ratt_position = 0
            fel_position = 0
            tryAgain()
 
playGame()