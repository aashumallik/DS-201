
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt


# In[2]:

df = pd.read_csv('http://bit.ly/drinksbycountry') 


# In[3]:

df.head()
df.shape


# In[4]:

df2 = df.groupby(['continent']).size()


# In[5]:

type(df2)


# In[6]:

df2.plot.bar();
plt.show()


# In[13]:

df['beer_servings']


# In[14]:

df[['beer_servings','continent']]


# In[15]:

df2.plot.bar();
plt.show()


# In[17]:

df.plot.box()
plt.show()


# In[ ]:



