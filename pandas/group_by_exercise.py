import pandas as pd

df = pd.read_csv('pandas/movies_data_groupby.csv')
print(df)

g = df.groupby('industry')
print(g.size())
print(g.describe())
print(g.get_group('Bollywood'))

def the_group(df,idx,col):
    if 1 <= df[col].loc[idx] <= 3.9:
        return "Poor"
    elif 4 <= df[col].loc[idx] <= 7.9:
        return "average"
    elif 8 <= df[col].loc[idx] <= 10:
        return "good"
    else:
        return "others"

grouper_object = df.groupby(lambda x: the_group(df,x,'imdb_rating'))

for rating,data in grouper_object:
    print(rating)
    print(data)
    print("\n") 