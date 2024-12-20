import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

data = pd.read_csv('data.csv')
kategori = data['kategori']

one_hot = LabelEncoder()
labels = one_hot.fit_transform(kategori)
binary_vectors = np.array([format(label, '03b') for label in labels])

# ganti data kategori dengan binary vector
data['kategori'] = binary_vectors
print(data)