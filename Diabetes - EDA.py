#!/usr/bin/env python
# coding: utf-8

# ## Importing Libraries

# In[3]:


import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

import warnings 
warnings.filterwarnings("ignore")


# ## Importing Data

# In[29]:


data = pd.read_csv("diabetes.csv")


# In[6]:


data.head()


# ## Data Understanding

# In[7]:


data.isna().sum()


# In[8]:


data.info()


# In[9]:


data.shape


# ## Data Processing

# In[10]:


data[["Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction"]] = data[["Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction"]].replace(0,np.nan)


# In[11]:


data.isna().sum()


# In[14]:


data.hist(figsize = (10,10))
plt.show()


# In[15]:


data["Glucose"] = data["Glucose"].fillna(data["Glucose"].mean())
data["BloodPressure"] = data["BloodPressure"].fillna(data["BloodPressure"].mean())
data["SkinThickness"] = data["SkinThickness"].fillna(data["SkinThickness"].median())
data["Insulin"] = data["Insulin"].fillna(data["Insulin"].median())
data["BMI"] = data["BMI"].fillna(data["BMI"].mean())


# ### EDA

# In[22]:


sns.pairplot(data = data, hue = "Outcome")
plt.show()


# In[26]:


corr = data.corr()


# In[28]:


sns.heatmap(data = corr , annot = True , cmap ='RdYlGn')


# In[ ]:




