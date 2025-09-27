import pandas as pd

df = pd.read_csv("pandas/bengaluru_house_prices.csv")
print(f"The number of rows and columns: {df.shape}")
print(df.head(5))
print(df.area_type.unique())
print(df['size'].unique())

print(df[(df['area_type'] == "Super built-up  Area") & (df["size"] == "2 BHK")])
print(df[(df['area_type'] == "Super built-up  Area") & (df["size"] == "2 BHK")].shape[0])