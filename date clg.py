#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


#creating data range
date_range = pd.date_range(start='2024-01-01', end='4-10-2024',freq='D')
print(date_range)


# In[3]:


# Assigning random data for each date in the range
data = np.random.randint(10, 100, size=(len(date_range)))

# Creating a time series using Pandas Series
time_series = pd.Series(data=data, index=date_range)
print(time_series)


# In[8]:


df = pd.DataFrame(data)


# In[49]:


date_range = pd.date_range(start='2024-01-01', end='2024-01-01', freq='D')
print("Date Range:")
print(date_range)


# In[50]:


df = pd.DataFrame(date_range, columns=['date'])


# In[51]:


#defining start and end date
start_date = pd.Timestamp('2024-01-01')
end_date = pd.Timestamp('2024-01-01')


# In[52]:


df['start'] = start_date
df['end'] = end_date
#(start and end date adding in dataframe)


# In[53]:


df['date_difference'] = df['end'] - df['start']
print("the difference between two dates")
print(df)


# In[54]:


years = date_range.year
print("Years:", years)


# In[55]:


months = date_range.month
print(months)


# In[56]:


days = date_range.day
print(days)


# In[59]:


df['Rolling_mean']=df['Value'].rolling(window=3).mean()


# In[ ]:




