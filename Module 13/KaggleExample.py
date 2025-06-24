import pandas as pd
df=pd.read_csv("avgIQpercountry.csv")
print(df.info()) #we see the colums of this dataset
print(df.head()) #we see the first 5 rows

country_data=df["Country"]
print(country_data)

subset=df[["Country","Average IQ"]]
filtered_DF=subset[subset["Average IQ"]>100]
print(filtered_DF)

#null_mask finding null rows
null_mask=df.isnull()
null_count=null_mask.sum()
print(null_count)

#removing duplicates
df.drop_duplicates(keep="first",inplace=True)
df["Population - 2023"]=df["Population - 2023"].apply(lambda x: float(x.replace(",", "")))

#finding the avg of a continent
avg_iq_per_country=df.groupby('Continent')["Average IQ"].mean()

avg_iq_per_country=avg_iq_per_country.sort_values(ascending=False)
print(avg_iq_per_country)

#calculate nobel prizes by country. and show countries only with more than 1 nobel
# you have to use Group By, Sum and sort values
nobel_prizes_per_country=df.groupby('Country')["Nobel Prices"].sum()
sorted_nobel_prizes_per_country=nobel_prizes_per_country.sort_values(ascending=False)
sorted_nobel_prizes_per_country=sorted_nobel_prizes_per_country[sorted_nobel_prizes_per_country!=0]
print(sorted_nobel_prizes_per_country)