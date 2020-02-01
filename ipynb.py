#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from matplotlib import pyplot as plt
data=pd.read_csv(r'C:\Users\JNTUAECE\Downloads\65 Years of Weather Data Bangladesh (1948 - 2013).csv')
data.head()


# In[9]:


data.plot(x='Station Names',y='YEAR')
plot.show()


# In[15]:


import matplotlib.pyplot as pyplot
pyplot.plot([2010,2011,2012,2013,2014,2015],[29,28.9,29,28.8,28.7,33.6])
pyplot.title('Temperature')
pyplot.show()


# In[16]:


import matplotlib.pyplot as pyplot
 
a = [13.6,10.8,10.9,13,10.6,16]
b = [29,28.9,29,28.8,28.7,33.6] 
pyplot.scatter(a,b,label='Rainfall VS Cloud Coverage',color='g')
pyplot.xlabel('Rainfall')
pyplot.ylabel('Cloud Coverage')
pyplot.title('Scatter Plot Example')
pyplot.legend()
pyplot.show()


# In[38]:


from matplotlib import pyplot as plt
from matplotlib import style
import random
x = random.sample(range(1,2018), 1000)
num_bins = 100
n, bins, patches = plt.hist(x, num_bins, facecolor='green', alpha=0.5)
 
plt.title('Histogram')
plt.xlabel('Station Names')
plt.ylabel('Max Temp')
plt.show()


# In[45]:


import matplotlib.pyplot as plt
 
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'avg', 'Rainfall', 'Relative Humidity', 'Wind Speed'
sizes = [19.9,0,75,5.1]
explode = (0.01, 0.01, 0.01, 0.1) # explode 'Milk' a little away
 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
 
plt.title('Average Monthly Consumption')
 
plt.show()


# In[ ]:




