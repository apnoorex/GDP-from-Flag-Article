import pandas as pd


countries = pd.read_csv('in_data/world_flags_2024.csv')

countries = countries[countries['Population'] > 100000]
countries = countries[countries['GDPPerCapita'] > 1000]

print('Dataset min:', countries['GDPPerCapita'].min())
print('Dataset max:', countries['GDPPerCapita'].max())
print('Dataset mean:', countries['GDPPerCapita'].mean())

countries = countries[countries['Crescent'] == 1]

print('Crescent min:', countries['GDPPerCapita'].min())
print('Crescent max:', countries['GDPPerCapita'].max())
print('Crescent mean:', countries['GDPPerCapita'].mean())
