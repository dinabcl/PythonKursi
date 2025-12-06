from calendar import month
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("weather_tokyo_data.csv")
print(df)

temperature_data=df["temperature"]
print(temperature_data)

temperature_data=df["temperature"].mean()
print("get the average",temperature_data)

average_temp_by_month = df.groupby("day")
print(average_temp_by_month)

temp = df.groupby("year")["temperature"].mean(numeric_only=True)
plt.figure(figsize=(14,8))

temp.plot(kind="line",marker="o",color="skyblue")

plt.title("Average temperature")
plt.xlabel("Idk")
plt.ylabel("idk2")
plt.show()

def get_seasons(month):
    if month in [12,1,2]:
        return print("winter")
    elif month in [3,4,5]:
        return print("spring")
    elif month in [6,7,8]:
        return print("summer")
    else :
        return print("Autumns")

