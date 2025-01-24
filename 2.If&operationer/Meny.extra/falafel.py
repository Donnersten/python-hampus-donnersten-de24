print("11ans Torggrill")
user_input = input("Vad vill du äta?\n")
total_pris_ft = 0
falafel_talrik = 95
falafel_check = True

if user_input == "ft":
    while falafel_check:
        if user_input == "ft":
            total_pris_ft = falafel_talrik + total_pris_ft
            falafel_check = False
print(f"Priset är {total_pris_ft} kr")
