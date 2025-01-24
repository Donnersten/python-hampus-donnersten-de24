
# Fråga 1

# class Maträtt:
#     def __init__(self,name,price,kcal,typ):
#         self.name = name
#         self.price = price
#         self.kcal = kcal
#         self.typ = typ
    
#     def __str__(self):
#         return f"{self.name} ({self.typ}) - {self.kcal} kcal: {self.price} kr"
    

# m1 = Maträtt("Vegetarisk Lasange",85, 600, "Vegetarisk"  )
# m2 = Maträtt("Köttbullar med Potatismos", 95, 800, "Kött")
# m3 = Maträtt("Falafel med Sallad",80, 500, "Vegansk" )
# m4 = Maträtt("Grillad Kyckling med Ris", 110, 750, "kött")

# lista = [m1,m2,m3,m4]

# print("Dagens Lunchmeny")
# for maträtt in lista:
#     print(maträtt)
# print("Dagens Lunchmeny")
# print(m1)
# print(m2)
# print(m3)
# print(m4)

# Fråga 2
class Person:
    def __init__(self,fodelsedatum):
        self.fodelsedatum = fodelsedatum
        self._name = None
        self._adress = None
        self._zipcode = None
        self._city = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name = name

    @property
    def adress(self):
        return self._adress
    
    @adress.setter
    def adress(self,adress):
        self._adress = adress

    @property
    def zipcode(self):
        return self._zipcode
    
    @zipcode.setter
    def zipcode(self,zipcode):
        self._zipcode = zipcode

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self,city):
        self._city = city

    def namer(self, changeName):
        self.name = changeName

    def changeArdess(self, newArdess, newZipcode, newCity):
        self.adress = newArdess
        self.zipcode = newZipcode
        self.city = newCity
    
    def showInfo(self):
        return f"person: {self.name} Födesedag: {self.fodelsedatum} Adress: {self.adress} Postadress: {self.zipcode} Postort {self.city} "

person1 = Person("1990-05-12")
person2 = Person("1988-12-24")

person1.namer("Anna Andersson")
person2.namer("Sven Svensson")

person1.changeArdess("sveavägen 1", "11252", "Stockholm")
person2.changeArdess("Kungsgatan 12", "21542", "Göterborg")

print(person1.showInfo())
print(person2.showInfo())

person2.changeArdess(person1.adress,person1.zipcode,person1.city)

print("\nEfter flytten:")
print(person1.showInfo())
print(person2.showInfo())

# -------------------------------------------------------
# Alternativ 2 (ChatGPT)

class Person:
    def __init__(self, fodelsedatum, name=None, adress=None, zipcode=None, city=None):
        self._fodelsedatum = fodelsedatum
        self._name = name
        self._adress = adress
        self._zipcode = zipcode
        self._city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Du kan lägga till validering eller extra logik här om det behövs för adress, zipcode eller city
    @property
    def adress(self):
        return self._adress

    @adress.setter
    def adress(self, value):
        self._adress = value

    @property
    def zipcode(self):
        return self._zipcode

    @zipcode.setter
    def zipcode(self, value):
        self._zipcode = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    def update_info(self, name=None, adress=None, zipcode=None, city=None):
        """Samlad metod för att uppdatera information på ett smidigt sätt."""
        if name:
            self._name = name
        if adress:
            self._adress = adress
        if zipcode:
            self._zipcode = zipcode
        if city:
            self._city = city

    def show_info(self):
        """Visar personens information."""
        return (f"Person: {self._name} | Född: {self._fodelsedatum} | Adress: {self._adress}, "
                f"{self._zipcode} {self._city}")

# Användning
person1 = Person("1990-05-12")
person2 = Person("1988-12-24")

person1.update_info(name="Anna Andersson", adress="Sveavägen 1", zipcode="11252", city="Stockholm")
person2.update_info(name="Sven Svensson", adress="Kungsgatan 12", zipcode="11542", city="Stockholm")

print(person1.show_info())
print(person2.show_info())

# Flyttar person2 till person1:s adress
person2.update_info(adress=person1.adress, zipcode=person1.zipcode, city=person1.city)

print("\nEfter flytten:")
print(person1.show_info())
print(person2.show_info())


