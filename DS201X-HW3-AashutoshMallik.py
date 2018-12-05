
# coding: utf-8

# In[1]:

import pandas as pd
import seaborn as sns


# In[2]:

df = pd.read_csv("USvideos.csv")


# In[3]:

df.head()


# In[4]:

df.info()


# In[5]:

df.describe()


# In[6]:

df.drop_duplicates()
df.describe()


# In[7]:

corr = df.corr()
corr.style.background_gradient()


# In[8]:

df.plot.scatter(x="views", y="likes", c="category_id")


# In[9]:

df_top100views = df.nlargest(100, "views")
df_top100views


# In[10]:

df.nlargest(10,['likes', 'views'])


# In[11]:

data = df[["views", "likes", "category_id"]]
data


# In[12]:

sns.pairplot(data, hue = "category_id")


# In[13]:

data2 = df_top100views[["views", "likes", "category_id"]]
data2


# In[14]:

sns.pairplot(data2, hue = "category_id")


# In[15]:

#The second set of graphs are alot easier to read. 
#The numbers are easier to see in the second graph
#The trends are similar between the graphs. 
#The second set of graphs has less data points so they're less cluttered and easier to read


# In[ ]:



