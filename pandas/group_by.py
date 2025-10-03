import pandas as pd

df = pd.read_csv('pandas/weather_by_cities.csv')
print(df)

for city,data in (df.groupby('city')):
    print(city)
    print("max temperature: ", data.temperature.max())

g = df.groupby('city')
print(g.temperature.max())

print(g.describe())

def grouper(df,idx,col):
    if 80 <= df[col].loc[idx] <= 90:
        return '80-90'
    elif 50 <= df[col].loc[idx] < 60:
        return '50-60'
    else:
        return 'others'

print("\n")
grouper_object = df.groupby(lambda x: grouper(df,x,'temperature'))
for key,d in grouper_object:
    print(key)
    print(d)
    print("\n")