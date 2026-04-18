import requests
import pandas as pd

LAT = 51.819112
LON = 20.527418

def fetch(lat, lon, start_date, end_date):
    url = f"https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max&timezone=Europe/Warsaw"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data['daily'])
    df["time"] = pd.to_datetime(df["time"])
    df["temp_avg"] = ((df["temperature_2m_max"] + df["temperature_2m_min"] )/2).round(1)
    df["rainy_day"] = df["precipitation_sum"] >= 0.5
    df["windy_day"] = df["windspeed_10m_max"] > 20
    df["nice_temp"] = df["temp_avg"].between(12, 22)
    df["freeze_day"] = df["temperature_2m_min"] < 0
    df["score"] = (
                    df["nice_temp"].astype(int)+
                   (~df["windy_day"]).astype(int)+
                   (~df["rainy_day"]).astype(int)
                   )
    return df

df = fetch(LAT,LON,"2020-04-17","2026-04-17")
print(df.head())
df.to_csv(r'data/data.csv',index=False)