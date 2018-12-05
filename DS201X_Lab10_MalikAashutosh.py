
# coding: utf-8

# In[4]:

import pandas as pd
from bokeh.io import output_notebook, show, output_file
from bokeh.plotting import figure
import matplotlib.pyplot as plt


# In[5]:

df = pd.read_csv("Lemonade_Lab10.csv")


# In[6]:

df.head(5)


# In[7]:

p = figure(title="Lemons and Orange Sales by Temperature")


# In[8]:

p.circle(x=df["Temperature"], y=df["Lemon"], size=10, alpha=0.5, color="green", legend="Lemon")
p.triangle(x=df["Temperature"], y=df["Orange"], size=10, alpha=0.5, color="orange", legend="Orange")
p.legend.location="top_left"
show(p)


# In[9]:

grouped =  df.groupby("Temperature")
lem = grouped["Lemon"]
avg = lem.mean()
std = lem.std()
Tem = list(grouped.groups.keys())
Park = df[df["Location"]=="Park"]
Beach = df[df["Location"] == "Beach"]


# In[10]:

v = figure(title = "Temperature vs Lemon Sales (Park and Beach)")


# In[11]:

v.vbar(x=Tem, bottom=avg-std, top=avg+std, width =0.8, fill_alpha=0.2, line_color=None, legend="Lemon Revenue 1 stddev")
v.circle(x=Beach["Temperature"], y=Beach["Lemon"], alpha=0.5, size=10, color ="red", legend="Sales in Beach")
v.triangle(x=Park["Temperature"], y=Park["Lemon"], alpha=0.5, size=10, color="blue", legend="Sales in Park")
v.legend.location="top_left"
show(v)


# In[ ]:




# In[ ]:



