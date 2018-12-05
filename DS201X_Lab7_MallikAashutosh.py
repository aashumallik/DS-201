
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


# In[ ]:

values=[0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values,bins=6)
plt.show()


# In[ ]:

frame = pd.read_csv('Automobile-price-data_Cleaned.csv')


# In[ ]:

frame.head(5)


# In[ ]:

frame.describe()


# In[ ]:

frame['city-mpg'].plot.hist(bins=15,title='DS201X Lab 7 ASHU Automotive city-mpg Histograms')
plt.show


# In[ ]:




# In[ ]:

frame.boxplot(by='make', column ='city-mpg', figsize=(12,8), rot=45)


# In[ ]:

frame.plot.scatter(x='engine-size', y='city-mpg')


# In[ ]:

frame.plot.scatter(y='engine-size', x='city-mpg', s=frame['price']/1000, c='curb-weight')


# In[ ]:




# In[ ]:



