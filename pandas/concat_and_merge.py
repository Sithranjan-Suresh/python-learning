import pandas as pd

india_weather = pd.DataFrame({
    'city': ['Delhi', 'Mumbai', 'Bangalore'],
    'temperature': [32, 45, 30],
    'humidity': [85, 60, 78]
})

us_weather = pd.DataFrame({
    'city': ['New York', 'Chicago', 'Orlando'],
    'temperature': [21, 14, 35],
    'humidity': [68, 65, 75]
})

df = pd.concat([india_weather, us_weather], keys = ["india", "us"])
print(df)
print(df.loc["us"])

temperature_df = pd.DataFrame({
    'city': ['Delhi', 'Mumbai', 'Bangalore'],
    'temperature': [32, 45, 30]
    })
print(temperature_df)

windspeed_df = pd.DataFrame({
    'city': ['Mumbai', 'Delhi'],
    'windspeed': [7, 4]
    }, index = [1,0])

print(windspeed_df)

combined = pd.concat([temperature_df, windspeed_df], axis = 1)
print(combined)

df1 = pd.DataFrame({
    'city': ['Delhi', 'Mumbai', 'Bangalore'],
    'temperature': [32, 45, 30]
    })

df2 = pd.DataFrame({
    'city': ['Mumbai', 'Delhi'],
    'windspeed': [7, 4]
    })

print(pd.merge(df1, df2, on = 'city'))