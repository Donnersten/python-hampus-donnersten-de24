import requests

response = requests.get("https://fakestoreapi.com/products")

def menyQuest():
    print()
    print("Meny") 
    print("1. Visa alla prudukter")
    print("2. Visa produktdetaljer")
    print("3. Lägg till en ny produkt")
    print("4. Avsluta")

def getTitle():
    if response.status_code == 200:
        data = response.json()
        for pruduct in data:
          print(f"{pruduct["id"]}. {pruduct["title"]}")
        
    else:
        print(f"Error fetching products. Status code {response.status_code}")

def getprducts():
    pruduct_id = int(input("Ange product-ID du vill se: "))
    filterd = requests.get(f"https://fakestoreapi.com/products/{pruduct_id}")
    if filterd.status_code == 200:
        data = filterd.json()
        print(f"Produktnamn: {data["title"]}")
        print(f"Pris: {data["price"]}")
        print(f"Beskrivning: {data["description"]}")
        print(f"Kategori: {data["category"]}")
    else:
        print(f"Något gick fel. Statuskod: {filterd.status_code}")
    

def addNewProduct():
    url = ("https://fakestoreapi.com/products")
    product_title = input("Ange produktnamn: ")
    product_price = float(input("Ange pris: "))
    product_details = input("Ange produktbeskrivning: ")
    product_category = input("Ange kategori: ")
    
    new_product_details = {
        "title": product_title, 
        "price": product_price, 
        "description": product_details, 
        "category": product_category
    }

    new_product = requests.post(url, json=new_product_details)
    if new_product.status_code == 200:
        print("Produkt tillagd:", new_product.json())
    else:
        print(f"Något gick fel. Statuskod: {new_product.status_code}")


def meny():  
    menyQuest()
    meny_input = int(input("Välj ett val 1-4: "))
    
    while True:
        if  meny_input == 4:
          break
        elif meny_input == 1:
            getTitle()
            menyQuest()
            meny_input = int(input("Välj ett val 1-4: "))
        elif meny_input == 2:
            getprducts()
            menyQuest()
            meny_input = int(input("Välj ett val 1-4: "))
        elif meny_input == 3:
            addNewProduct()
            menyQuest()
            meny_input = int(input("Välj ett val 1-4: "))
           

meny()




