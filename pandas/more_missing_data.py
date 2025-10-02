import pandas as pd
import numpy as np

df = pd.read_csv("pandas/more_weather_data.csv")
print(df)
'''
df.replace({
    "temperature": -99999,
    "windspeed": [-99999,-88888],
    "event": "no event"}, np.nan, inplace=True)
    '''

df.replace({
    -99999: np.nan,
    -88888: np.nan,
    "no event": "Sunny"
}, inplace=True)
print(df)

df_one = pd.DataFrame({
    "student": ["Ravi", "Ajay", "Kumar", "Anil"],
    "score": ["excellent", "good", "average", "poor"]
})
print(df_one)

df_one.replace(["excellent", "good", "average", "poor"],[4, 3, 2, 1], inplace=True)
print(df_one)