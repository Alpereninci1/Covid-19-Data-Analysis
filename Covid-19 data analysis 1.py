# -*- coding: utf-8 -*-
"""calisma_ortami.ipynb adlı not defterinin kopyası

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DBhF2DkqAGZ2Z7WwIYjAtM_wDnd7Eyyg
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import pandas_profiling
import numpy
from numpy import percentile
from numpy.random import rand
import matplotlib.pyplot as plt
# %matplotlib inline
#https://www.google.com/covid19/mobility/
url='https://drive.google.com/file/d/18gyHbx6rfogq3yQ-GR9COjcGgyYlCnBZ/view?usp=sharing'
url2='https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url2)
df.info()

#soru 1
df.describe().transpose()

#soru2
x1 = df.plot(kind='scatter', x='retail_and_recreation_percent_change_from_baseline', y='transit_stations_percent_change_from_baseline', color='r')
x2 = df.plot(kind='scatter', x='parks_percent_change_from_baseline', y='grocery_and_pharmacy_percent_change_from_baseline', color='g')
x3 = df.plot(kind='scatter', x='workplaces_percent_change_from_baseline', y='residential_percent_change_from_baseline', color='b')

#soru 3
boxplot= df.boxplot( figsize=(20,15),rot=90, fontsize=10,column=['retail_and_recreation_percent_change_from_baseline', 'grocery_and_pharmacy_percent_change_from_baseline', 'parks_percent_change_from_baseline','transit_stations_percent_change_from_baseline','workplaces_percent_change_from_baseline','residential_percent_change_from_baseline'])
#Tüm sutünlarda outlier vardır.

#soru4 

df.date = pd.to_datetime(df.date)
fig, ax = plt.subplots(figsize=(10,10))
g = df.groupby(pd.Grouper(key='date', freq='M')) # aydan aya grupla
g.sum().plot(ax=ax)

#soru5
url='https://drive.google.com/file/d/1Eg8Lffm49bc-bGFkv_4ddrQw8U8WE6P4/view?usp=sharing'
url2='https://drive.google.com/uc?id=' + url.split('/')[-2]
df2 = pd.read_csv(url2)

df2.date = pd.to_datetime(df2.date)
fig, ax = plt.subplots(figsize=(10,10))
g = df2.groupby(pd.Grouper(key='date', freq='M')) # aydan aya grupla
g.sum().plot(ax=ax)