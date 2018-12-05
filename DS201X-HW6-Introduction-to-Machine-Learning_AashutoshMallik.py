
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier


# In[2]:

weight = [140, 130, 150, 170]
skin = ['Smooth', 'Smooth', 'Bumpy', 'Bumpy']

stack = np.column_stack((np.array(weight), np.array(skin)))

print(stack)

fruit = ['Apple', 'Apple', 'Orange', 'Orange']
print(fruit)


# In[3]:

skin=[0,0,1,1]

fruit = [0,0,1,1]

features = np.column_stack((np.array(weight), np.array(skin)))
print(features)


# In[4]:

clf = DecisionTreeClassifier()


# In[5]:

clf = clf.fit(features, fruit)


# In[6]:

def labelPrediction(predicted):
    if predicted == 0:
        predicted = 'Apple'
    elif predicted == 1:
        predicted = 'Orange'
    print('Prediction: ', predicted)


# In[7]:

prediction = clf.predict([[140,1]])
labelPrediction(prediction)


# In[9]:

features = np.column_stack((np.array(skin), np.array(weight)))
clf = clf.fit(features, fruit)
pred = clf.predict([[1,140]])
labelPrediction(pred)


# In[11]:

skin2 = [1 , 0, 1, 0]
weight2 = [140, 130, 150, 170]

fruit2 = [0,0,1,1]
features2 = np.column_stack((np.array(skin2), np.array(weight2)))

print(features2)

clf2 = DecisionTreeClassifier()
clf2 = clf2.fit(features2, fruit2)

prediction2 = clf2.predict([[140,1]])
labelPrediction(prediction2)


# In[12]:

skin3 = [0 , 0, 1, 1]
weight3 = [170, 130, 150, 140]

fruit3 = [0, 0, 1, 1]
features3 = np.column_stack((np.array(skin3), np.array(weight3)))

print(features3)

clf3 = DecisionTreeClassifier()
clf3 = clf3.fit(features2, fruit)

prediction3 = clf3.predict([[140,1]])
labelPrediction(prediction3)


# In[14]:

gender = ['F', 'F', 'M', 'F', 'M', 'M']
gender = [0, 0, 1, 0, 1, 1]
print(gender)

age = [15, 25, 32, 40, 12, 14]

app = ['Pokemon Go', 'WhatsApp', 'Snap Chat', 'WhatsApp', 'Pokemon Go', 'Pokemon Go']

app = [0, 1, 2, 1, 0, 0]

def listApp(pre):
    if pre == 0:
        print ('Pokemon Go')
    elif pre == 1:
        print ('WhatsApp')
    elif pre == 2:
        print ('Snap Chat')

appFeatures = np.column_stack((np.array(gender), np.array(age)))
print(appFeatures)

appClf = DecisionTreeClassifier()
appClf = appClf.fit(appFeatures, app)

appPred = appClf.predict([[1, 21]])
listApp(appPred)


# In[15]:

appPred2 = appClf.predict([[0, 18]])
listApp(appPred2)

