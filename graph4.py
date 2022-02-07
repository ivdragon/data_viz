import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#read data
data = pd.read_csv('/Users/iv_dragon/Documents/GitHub/data_viz/data/dovody_smrti_percentualne.csv',sep = ';')
reasons = data.dôvod
values1 = data.perc2021
values2 = data.perc19to17
values3 = data.perc19to15
values4 = data.perc19

#width of bars
barWidth = 1

#heights of bars
bars1 = []
bars2 = []
bars3 = []
bars4 = []

for i in range(len(values1)):
     values1[i] = values1[i].replace(',','.')
     bars1.append(float(values1[i])*100)
     values2[i] = values2[i].replace(',','.')
     bars2.append(float(values2[i])*100)
     values3[i] = values3[i].replace(',','.')
     bars3.append(float(values3[i])*100)
     values4[i] = values4[i].replace(',','.')
     bars4.append(float(values4[i])*100)

#bars position
r1 = [5*x for x in range(len(bars1))]
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

#actual plot
plt.bar(r1, bars1, width=barWidth, edgecolor='white', label='perc. hodnota v roku 2021')
plt.bar(r2, bars2, width=barWidth, edgecolor='white', label='priemerná perc. hodnota za roky 2019-2017')
plt.bar(r3, bars3, width=barWidth, edgecolor='white', label='priemerná perc. hodnota za roky 2019-2015')
plt.bar(r4, bars4, width=barWidth, edgecolor='white', label='perc. hodnota v roku 2019')

#plt.xlabel('príčina', fontweight='bold')
plt.xticks([5*r + barWidth for r in range(len(bars1))], list(reasons),rotation = 90, size = 7)

plt.subplots_adjust(left= 0.1, right = 0.9, bottom = 0.3)
plt.legend(prop={'size': 8})
plt.show()


