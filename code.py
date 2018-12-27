# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3


df = pd.read_csv('Data_BI.csv')
print df.head(5)

g = sns.factorplot(x='year', data=df, kind='count', size=6)
g.set_axis_labels('Year', 'Number of Crimes')

g = sns.factorplot(x='year', hue="SHIFT", data=df, kind='count', size=6)
g.set_axis_labels('Year', 'Number of Crimes')

g = sns.factorplot(x='OFFENSE', data=df, kind='count', size=6)
g.set_axis_labels('Offense', 'Number of Crimes')
g.set_xticklabels(rotation=90)


var = df.groupby(['year','SHIFT']).OFFENSE.count()
var.unstack().plot(kind='bar',stacked=True,  color=['red','blue', 'yellow'], grid=False)
plt.title("No. of offences as per shift")
plt.show()

va=df.groupby(['OFFENSE']).sum().stack()
temp=va.unstack()
x_list = temp['year']
label_list = temp.index
plt.axis("equal") 
plt.pie(x_list,labels=label_list,autopct="%1.1f%%")
plt.title("Offenses over 6 years")
plt.show()

plt.hist(df.year, bins=6, facecolor='green', alpha=0.75)
plt.plot(6, df.OFFENSE.count())
plt.axis([2011, 2016, 0, 500])
plt.xlabel("Years")
plt.ylabel("Offense counts")
plt.show()