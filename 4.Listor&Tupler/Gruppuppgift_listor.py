# Fråga 1
# lista = []
# for i in range(4):
#     tal = int(input("Skriv ett tal"))
#     lista.append(tal)
#     lista.sort()
    
# print(lista[-1])

# ------------------------
# Fråga 2
# lista = []
# for i in range(3):
#     tal1 = int(input("Skriv ett tal: "))
#     lista.append(tal1)
#     lista.sort()
# min_tal = min(lista)
# max_tal = max(lista)

# print(f"minsta talet är {min_tal} och största är {max_tal}")
# print(f"medianen är {lista[1]}")
# ------------------------
# Fråga 3
# lista = [15, 18 ,5, 99, 44,32 ,24, 12, 77, 89]
# guess = int(input("Gissa ett heltal: "))

# if guess in lista:
#     print("Ha, vilken tur du har, du gissa rätt! Är en på 10 att det sker!")  
# else:
#     print(" Aj då, bättre lycka nästa gång!")
    
# ------------------------
# Fråga 4

# lista_djur = ("hund", "katt", "häst","kyckling", "panda")
# user_list = ([])
# andvändardjur = input("Skriv 3 favorit djur: ").lower().split(",")
# andvändardjurdjur = [djur.strip() for djur in andvändardjur]

# gemensamma = 0
# for djur in andvändardjur:
#     if djur in lista_djur:
#         gemensamma += 1

# print(f"Vi har {gemensamma} gemensamma favoritdjur")            


# ------------------------
# Fråga 5
# user_list =[]
# while True:
#     print("\nVälj ett alternativ:")
#     print("1. Add (Lägg till vara)")
#     print("2. Remove (Ta bort vara)")
#     print("3. Edit (Redigera vara)")
#     print("4. Print shopping list (Skriv ut shoppinglistan)")
#     print("5. Insert (Sätt in vara på viss plats)")
#     print("6. Reversed (Skriv ut listan baklänges)")
#     print("7. Sorted (Skriv ut listan sorterad)")
#     print("8. Delete shopping list (Radera hela listan)")
#     print("0. Exit (Avsluta)")
#     user_input = input("Skriv in vad vill du göra: ")

#     if user_input == "1":
#         add = input("vad vill du lägga till i listan?: ")
#         user_list.append(user_input)
#         user_input = input("Skriv in vad vill du göra: ")
    
#     elif user_input == "2":
#         if user_input == "2":
#             remove = input("vad vill du ta bort?: ")
#             user_list.remove(remove)
#             user_input = input("Skriv in vad vill du göra: ")
#         else:
#             print(f"{user_input} finns inte i listan")

# Fråga 6
bank_acc = {}

while True:
    print("1. Skapa konto")
    print("2. Ta bort konto")
    print("3. Lista alla kontonummer")
    print("4. Lista totalsaldo")
    print("5. Lista alla kontonummer och saldo}")
    print("9. Avsluta")
    user_input = input("Väl ett alternativ: ")

    if user_input == "1":
        nytt_kontonummer = int(input("skiv ett kontonummer: "))
        nytt_saldo = int(input("Hur mycket pengar har du?: "))
        bank_acc[nytt_kontonummer] = nytt_saldo
        print(f"Ditt konto är skapat")
    elif user_input == "2":
            delete_konto = int(input("Vilket kontot vill du radera?: "))
            if delete_konto in bank_acc:
                bank_acc.pop(delete_konto)
                print(f"konto {delete_konto} är raderat")
            else:
             print("kotot finns inte")
    elif user_input == "3":
            if bank_acc:
                 print("kontonummer: ")
                 for nytt_kontonummer in bank_acc.keys():
                    print(f"Konto: {nytt_kontonummer}")
    elif user_input == "4":
        saldo = 0
        for value in bank_acc.values():
            saldo += value
        print(saldo)
    elif user_input == "5":
        if bank_acc:
              print("kontonummer och saldo: ")
              for nytt_kontonummer, nytt_saldo in bank_acc.items():
                print(f"Konto {nytt_kontonummer} och {nytt_saldo} SEK")
        else:
             print("Finns inga konton")
    elif user_input == "9":
         break
    else:
         print("Felaktigt alternativ, prova igen. \n")
    
    # Fortsätt på input "5" den funkar inte