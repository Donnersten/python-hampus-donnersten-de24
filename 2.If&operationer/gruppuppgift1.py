#Uppgift 1 

# user_input = int(input("Mata in ett tal"))
# if user_input > 10:
#     print("Talet är större än 10")
# else:
#    print("Talet är mindre än 10")

#-------------------------------------------------
# fråga 2

# user_input = int(input ("hur många mjölk paket finns det"))
# if user_input < 0:
#     print ("beställ 30 paket")
# elif user_input <= 20:
#     print("beställ 20 paket")
# else:
#     print("du behöver inte beställa mer!")


#-------------------------------------------------
# fråga 3
# number1 = int(input("mata in ett tal: "))
# number2 = int(input("mata in ett till tal: "))

# if number1 > number2:
#     largest = number1
# else:
#     largest = number2

# print(f"Det största talet är {largest}")



#-------------------------------------------------
# fråga 4


# number1 = int(input("mata in ett tal: "))
# number2 = int(input("mata in ett till tal: "))
# number3 = int(input("mata in ett till tal: "))


# if number1 > number2 and number1 > number3:
#     largest = number1
# elif number2 > number1 and number2 > number3:
#     largest = number2
# else:
#     largest= number3

# print(f"Det största talet är {largest}")
# -------------------------------------------------
# fråga 5

# user = input("vilken kategri tillhör du? ")

# if user == "student" or user == "pensionär":
#     pris = "20"
#     print (f"priset för resan är {pris} kr")
# elif user == "vuxen":
#     pris = "30" 
#     print (f"priset för resan är {pris} kr")   
# else:
#     print ("fel kategori")

#-------------------------------------------------
# fråga 6
# age = int(input("vilket år är du född? "))

# if 1980 <= age < 1990:
#     print("Du är född på 80-talet ")
# elif 1990 <= age < 2000:
#     print("du är född på 1990-talet")
# else:
#     print("du är inte född på 1980 eller 1990-talet")

#-------------------------------------------------
# fråga 7

# user = input ("vart bor du")
# user = user.lower()
# if user == "sverige" or user == "danmark" or user == "norge":
#     print ("du bor i scandinavien")
# else:
#     print ("du bor inte i scandinavien")



#-------------------------------------------------
# fråga 8

# money= int(input("hur mycket pengar har du?"))
# discount=input("Hur mycket rabatt har du?")

# if 15 <= money <= 25 and discount == "nej":
#     print("du kan köpa en liten hamburgare")
# elif 15 <= money <= 25 and discount == "ja":
#     print("Du kan köpa en liten hamburgare och en pommes")
# elif 25 < money <= 50 and discount == "nej":
#     print("du kan köpa en stor hamburgre")
# elif 25 < money <= 50 and discount == "ja":
#     print("Du kan köpa en stor hamburgare och en pommer")
# elif money >= 50 and discount == "ja":
#     print("Du kan köpa ett meal!")
# else:
#     print("du kan inte köpa något")


#-------------------------------------------------
# fråga 9

# temp_svedala = float(input("mata in temperaturen i Svedala: "))
# temp_jukkas= float(input("mata in temperaturen i Jukkasjärvi: "))
# temp_visby = float(input("mata in temperaturen i Visby: "))


# min_temp = min(temp_jukkas, temp_svedala, temp_visby)
# max_temp = max(temp_visby, temp_jukkas, temp_svedala)
# medel_temp = (temp_jukkas + temp_svedala + temp_visby) / 3

# if min_temp == temp_svedala:
#     coldest_place = "Svedala"
# elif min_temp == temp_jukkas:
#     coldest_place = "Jukkasjärvi"
# else:
#     coldest_place = "visby"

# if min_temp == temp_svedala:
#     warmest_place = "Svedala"
# elif min_temp == temp_jukkas:
#     warmest_place = "Jukkasjärvi"
# else:
#     warmest_place = "visby"

# print(f"Det är kallast i {coldest_place}")
# print(f"Det är varmast i {warmest_place}")
# print(f"medeltemperaturen är {medel_temp} grader")

#--------------------------------------------------
# Fråga 10
# password = input("Skriv ett lösenord: (minst 8 bokstäver)").replace(" ","")

# if len(password) >= 8:
#     print("Lösenordet är skapat")
# else:
#     print("Lösenord uppfyller inte kraven.")
    


# --------------------------------------------------
# Fråga 11
# c_temp = int(input("ange temperaturen i C: "))
# edit_temp = input("vill du konvertera temperaturen till Fahrenheit eller Kelvin?(K eller F eller N): ").upper()

# if edit_temp == "F":
#     f_temp = c_temp * 9/5 + 32
#     print(f"temperaturen till Fahrenheit är {f_temp}")
# elif edit_temp == "K":
#     k_temp = c_temp + 273.15
#     print(f"Kelvin temperaturen är {k_temp}")
# elif edit_temp == "N":
#     print(f"temperaturen är {c_temp}")
# else:
#     print("Ogiltigt val")



# ---------------------------------------------------
# Fråga 12 
# while True: 
#     try: 
#         tal1 = int(input("Ange ett tal: "))
#         mini = input("Vilken operation vill du utföra? (+, -, *, /)")
#         tal2 = int(input("Ange ett till tal: "))
#         break
#     except ValueError:
#         print("Fel, Du måste ange ett tal.")

# if mini == "+":
#     plus = tal1 + tal2
#     print(f"svaret är {plus}")
# elif mini == "-":
#     minus = tal1 - tal2
#     print(f"svaret är {minus}")
# elif mini == "*":
#     multi = tal1 * tal2
#     print(f"svaret är {multi}")
# elif mini == "/" and tal2 != 0: 
#     div = tal1 / tal2
#     print(f"svaret är {div}")
# else:
#     print("Ogiltigt operation")


# ändrade rad 171 från > 0 till != 0 
# ------------- KOLLA PÅ LEKTION -------------------

# --------------------------------------------------
# Fråga 13 
# pris = int(input("Ange pris: "))
# rabatt = int(input("Ange rabatt: "))

# if rabatt < 50:
#     nytt_pris = pris - rabatt / 100 * pris
#     print(f"Det nya priset efter rabatten är {nytt_pris} kr")
# else:
#     print("Rabatten är för hög, det nya priset kan inte beräknas")


# --------------------------------------------------
# Fråga 14

# veckodagar = ["måndag", "tisdag", "onsdag", "torsdag", "fredag",]

# vecka = input("mata in veckodag: ").lower()
# tid = int(input("Mata in tiden(24h format): "))

# if vecka in veckodagar:
#     if 9 <= tid <= 18:
#         print("butiken är öppen")
#     else:
#         print("Det är stängt")
# elif vecka == "lördag":
#     if 10 <= tid <= 14:
#         print("Butikrn är Öppen")
#     else:
#         print("Det är stängt")
# else:
#     print("Det är stängt")
    
# -------------------------------------------------
# Fråga 15
# tal = int(input("mata in ett heltal: "))

# if tal % 2 == 0:
#     print(f"{tal} är jämnt")
# else:
#     print(f"{tal} är ojämnt")
# -------------------------------------------------
