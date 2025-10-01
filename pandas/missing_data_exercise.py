import pandas as pd

df = pd.read_csv("pandas/fruits_data.csv")
print(df.shape)
print(df.columns)
print(df)

new_df = df.fillna(-1)
print(new_df)
