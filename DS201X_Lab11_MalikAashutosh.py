
# coding: utf-8

# In[1]:

import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:

from sklearn.datasets import load_iris


# In[3]:

iris = load_iris()
iris


# In[4]:

#iris = sns.load_dataset("iris")
#print(iris)


# In[5]:

dataset = sns.load_dataset("iris")
sns.pairplot(dataset, hue="species", markers = ['o','s','D'])


# In[6]:

from sklearn.neighbors import KNeighborsClassifier


# In[7]:

knn = KNeighborsClassifier(n_neighbors = 1)
knn


# In[14]:

X = iris.data
print (X)
Y = iris.target
print (Y)
knn.fit(X, Y)


# In[9]:

knn.predict([[3,4,4,2]])


# In[10]:

X_new = ([3,4,4, 2], [4, 4, 3, 2])


# In[11]:

knn.predict(X_new)


# In[12]:

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X, Y)


# In[13]:

logreg.predict(X_new)


# In[ ]:



