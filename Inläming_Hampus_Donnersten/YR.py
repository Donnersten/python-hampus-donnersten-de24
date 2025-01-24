import requests as rq
from  datetime import datetime, timedelta
import pandas as pd

def yrWether():

    lat = 59.3099 
    lon = 18.0215
    date_today = datetime.now().strftime("%Y-%m-%dT%T")
    wether = {
         "Datum": [],
         "Timme": [],
         "Temp": [],
         "Nederbörd": [],
         "Skapad": date_today,
         "Longitude": lon,
         "Latitude": lat,
         "Leverantör": "YR"
    }
    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
    }
    response = rq.get(f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}", headers=headersList)
    if response.status_code == 200:
        response = response.json()
        response = response["properties"]["timeseries"]
    else:
        print(f"Något gick fel med YR's API! Statuskod: {response.status_code}")
        return False

    date_next_day = datetime.now() + timedelta(days=1, hours=-2)
    date_next_day = date_next_day.replace(minute=0, second=0)
    date_next_day = date_next_day.strftime("%Y-%m-%dT%H:%M:%S")
    
    date_today = datetime.now().strftime("%Y-%m-%dT%T%H:%M")

    for validtime in response:
         temp_date = validtime["time"]
         temp_date, temp_time = temp_date.split("T")
         temp_time = temp_time.split(":")
         wether["Datum"].append(temp_date)
         wether["Timme"].append(int(temp_time[0]))

         wether["Temp"].append((validtime["data"]["instant"]["details"]["air_temperature"]))
        
         if validtime["data"]["next_1_hours"]["details"]["precipitation_amount"] > 0:
            wether["Nederbörd"].append(True)
         else:
            wether["Nederbörd"].append(False)
         if date_next_day in validtime["time"]:
            break
    yr_data = pd.DataFrame(wether)
    try:
        with pd.ExcelWriter("./Data/wether.xlsx",mode="a" ,if_sheet_exists="replace", engine="openpyxl") as writer:
            yr_data.to_excel(writer, sheet_name="YR", index=False)
    except FileNotFoundError:
        yr_data = pd.DataFrame(wether)
        with pd.ExcelWriter("./Data/wether.xlsx", engine="openpyxl") as writer:
            yr_data.to_excel(writer, sheet_name="YR", index=False)
    return True


def readYR():
    try:
        readYR = pd.read_excel("./Data/wether.xlsx", sheet_name="YR")
        leverantör = readYR["Leverantör"].values[0]
        tid = readYR["Skapad"].values[0]
        print(f"Prognos för {leverantör} skapad {tid}")
        for index, row in readYR.iterrows():
            if row["Nederbörd"] == True:
                print(f"KL: {row["Timme"]:02d}:00, {row["Temp"]:.0f} grader och nederbörd")
            else:
                print(f"KL: {row["Timme"]:02d}:00, {row["Temp"]:.0f} grader och ingen nederbörd")     
    except (FileNotFoundError, ValueError):
          print("Kunde inte hämta prognos från YR.")
