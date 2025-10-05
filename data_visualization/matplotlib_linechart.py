import pandas as pd
from matplotlib import pyplot as plt

df_sales = pd.read_excel("data_visualization/linechart.xlsx")
plt.figure(figsize=(12, 4))
plt.plot(df_sales["Quarter"], df_sales["Fridge"], color = "blue", label = "Fridge")
plt.plot(df_sales["Quarter"], df_sales["Dishwasher"], color = "black", label = "Dishwasher")
plt.plot(df_sales["Quarter"], df_sales["Washing Machine"], color = "yellow", label = "Washing Machine")
plt.title("Product Sales")
plt.xlabel("Quarter")
plt.ylabel("Revenue (in millions)")
plt.legend()
plt.show()
