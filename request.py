#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'radius_mean':2, 'texture_mean':1, 'smoothness_se':4,'concavity_se':5,'perimeter_worst':1,'smoothness_worst':3})

print(r.json())

