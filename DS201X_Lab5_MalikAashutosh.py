
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt


# In[2]:

df = pd.read_csv('lab5.csv') 


# In[3]:

df.head()
df.shape


# In[4]:

df2 = df.groupby(['State_name']).size()


# In[5]:

type(df2)


# In[6]:

df2.plot.bar();
plt.show()


# In[7]:

df2.plot.bar(figsize=(15,7));
plt.show()


# In[ ]:



