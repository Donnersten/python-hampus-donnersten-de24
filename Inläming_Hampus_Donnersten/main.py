import smhi
import YR
def main():
    while True:
        meny()
        user_input = input("Välj ett alternativ (1,2,9): ")
        if user_input == "1":
            get_data()
            user_select = input("Välj ett alternativ (1,2,3): ")
            if user_select == "1":
                if smhi.smhiWether():
                    print("Lyckades! Data är hämtad från SMHI")
            elif user_select == "2":
                if YR.yrWether():
                    print("Lyckades! Data är hämtad från YR")
            elif user_select == "3":
                if smhi.smhiWether() == True:
                    print("Lyckades! Data är hämtad från SMHI!")
                if YR.yrWether() == True:
                    print("Lyckades! Data är hämtad från YR!")
            else:
                print("Felaktigt meny val. Prova igen!")
        elif user_input == "2":
            printData()
            user_print = input("Välj ett alternativ (1 eller 2): ")
            if user_print == "1":
                smhi.readsmhi()
            elif user_print == "2":
                YR.readYR()
            else:
                print("Felaktigt meny val. Prova igen!")
        elif user_input == "9":
            print("Programet avslutat!")
            break
        else:
            print("Felaktigt meny val. Prova igen!")

def meny():
    print()
    print("Meny")
    print("1. Hämta data")
    print("2. Skriv ut prognos")
    print("9. Avsluta")

def get_data():
    print()
    print("Välj ett alternativ")
    print("1. SMHI")
    print("2. YR")
    print("3. SMHI och YR")

def printData():
    print()
    print("Välj ett alternativ")
    print("1. SMHI")
    print("2. YR")

if __name__=="__main__":
     main()