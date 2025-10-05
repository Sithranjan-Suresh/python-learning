import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df_score = pd.read_excel("data_visualization/histograms.xlsx")
print(df_score.head())

sns.histplot(df_score["Exam_Score"], bins=10, kde=True)
plt.show()
