#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd


# In[28]:


df=pd.DataFrame(
{"a": [4,5,6, 4],
"b" : [7,8,9, 9],
"c" : [10,11,12, 10]},
index = [1,2,3,4])
df


# Series

# In[22]:


df[["a"]]


# Subset

# In[25]:


df[df["a"] > 4]


# In[26]:


df[["a","b"]]


# In[29]:


df["a"].value_counts()


# In[30]:


len(df)


# In[32]:


df.sort_values("a", ascending=False)


# In[38]:


df = df.drop(["c"], axis=1)
df


# In[44]:


df.groupby(["a"])["b"].agg(["mean", "sum", "count"])


# In[47]:


pd.pivot_table(df, index="a", values="b", aggfunc="sum")


# In[51]:


df.plot()

