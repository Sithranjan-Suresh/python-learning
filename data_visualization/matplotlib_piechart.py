import pandas as pd
from matplotlib import pyplot as plt

df_sales = pd.read_excel("data_visualization/linechart.xlsx")
print(df_sales.head())

total_sales = df_sales[["Fridge", "Dishwasher", "Washing Machine"]].sum()
print(total_sales)

plt.pie(total_sales, labels = total_sales.index, autopct="%1.1f%%", explode=(0.1, 0, 0), shadow=True)
plt.show()