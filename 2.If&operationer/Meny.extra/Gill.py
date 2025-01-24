print("11ans Torggrill")
user_input = input("Vad vill du äta?\n")

lövbiff = 130
kycklingspett = 110
schnitzel = 120
chicken_nuggets = 95
grillad_kyckling = 115
extra_löv = 50
dipp_cost = 5
grill_check = True

if user_input == "l":
        while grill_check:
                if user_input == "l":
                        löv_b = input("Bea?\n")
                        löv_v = input("Viltöksås?\n")
                        löv_vitlökssmör = input("Vitlökssmör\n")
                        löv_extra = input("Exta kött?\n")
                        grill_check = False
        if user_input == "l" and löv_extra == "ja":
                total_pris_lövbiff = lövbiff + extra_löv
                print(f"prset är {total_pris_lövbiff} kr")
        else:
                print(f"priset är {lövbiff} kr")

# Fortsätt med while loop på alla kategorier och gör samma med if satsen. 
elif user_input == "s":
        while grill_check:
                if user_input == "s":
                        schnitzel_r = input("Remouladsås?(ja/nej)\n")
                        schnitzel_m = input("Majonäs?(ja/nej)\n")
                        grill_check = False
        else:
                print(f"priset är {schnitzel} kr")

elif user_input == "cn":
        while grill_check:
                if user_input == "cn":
                        chicken_dipp_free = input("vilken sås önskas?(sweet and sour, BBQ, taco, vitlök eller Szechuan)\n")
                        dipp = input("Extra dipp?(ja/nej)")
                        if dipp == "ja":
                                extra_dipp = int(input("hur många extra önskas?\n"))
                        grill_check = False
        if user_input == "cn" and dipp == "ja":
                total_pris_cn = chicken_nuggets + dipp_cost * extra_dipp
                print(f"priset är {total_pris_cn} kr")
        else:
                print(f"priset är {chicken_nuggets} kr")

elif user_input == "gk":
        while grill_check:
                if user_input == "gk":
                        gk_extra = input("pommer eller potatis mos (p/pm)\n")
                        grill_check = False
        print(f"priser är {grillad_kyckling} kr")
elif user_input == "ks":
        while grill_check:
                if user_input == "ks":
                        grill_check = False
        print(f"priset är {kycklingspett} kr")