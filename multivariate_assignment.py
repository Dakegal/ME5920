import pandas as pd


airfoil_data = pd.read_csv(r"C:\Users\kolan\Documents\2025_Spring\ME5920\airfoil_self_noise.dat", delimiter="\t", header=None)
airfoil_data.columns = ['Frequency(Hz)' , 'Attack angle' , 'Chord length' , 'Free stream vel' , 'thickness', 'scaled sound pressure']

#print(airfoil_data.head())

means = airfoil_data[['Frequency(Hz)' , 'Attack angle' , 'Chord length' , 'Free stream vel' , 'thickness', 'scaled sound pressure']].mean()
variances = airfoil_data[['Frequency(Hz)' , 'Attack angle' , 'Chord length' , 'Free stream vel' , 'thickness', 'scaled sound pressure']].var()
medians = airfoil_data[['Frequency(Hz)' , 'Attack angle' , 'Chord length' , 'Free stream vel' , 'thickness', 'scaled sound pressure']].median()
skewnesses = airfoil_data[['Frequency(Hz)' , 'Attack angle' , 'Chord length' , 'Free stream vel' , 'thickness', 'scaled sound pressure']].skew()
kurtosises = airfoil_data[['Frequency(Hz)' , 'Attack angle' , 'Chord length' , 'Free stream vel' , 'thickness', 'scaled sound pressure']].kurt()
ranges = airfoil_data[['Frequency(Hz)' , 'Attack angle' , 'Chord length' , 'Free stream vel' , 'thickness', 'scaled sound pressure']].apply(lambda x: x.max() - x.min())
print(ranges)