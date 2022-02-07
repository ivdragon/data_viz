import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as plticker
import numpy as np
import seaborn as sns

#read data
data = pd.read_csv('/Users/iv_dragon/Documents/GitHub/data_viz/data/covid_deaths_cumulative.csv',sep = ';')
data2 = pd.read_csv('/Users/iv_dragon/Documents/GitHub/data_viz/data/covid_mesacne_statistiky.csv',sep = ';')

#set datumy and values used
datumy = pd.to_datetime(data.Date, dayfirst = True)
values1 = data.DeathCovid
values2 = data.DeathWithCovid
values3 = data.Total
values4 = pd.to_datetime(data2.datum, dayfirst = True)
values5 = data2.kumulativne

#sns.set_theme(style="whitegrid")
sns.set_theme()

#plot
fig, ax = plt.subplots(figsize=(9,6))

#edit x axis
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b, %Y"))

#edit y axis
#ax.yaxis.set_ticks(np.arange(min(values3), max(values3), round((max(values3)-min(values3))/10)))
def tickfr(x):
     return x if x % 100 == 0 else x + 100 - x % 100
ax.yaxis.set_major_locator(plticker.MultipleLocator(base=tickfr(max(values3)/10)))

#plot
ax.plot(datumy, values1, linewidth = 2, label = 'na covid (nczi)')
ax.plot(datumy, values2, linewidth = 2, label = 's covidom (nczi)')
ax.plot(datumy, values3, linewidth = 2, label = 'spolu (nczi)', linestyle = 'dashed')
ax.plot(values4, values5, linewidth = 0, marker='o',label = 'covid (štatistickú úrad)')

#show plot
fig.autofmt_xdate()
plt.legend()
plt.show()


