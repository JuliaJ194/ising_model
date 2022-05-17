#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# ## L = 10

# In[2]:


traj_10_1_txt = open('magnetyzacja_trajektorieL10v1.txt','r')
traj_10_1 = []
for i in traj_10_1_txt.read().split():
    traj_10_1.append(float(i))
traj_10_1_txt.close()

traj_10_2_txt = open('magnetyzacja_trajektorieL10v2.txt','r')
traj_10_2 = []
for i in traj_10_2_txt.read().split():
    traj_10_2.append(float(i))
traj_10_2_txt.close()

traj_10_3_txt = open('magnetyzacja_trajektorieL10v3.txt','r')
traj_10_3 = []
for i in traj_10_3_txt.read().split():
    traj_10_3.append(float(i))
traj_10_3_txt.close()

traj_10_4_txt = open('magnetyzacja_trajektorieL10v4.txt','r')
traj_10_4 = []
for i in traj_10_4_txt.read().split():
    traj_10_4.append(float(i))
traj_10_4_txt.close()

traj_10_5_txt = open('magnetyzacja_trajektorieL10v5.txt','r')
traj_10_5 = []
for i in traj_10_5_txt.read().split():
    traj_10_5.append(float(i))
traj_10_5_txt.close()


# In[27]:


plt.rcParams["figure.figsize"] = 12,6
plt.plot(list(range(len(traj_10_1))), traj_10_1, color='cornflowerblue')
plt.plot(list(range(len(traj_10_1))), traj_10_2, color='deeppink')
#plt.plot(list(range(len(traj_10_1))), traj_10_3)
plt.plot(list(range(len(traj_10_1))), traj_10_4, color='gold')
plt.plot(list(range(len(traj_10_1))), traj_10_5, color='chartreuse')
plt.ylim(-1,1)
plt.xlim(0, 1000)
plt.title('Trajektorie dla T*=1.7 dla L=10', fontsize=20)
plt.xlabel('t [MCS]', fontsize=16)
plt.ylabel('m', fontsize=16)


# ## L = 50

# In[5]:


traj_50_1_txt = open('magnetyzacja_trajektorieL50v1.txt','r')
traj_50_1 = []
for i in traj_50_1_txt.read().split():
    traj_50_1.append(float(i))
traj_50_1_txt.close()

traj_50_2_txt = open('magnetyzacja_trajektorieL50v2.txt','r')
traj_50_2 = []
for i in traj_50_2_txt.read().split():
    traj_50_2.append(float(i))
traj_50_2_txt.close()

traj_50_3_txt = open('magnetyzacja_trajektorieL50v3.txt','r')
traj_50_3 = []
for i in traj_50_3_txt.read().split():
    traj_50_3.append(float(i))
traj_50_3_txt.close()

traj_50_4_txt = open('magnetyzacja_trajektorieL50v4.txt','r')
traj_50_4 = []
for i in traj_50_4_txt.read().split():
    traj_50_4.append(float(i))
traj_50_4_txt.close()


# In[26]:


plt.rcParams["figure.figsize"] = 12,6
plt.plot(list(range(len(traj_50_1))), traj_50_1, color='cornflowerblue')
plt.plot(list(range(len(traj_50_1))), traj_50_2, color='deeppink')
plt.plot(list(range(len(traj_50_1))), traj_50_3, color='gold')
plt.plot(list(range(len(traj_50_1))), traj_50_4, color='chartreuse')
plt.ylim(-1,1)
plt.xlim(0, 10000)
plt.title('Trajektorie dla T*=1.7 dla L=50', fontsize=20)
plt.xlabel('t [MCS]', fontsize=16)
plt.ylabel('m', fontsize=16)


# ## L =100

# In[7]:


traj_100_1_txt = open('magnetyzacja_trajektorieL100v1.txt','r')
traj_100_1 = []
for i in traj_100_1_txt.read().split():
    traj_100_1.append(float(i))
traj_100_1_txt.close()

traj_100_2_txt = open('magnetyzacja_trajektorieL100v2.txt','r')
traj_100_2 = []
for i in traj_100_2_txt.read().split():
    traj_100_2.append(float(i))
traj_100_2_txt.close()

traj_100_3_txt = open('magnetyzacja_trajektorieL100v3.txt','r')
traj_100_3 = []
for i in traj_100_3_txt.read().split():
    traj_100_3.append(float(i))
traj_100_3_txt.close()

traj_100_4_txt = open('magnetyzacja_trajektorieL100v4.txt','r')
traj_100_4 = []
for i in traj_100_4_txt.read().split():
    traj_100_4.append(float(i))
traj_100_4_txt.close()


# In[25]:


plt.rcParams["figure.figsize"] = 12,6
plt.plot(list(range(len(traj_100_1))), traj_100_1, color='cornflowerblue')
plt.plot(list(range(len(traj_100_1))), traj_100_2, color='deeppink')
plt.plot(list(range(len(traj_100_1))), traj_100_3, color='gold')
plt.plot(list(range(len(traj_100_1))), traj_100_4, color='chartreuse')
plt.ylim(-1,1)
plt.xlim(0, 10000)
plt.title('Trajektorie dla T*=1.7 dla L=100', fontsize=20)
plt.xlabel('t [MCS]', fontsize=16)
plt.ylabel('m', fontsize=16)

