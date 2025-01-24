
# for - loop

# lista =[1, True, None, "String", 2.5]

# for i in lista:
#     print(i)
# ----------------------
# lista = [1,2,3,4,5]

# for i in lista:
#     print("yes")

# ----------------------

# lista = [1,2,3,4,5]
# for hej in lista:
#     print(hej + hej)

# --------------------
# for i in range(10):
#     print(i)

# for i in range(1,10):
#     print(i)

# for i in range(3,10,1):
#     print(i)

# for i in range(1,11):
#     print(i**2)

# for i in range(21):
#     if i % 2 == 0:
#         print(i)

# ------------------------------------------
# while - loop 

# guess = input("vilket är det bästa lagert?\n")

# while guess != "DIF":
#     print("DU HAR FEL!")
#     guess = input("Vilket är det bästa laget?\n")

# print("Grattis du har rätt")
# ------------------------------------------

# Kontrollsattser

# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("loopen avslutades")
# Skirver ut fram till 3 sen slutar loopen

# for i in range(5):
#     if i == 2:
#         continue
#     print(i)
# # Skriver inte UT 2 men fortätter till index 5 0-4

# -------------------------------------------

# Nässaldloop (loop i en loop)

# for i in range(3):
#     for j in range(2):
#         print(f"i = {i} och j = {j}")
# # Den andra loopen måsre köra klart innan den kommer gå över till första loopen. 