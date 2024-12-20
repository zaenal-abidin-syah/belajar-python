import pandas as pd


df = pd.read_csv('data.csv')

df = pd.get_dummies(df, columns=['Pekerjaan'])

kolom_numerik = df['Umur']
mean = kolom_numerik.mean()
median = kolom_numerik.median()
mode = kolom_numerik.mode()[0]

print(f"Mean: {mean}, Median: {median}, Modus: {mode}")

range_value = kolom_numerik.max() - kolom_numerik.min()
variance = kolom_numerik.var()
std_dev = kolom_numerik.std()
print(f"Range: {range_value}, Variance: {variance}, Standar Deviasi: {std_dev}")