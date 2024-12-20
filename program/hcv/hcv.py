import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./hcv.csv')

descriptive_stats = df.describe()
print("statistik deskriptif")
print(descriptive_stats)

plt.figure(figsize=(8,6))
sns.countplot(x='Category', data=df)
plt.title("distribusi kategori")
plt.show()