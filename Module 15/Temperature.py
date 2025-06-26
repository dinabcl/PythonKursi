import pandas as pd
import matplotlib.pyplot as plt

#getting data from file
df=pd.read_csv("weather_tokyo_data.csv")
print(df)

filtered_DF=df[df["temperature"]]

filtered_DF=filtered_DF.sort_values(by="temperature", ascending=False)
print(filtered_DF)
plt.figure(figsize=(14,8))
bars=plt.bar(filtered_DF["year"],filtered_DF["temperature"], color="skyblue")

plt.title("Average IQ by Country (IQ>=100) " ,fontsize=16)
plt.xlabel("Country" , fontsize=14)
plt.ylabel("Average IQ" , fontsize=14)

plt.bar_label(bars, fmt="%.2f" ,fontsize=10, color="black")

plt.tight_layout()

plt.show()










