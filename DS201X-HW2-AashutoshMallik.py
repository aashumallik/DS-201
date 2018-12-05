
# coding: utf-8

# In[3]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:

df = pd.read_csv('Lemonade2016-2.csv')


# In[9]:

df.info()


# In[38]:

df.head()


# In[39]:

df.loc[8,'Date']="7/8/2016"


# In[40]:

df['Leaflets'] = df['Leaflets']. fillna(round(df['Leaflets'].mean()))


# In[41]:

df


# In[42]:

df.drop_duplicates()


# In[43]:

df.reset_index()


# In[44]:

df['Sales']=df['Lemon']+df['orange']


# In[45]:

df


# In[46]:

df['Revenue']=df['Sales']*df['Price']
df


# In[47]:

df.plot.scatter(x=['Leaflets'],y=['Sales'])
plt.show()


# In[48]:

df.hist(coloumn=['Revenue'],bins=10)
plt.show()


# In[49]:

df.boxplot(by=['Location'],coloumn=['Sales'])
plt.show()


# In[50]:

import seaborn as sns


# In[51]:

a = sns.boxplot(x='Location',y='Sales',data=df,palette='Set3')


# In[52]:

data = df['Temperature']>=75
df[data]


# In[53]:

a1 = sns.boxplot(x='Location',y='Sales',data=df[data1],palette='Set3')


# In[54]:

data1=df[['Revenue','Temperature','Leaflets','Location']]


# In[55]:

sns.pairplot(data1,hue='Location')
plt.show()


# In[ ]:




# In[ ]:



