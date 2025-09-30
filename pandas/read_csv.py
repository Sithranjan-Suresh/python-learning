import pandas as pd

df = pd.read_csv("pandas/stock_data.csv", header=1, names = ["stock_symbols", "eps", "revenue", "price", "people"], na_values=["Not Available", "n.a.", -1, 'not available'])
print(df)
df["pe"] = df["price"]/df["eps"]
print(df)
df.to_csv("pandas/pe.csv", index=False)