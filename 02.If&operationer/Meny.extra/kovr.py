print("11ans Torggrill")
user_input = input("Vad vill du äta?\n")

korv_pris = 20
rostad_lök = 5
räksallad = 15
korv_check = True

     
if user_input == "v":
        while korv_check:
                if user_input == "v":
                        korv_K = input("ketshup?(ja/nej)\n")
                        korv_S = input("Senap?(ja/nej)\n")
                        korv_extra2 = input("rostadlök?(ja/nej)\n")
                        korv_extra3 = input("Räksallad?(ja/nej)\n")
                        korv_check = False

        if user_input == "v" and korv_extra2 == "ja" and korv_extra3 == "ja":
                        total_pris_korv = korv_pris + rostad_lök + räksallad
                        print(f"priset är {total_pris_korv}")
        elif user_input == "v" and korv_extra2 == "ja":
                        total_pris_korv = korv_pris + rostad_lök
                        print(f"prister är {total_pris_korv}")
        elif user_input == "v" and korv_extra3 == "ja":
                        total_pris_korv = korv_pris + räksallad
                        print(f"priset är {total_pris_korv}")
        else:
                print(f"priset är {korv_pris}") 
    
