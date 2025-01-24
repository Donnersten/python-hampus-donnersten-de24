import requests as rq
from  datetime import datetime, timedelta
import pandas as pd



def smhiWether():
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
         "Leverantör": "SMHI"
    }
     response = rq.get(f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{lon}/lat/{lat}/data.json")
     if response.status_code == 200 or response.status_code == 201:
        response = response.json()
        response = response["timeSeries"]
     else:
        print(f"Något gick fel med SMHI's API! Statuskod: {response.status_code}")
        return False
     
     date_next_day = datetime.now() + timedelta(days=1, hours =- 2)
     date_next_day = date_next_day.replace(minute=0, second=0)
     date_next_day = date_next_day.strftime("%Y-%m-%dT%H:%M:%S")
    


     for validtime in response:
         temp_date = validtime["validTime"]
         temp_date, temp_time = temp_date.split("T")
         temp_time = temp_time.split(":")
         wether["Datum"].append(temp_date)
         wether["Timme"].append(int(temp_time[0] ))
         for parameter in validtime["parameters"]:
            if parameter["name"] == "t":
                 wether["Temp"].append((parameter["values"][0]))
            if parameter["name"] == "pcat":
                    if parameter["values"][0] > 0:
                          wether["Nederbörd"].append(True)
                    else:
                         wether["Nederbörd"].append(False)
         if date_next_day in validtime["validTime"]:
                 break
     smhi_data = pd.DataFrame(wether)
     try:
          with pd.ExcelWriter("./Data/wether.xlsx",mode="a" ,if_sheet_exists="replace", engine="openpyxl") as writer:
               smhi_data.to_excel(writer, sheet_name="SMHI", index=False)
     except FileNotFoundError:
          with pd.ExcelWriter("./Data/wether.xlsx", engine="openpyxl") as writer:
               smhi_data.to_excel(writer, sheet_name="SMHI", index=False)
     return True

def readsmhi():
     try:
          readsmhi = pd.read_excel("./Data/wether.xlsx", sheet_name="SMHI")
          leverantör = readsmhi["Leverantör"].values[0]
          tid = readsmhi["Skapad"].values[0]
          print(f"Prognos för {leverantör} skapad {tid}")
          for index, row in readsmhi.iterrows():
               if row["Nederbörd"] == True:
                    print(f"KL: {row["Timme"]:02d}:00, {row["Temp"]:.0f} grader och nederbörd")
               else:
                    print(f"KL: {row["Timme"]:02d}:00, {row["Temp"]:.0f} grader och ingen nederbörd")      
     except (FileNotFoundError, ValueError):
          print("Kunde inte hämta prognos från SMHI.")


