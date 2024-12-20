from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd

data = ['pencil', 'bolpoint', 'buku', 'bolpoint']

label_encoder  = LabelEncoder()
num_data = label_encoder.fit_transform(data)

print(num_data)


data = ['pencil', 'bolpoint', 'buku', 'bolpoint']

one_hot = pd.get_dummies(data)
print(one_hot)

data = [['pencil'], ['bolpoint'], ['buku'], ['bolpoint']]
ordinal_data = OrdinalEncoder()
num_data = ordinal_data.fit_transform(data)
print(num_data)  # Output: [[0. 0. 1. 1.

data = pd.DataFrame({
  'Alat': ['Pencil', 'Buku', 'Bolpoint', 'Pencil', 'Bolpoint'],
  'Target':[1,0,1,1,0]
})
mean = data.groupby('Alat')['Target'].mean()
data['Alat'] = data['Alat'].map(mean)
print(data)  # Output:   City  Target

