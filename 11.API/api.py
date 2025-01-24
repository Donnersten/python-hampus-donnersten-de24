

import requests

#GET (URL)

#Status Kod
    # Om OK -> Konvertera svar till JSON
    # Om EJ OK -> Felmedelande


#GET Request för att hämta prudukterna
response = requests.get("https://fakestoreapi.com/products")

if response.status_code == 200:
    products = response.json()  #konverterar till JSON
    print(f"Alla pruducter: {products}")  #Visar alla producter
else:
    print(f"Error fetching products. Status code {response.status_code}")


