import pandas as pd

df = pd.read_csv('pandas/weather_data.csv', parse_dates = ['day'])
df.set_index('day',inplace=True)

df.fillna({
    'temperature': df.temperature.median(),
    'windspeed':df.windspeed.median(),
    'event': 'No event'
},inplace=True)
print(df)

df_one = pd.read_csv('pandas/weather_data.csv', parse_dates = ['day'])
df_one.ffill(inplace=True)

print(df_one)

df_two = pd.read_csv('pandas/weather_data.csv', parse_dates = ['day'])

df_two.dropna(inplace=True)
print(df_two)