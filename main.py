import pandas as pd
import csv as csv

df = pd.read_csv('fin.csv')

del df['LUMINOSITY']

df.dropna()

df.to_csv('finally.csv')
