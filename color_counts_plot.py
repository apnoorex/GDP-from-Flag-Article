import pandas as pd
import matplotlib.pyplot as plt


countries = pd.read_csv('in_data/world_flags_2024.csv')

color_sums = pd.DataFrame(countries[['White', 'Red', 'Blue', 'Black', 'Yellow', 'Green', 'Orange', 'OtherColor']].sum()).reset_index()
color_sums.columns = ['Color', 'Count']
print(color_sums)

fig = plt.figure(figsize=(10, 4))
ax = fig.add_subplot(1, 1, 1)

barlist = plt.bar(color_sums['Color'], color_sums['Count'], color='#3a8a8d')
ax = plt.gca()
barlist[0].set_color('grey')
barlist[1].set_color('red')
barlist[2].set_color('blue')
barlist[3].set_color('black')
barlist[4].set_color('yellow')
barlist[5].set_color('green')
barlist[6].set_color('orange')
barlist[7].set_color('#3a8a8d')
plt.ylabel('Number of countries')
plt.savefig('out_data/ColorCounts.png')
plt.show()
