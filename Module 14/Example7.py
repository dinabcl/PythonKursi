import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt


my_dataset=pd.read_csv("avgIQpercountry.csv")

my_dataset["Population - 2023"] = my_dataset["Population - 2023"].str.replace(",","").astype(float)

fig=px.scatter_geo(my_dataset,locations="Country",locationmode="country names", hover_name="Country",
                   size="Average IQ", color="Continent", projection="natural earth",
                   title="Average IQ by Country", size_max=20, template="plotly_dark")

fig.show()