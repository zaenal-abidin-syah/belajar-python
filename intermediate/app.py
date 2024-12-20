import pickle

with open('text.txt', 'wb') as file:
	pickle.dump('halo',file)
	file.close()