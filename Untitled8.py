#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns


# In[2]:


df = pd.read_csv(r"C:\Users\ydaks\Downloads\WA_Fn-UseC_-Telco-Customer-Churn.csv")


# In[4]:


df.head()


# In[5]:


df.Partner = df.Partner.map(dict(Yes=1, No=0))


# In[7]:


df.Dependents = df.Dependents.map(dict(Yes=1, No=0))


# In[8]:


df.PhoneService = df.PhoneService.map(dict(Yes=1, No=0))


# In[9]:


df.PaperlessBilling = df.PaperlessBilling.map(dict(Yes=1, No=0))


# In[10]:


df.Churn = df.Churn.map(dict(Yes=1, No=0))


# In[11]:


df.head()


# In[12]:


df.tail()


# In[13]:


df


# In[ ]:




