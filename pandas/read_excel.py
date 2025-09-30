import pandas as pd

def standardize_currency(curr):
    if curr == '$$' or curr == 'Dollars':
        return 'USD'
    return curr

df_movies = pd.read_excel("pandas/movies_db.xlsx", "movies")
print(df_movies)
df_financials = pd.read_excel("pandas/movies_db.xlsx", "financials" , converters = {
    'currency':standardize_currency
})
print(df_financials)

df_everything = pd.merge(df_movies, df_financials, on="movie_id")
print(df_everything)

df_everything.to_excel("pandas/movies_full.xlsx", sheet_name = "all_data", index=False)
