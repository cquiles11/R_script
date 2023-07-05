#!/usr/bin/env python

# In[1]:
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.pyplot
# In[2]:
filename = "regrex1.csv"
# In[3]:
dataset = pd.read_csv(filename)
# In[4]:
model = LinearRegression()
# In[5]:
model.fit(dataset[['x']], dataset[['y']])
# In[6]:
plt.scatter(dataset[['x']], dataset[['y']], color = 'red')
# In[7]:
plt.savefig("pyhton_scatter.png")