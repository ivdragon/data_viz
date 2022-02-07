import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#read data
data = pd.read_csv('/Users/iv_dragon/Documents/GitHub/data_viz/data/pomer_dych_chorob.csv',sep = ';')
reasons = data.pricina
values1 = data.rok2021
values2 = data.rok2020
values3 = data.roky2019to2017

names1 =  list(reasons)
#v1
##size1 = list(values1)
##plt.pie(size1,labels=names1)

#v2
size2 = list(values2)
plt.pie(size2,labels=names1)

#v3
##size3 = list(values3)
##plt.pie(size3,labels=names1)


my_circle = plt.Circle( (0,0), 0.5, color='white')
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.show()