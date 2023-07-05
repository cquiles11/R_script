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
plt.plot(dataset[['x']], model.predict(dataset[['x']]), color = 'blue')
plt.title('y vs x')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
# In[7]:
plt.savefig("python_combined.png")