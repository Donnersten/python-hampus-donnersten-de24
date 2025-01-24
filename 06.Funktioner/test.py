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