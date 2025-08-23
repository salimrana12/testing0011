#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.DataFrame()
df


# In[3]:


df.info()


# In[8]:


city = ['texus', 'clafornia', 'valicon city']


# In[9]:


df = pd.DataFrame(city)


# In[6]:


df


# In[10]:


type(df)


# In[11]:


type(city)


# In[14]:


df


# In[17]:


type(df)


# In[18]:


row, col = df.shape


# In[19]:


row


# In[20]:


col


# In[21]:


row, col


# In[23]:


df = pd.DataFrame(city, columns=['city_in_USA'])
df


# In[24]:


df = pd.DataFrame(city, columns=['City_in_Europe'], index=['c1', 'c2', 'c3'])
df


# In[25]:


row, col


# In[55]:


town = ['vatican_city', 'texus', 'hollywood']


# In[56]:


df2 = pd.DataFrame(town)
df2


# In[49]:


df2 = pd.DataFrame(town, columns=['City_in_Texus'], index=['City1', 'City2', 'City3'])


# In[50]:


df2


# In[51]:


df3 = pd.DataFrame(zip(city, town), columns=['USA', 'UA'])


# In[100]:


df3


# In[59]:


df3.shape


# In[87]:


town3 = [['Bravia', 'England'], ['Neuziland', 'Biyetname'], ['hawzu', 'khauzo']]


# In[98]:


df4 = pd.DataFrame(town3, columns=['state', 'stats'])


# In[99]:


df4


# In[105]:


df5 = pd.DataFrame(town3, columns=['Faver', 'look'])


# In[106]:


df5


# In[112]:


dict1 = {
    'city1': city,
    'city2': town
}


# In[113]:


dict1


# In[115]:


type(dict1)


# In[116]:


car = pd.read_csv('time text2.csv')


# In[117]:


car


# In[118]:


car.shape


# In[121]:


car.head()


# In[123]:


car.tail()


# In[125]:


car.head(10)


# In[127]:


car.shape


# In[129]:


car.values


# In[130]:


car.index


# In[ ]:




