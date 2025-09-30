import pandas as pd

def before_or_after(year):
    if year > 2000:
        return "After 2000"
    return "Before 2000"

df = pd.read_csv("pandas/movies_data.csv")
print(df.head(5))

df["year_classify"] = df["release_year"].apply(before_or_after)
print(df)

df_new = df[['movie_id', 'title', 'budget', 'revenue','year_classify']]

df_new.to_csv("pandas/movies_data_with_classification.csv", index=False)