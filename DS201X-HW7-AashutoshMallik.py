
# coding: utf-8

# In[29]:


from sklearn.datasets import load_iris

import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

import seaborn as sns
import pandas as pd

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split




iris = pd.read_csv('Iris.csv')


iris.head()


# In[36]:

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=5)


# In[37]:

knn = KNeighborsClassifier(n_neighbors=1)


# In[39]:

knn.fit(X_train,y_train)


# In[42]:

y_prediction=knn.predict(X_test)


# In[44]:

knn1_score=metrics.accuracy_score(y_prediction,y_test)


# In[45]:

knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train,y_train)
y_prediction=knn.predict(X_test)
accuracy_knn7=metrics.accuracy_score(y_prediction,y_test)


# In[68]:

scores = []
i_range = list(range(1,25))
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=5)
for i in range(1,25):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    y_prediction=knn.predict(X_test)
    scores.append(metrics.accuracy_score(y_prediction,y_test))

plt.plot(i_range,scores)


# In[80]:

best_k = scores.index(max(scores))
# best k is the variable that stores the best k to use for knn on this dataset
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=5)
knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train,y_train)
y_prediction=knn.predict(X_test)
accuracy_knn=metrics.accuracy_score(y_prediction,y_test)
accuracy_knn


# In[81]:

logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
accuracy_logReg=metrics.accuracy_score(y_test, y_pred)
accuracy_logReg


# In[82]:

from sklearn.tree import DecisionTreeClassifier
decTree = DecisionTreeClassifier()


# In[83]:

decTree.fit(X_train, y_train)
y_pred = decTree.predict(X_test)
accuracy_decTree=metrics.accuracy_score(y_test, y_pred)
accuracy_decTree


# In[95]:

data = [accuracy_knn,accuracy_logReg,accuracy_decTree]
columns = ['KNN','Logistic Regression','Decision Tree']
plt.bar(columns,data,width=0.3,alpha=0.5, color='Orange')


# In[ ]:



