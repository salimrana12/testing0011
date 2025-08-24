#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.DataFrame()


# In[4]:


df


# In[5]:


df.shape


# In[6]:


df.info()


# In[19]:


city = ['texus', 'clafornia', 'vatican city']


# In[ ]:





# In[12]:


city2 = ['valican sity', 'hollywood', 'seaborn']


# In[14]:


type(city2)


# In[15]:


df1 = pd.DataFrame(city, columns=['city_in_USA'], index=['city1', 'city2', 'city3'])
df1


# In[20]:


df2 = pd.DataFrame(zip(city, city2), columns=['city_in_USA', 'texus'], index=['city1', 'city2', 'city3'])


# In[21]:


df2


# In[22]:


df2.info()


# In[23]:


df2.shape


# In[24]:


df0 = pd.read_csv('time text2.csv')
df0


# In[25]:


df0.head()


# In[26]:


df0.shape


# In[28]:


df0.tail(10)


# In[29]:


df0.head(10)


# In[33]:


df0.columns


# In[35]:


df0.index


# In[44]:


df0['Id No']


# In[ ]:




