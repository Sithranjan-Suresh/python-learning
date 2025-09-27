import pandas as pd

df = pd.read_csv("pandas\movies.csv")
'''print(df.head(3))
print(df.shape)
print(df.columns)
print(df.release_year.unique())
print(df['language'].unique())
print(df.industry.value_counts())
print(df.language.value_counts())
print(df[["title", "imdb_rating"]])

print(df[(df.release_year > 2000) & (df.release_year <= 2010)])'''

print(df[df.studio == "Marvel Studios"])
print(df.describe())
print(df[df.imdb_rating == df.imdb_rating.max()])
print(df[df.release_year == df.release_year.max()])

df['age'] = df.release_year.apply(lambda x: 2025 - x)
print(df)
df['profit'] = df.apply(lambda x: x.revenue - x.budget, axis=1)
print(df[['budget','revenue','profit']])
df.set_index('title', inplace=True)
print(df)
print(df.loc['The Shawshank Redemption'])