import pandas as pd
from matplotlib import pyplot as plt

df_sales = pd.read_excel("data_visualization/linechart.xlsx")
print(df_sales.head())

df_sales.plot(kind="bar", x="Quarter")
plt.title("Product Sales by Quarter")
plt.xticks(rotation=45)


df_sales_2 = df_sales.set_index("Quarter")
df_sales_2.plot(kind="bar")
plt.title("Product Sales by Quarter_v2")
plt.xticks(rotation=45)
plt.show()