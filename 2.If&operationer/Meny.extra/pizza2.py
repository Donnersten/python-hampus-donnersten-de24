print("11ans Torggrill")
user_input = input("Vad vill du äta?\n")

margherita = 100
vesuvio = 110
fungi = 110
kebbab_pizza = 125
salami = 135
pizza_check = True

small_extra = 10
large_extra = 25
lunch_m = 80
lunch_v = 90
lunch_f = 90
lunch_k = 110
lunch_s = 115

pizza_check = True

if user_input == "kp":
       while pizza_check:
            if user_input == "kp":
                lunch_tid = int(input("vad är klockan?\n"))
                kebab_vit = input("vit sås?(ja/nej)\n")
                kebab_röd = input("röd sås?(ja/nej)\n")
                extra_topping = input("Extra topping?(ja/nej)\n")
                if extra_topping == "ja":
                        s_extra_topping = int(input("antal SMÅ tillbehör (jalapeno, extra ost, bacon eller oliver)\n"))
                        l_extra_topping = int(input("antal STORA tillbehör (kebab eller skinka)\n"))
                pizza_check = False
            if user_input == "kp" and 11 < lunch_tid <= 14 and extra_topping == "ja":
                total_pris_pizza = lunch_k + (small_extra * s_extra_topping) + (large_extra * l_extra_topping)
                print(f"priset är {total_pris_pizza} kr")
            elif user_input == "kp" and 11 < lunch_tid <= 14 and extra_topping == "nej":
                  print(f"priset är {lunch_k} kr")
            elif user_input == "kp" and extra_topping == "ja" and 11 > lunch_tid >= 15:
                total_pris_pizza = kebbab_pizza + small_extra * s_extra_topping + large_extra * l_extra_topping
                print(f"priset är {total_pris_pizza} kr")
            else:
                print(f"priset är {kebbab_pizza} kr")
elif user_input == "mp":
        while pizza_check:
            if user_input == "kp":
                lunch_tid = int(input("vad är klockan?"))
                pizza_check = False
        if user_input == "mp" and 11 < lunch_tid <= 14:
                print(f"priset är {lunch_m} kr")
        else:
                print(f"priset är {margherita} kr")
elif user_input == "vp":
        while pizza_check:
            if user_input == "vp":
                lunch_tid = int(input("vad är klockan?"))
                pizza_check = False
        if user_input == "vp" and 11 < lunch_tid <= 14:
                print(f"priset är {lunch_v} kr")
        else:
                print(f"priset är {vesuvio} kr")        
elif user_input == "fp":
        while pizza_check:
            if user_input == "fp":
                lunch_tid = int(input("vad är klockan?"))
                pizza_check = False
        if user_input == "fp" and 11 < lunch_tid <= 14:
                print(f"priset är {lunch_f} kr")
        else:
                print(f"priset är {fungi} kr")      
elif user_input == "sp":
        while pizza_check:
            if user_input == "sp":
                lunch_tid = int(input("vad är klockan?"))
                pizza_check = False
        if user_input == "sp" and 11 < lunch_tid <= 14:
                print(f"priset är {lunch_s} kr")
        else:
                print(f"priset är {salami} kr")         
                                        
                