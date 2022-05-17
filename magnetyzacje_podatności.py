#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import random
get_ipython().run_line_magic('matplotlib', 'inline')
from numpy.random import rand
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import imageio
import numba
import time
import warnings
warnings.filterwarnings('ignore')


# In[6]:


mag1_txt = open('magnetyzacjaL10.txt','r')
mag1 = []
for i in mag1_txt.read().split():
    mag1.append(float(i))
mag1_txt.close()

mag2_txt = open('magnetyzacjaL50.txt','r')
mag2 = []
for i in mag2_txt.read().split():
    mag2.append(float(i))
mag2_txt.close()

mag3_txt = open('magnetyzacjaL100.txt','r')
mag3 = []
for i in mag3_txt.read().split():
    mag3.append(float(i))
mag3_txt.close()

pod1_txt = open('podatnośćL10.txt','r')
pod1 = []
for i in pod1_txt.read().split():
    pod1.append(float(i))
pod1_txt.close()

pod2_txt = open('podatnośćL50.txt','r')
pod2 = []
for i in pod2_txt.read().split():
    pod2.append(float(i))
pod2_txt.close()

pod3_txt = open('podatnośćL100.txt','r')
pod3 = []
for i in pod3_txt.read().split():
    pod3.append(float(i))
pod3_txt.close()

t= np.linspace(1, 3.5, 20) 


# ## Magnetyzacja

# In[19]:


plt.rcParams["figure.figsize"] = 10,8

plt.plot(t, mag1, marker='o', markersize=10, color='navy', label='L=10')
plt.plot(t, mag2, marker='*', markersize=10, color='maroon', label='L=50')
plt.plot(t, mag3, marker='^', markersize=10, color='gold', label='L=100')
plt.xlabel('T*  -  temperatura', fontsize=16)
plt.ylabel('<m> [-]  -  magnetyzacja', fontsize=16)
plt.title('Zależność magnetyzacji od temperatury \n <m>(T*)', fontsize=20)
plt.legend()


# ## Podatność magnetyczna

# In[25]:


plt.rcParams["figure.figsize"] = 10,8

plt.plot(t, pod1, marker='o', markersize=10, color='navy', label='L=10')
plt.plot(t, pod2, marker='*', markersize=10, color='maroon', label='L=50')
plt.plot(t, pod3, marker='^', markersize=10, color='gold', label='L=100')
plt.xlabel('T*  -  temperatura', fontsize=16)
plt.ylabel("$ \chi $ [1/J]  -  podatność magnetyczna", fontsize=16)
plt.title('Zależność podatności od temperatury \n $ \chi $ (T*)', fontsize=20)
plt.legend()

