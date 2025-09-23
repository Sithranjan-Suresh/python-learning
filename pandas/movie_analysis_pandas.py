import pandas as pd
df = pd.read_csv("pandas\movies.csv")
print(df.head(4))
print(df.tail(4))
print(df.sample(3))
print(df[2:6])
print(df.shape)

print(df["imdb_rating"].max())
print(df["imdb_rating"].min())
print(df["imdb_rating"].mean())

print(df[df.industry == "Bollywood"]["imdb_rating"].max())
print(df[df.industry == "Bollywood"]["imdb_rating"].min())
print(df[df.industry == "Bollywood"]["imdb_rating"].mean())

print(df[df.industry == "Hollywood"]["imdb_rating"].max())
print(df[df.industry == "Hollywood"]["imdb_rating"].min())
print(df[df.industry == "Hollywood"]["imdb_rating"].mean())