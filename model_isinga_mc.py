#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[3]:


@numba.jit(nopython=True)
def stan_poczatkowy_nieuporzadkowany(L):   
    macierz_spinow = np.random.choice(np.array([-1, 1]), size=(L, L))
    return macierz_spinow

@numba.jit(nopython=True)
def stan_poczatkowy_uporzadkowany(L):
    macierz_spinow = np.ones((L, L))
    return macierz_spinow

@numba.jit(nopython=True)
def ruch_jednego_spinu(spiny, beta, L):
    for i in range(L):
        for j in range(L):
                rzad = np.random.randint(0, L)
                kolumna = np.random.randint(0, L)
                spin =  spiny[rzad, kolumna]
                energia_sasiadow = spiny[(rzad + 1) % L, kolumna] + spiny[rzad, (kolumna + 1) % L] + spiny[(rzad - 1) % L, kolumna] + spiny[rzad, (kolumna - 1) % L]
                zmiana_energii = 2 * spin * energia_sasiadow
                if zmiana_energii < 0:
                    spin *= -1
                elif rand() < np.exp(- zmiana_energii * beta):
                    spin *= -1
                spiny[rzad, kolumna] = spin
    return spiny

@numba.jit(nopython=True)
def calkowita_energia_ukladu(spiny):
    energia_calkowita = 0
    for rzad in range(len(spiny)):
        for kolumna in range(len(spiny)):
            dany_spin = spiny[rzad, kolumna]
            energia_sasiadow = spiny[(rzad + 1) % L, kolumna] + spiny[rzad, (kolumna + 1) % L] + spiny[(rzad - 1) % L, kolumna] + spiny[rzad, (kolumna - 1) % L]
            energia_calkowita += - energia_sasiadow * dany_spin
    return energia_calkowita/4.

@numba.jit(nopython=True)
def magnetyzacja(spiny):
    L = len(spiny)
    m = np.sum(spiny) * 1/(L*L)
    return m


# In[9]:


@numba.jit
def symulacja(L):
    
    dt = 20                  
    K = 10**6  
    K0 = 10**4
    kroki_mc = K - K0

    T   = np.linspace(1, 3.5, dt)
    M = np.zeros(dt)
    X = np.zeros(dt)
    n1  = 1.0/kroki_mc
    n2  = 1.0/(kroki_mc * kroki_mc) 

    for t in range(dt):
        M1 = M2 = 0
        spiny = stan_poczatkowy_uporzadkowany(L)
        iT=1.0/T[t]
        
        pliktxt_mag = open('mag_n' + str(t) + '.txt', 'a')
        
        for i in range(K):
            ruch_jednego_spinu(spiny, iT, L)  
            
            if i >= K0:
                Mag = magnetyzacja(spiny) 
                pliktxt_mag.write(str(Mag) + '\n')

                M1 += abs(Mag)
                M2 += Mag*Mag 
            
        pliktxt_mag.close()
        
        M[t] = n1*M1
        X[t] = L*L *(n1*M2 - n2*M1*M1)*iT
        
        pliktxt_m = open('magnetyzacjaL' + str(L) + '.txt', 'a')
        pliktxt_m.write(str(M[t]) + '\n')
        pliktxt_m.close()
        
        pliktxt_p = open('podatnośćL'+ str(L) + '.txt', 'a')
        pliktxt_p.write(str(X[t]) + '\n')
        pliktxt_p.close()
        
    return M, X


# In[10]:


m100, x100 = symulacja(100)


# ---

# # Konfiguracja spinów
# 
# ## L=10 
# 
# ## L=100 
# 
# ## T_{1} = 1 
# 
# ## T_{2} = 2.26 
# 
# ## T_{3} = 4 

# In[11]:


def symulacja_wykresy(L, temp):   
            
    spiny = stan_poczatkowy(L)   
    spinyPlot(spiny, 0, L, temp)
    
    if L == 10:
        zakres = 10001
    if L == 100:
        zakres = 1000001
        
    for i in range(zakres):
        ruch_jednego_spinu(spiny, 1.0/temp, L)
        if i == 1:       
             spinyPlot(spiny, i, L, temp)
        if i == 10:       
             spinyPlot(spiny, i, L, temp)
        if i == 100: 
             spinyPlot(spiny, i, L, temp)
        if i == 1000:     
             spinyPlot(spiny, i, L, temp)
        if i == 10000:    
             spinyPlot(spiny, i, L, temp)
        if i == 100000:    
             spinyPlot(spiny, i, L, temp)
        if i == 1000000:    
             spinyPlot(spiny, i, L, temp)
       

            
def spinyPlot(config, i, L, temp):   
    X, Y = np.meshgrid(range(L), range(L))     
    plt.pcolormesh(X, Y, config, cmap=plt.cm.PuRd);
    plt.title('Temperatura=' + str(temp) + ' ' + 'Czas=%d'%i)
    plt.show()


# ## wersja z gifem

# In[14]:


@numba.jit
def symulacja_gif(L, t):   
    
    t = float(t)
    
    filenames = []
    images = []
           
    config = stan_poczatkowy(L)   
    X, Y = np.meshgrid(range(L), range(L))     
    plt.pcolormesh(X, Y, config, cmap=plt.cm.PuRd);
    plt.title('L=%d'%L + ' ' +'Temperatura=' + str(t) + ' ' + 'Czas=%d'%0)
    nazwa = "wykres"+'L'+str(L)+'T'+str(t)+'n'+str(0)+".png"
    filenames.append(nazwa)    
    plt.savefig(nazwa)
    
    if L == 10:
        zakres = 1001
    
    if L == 100:
        zakres = 1000001
        
    for i in range(zakres):
        ruch_jednego_spinu(config, 1.0/t, L)
        if i == 1:       
            X, Y = np.meshgrid(range(L), range(L))     
            plt.pcolormesh(X, Y, config, cmap=plt.cm.PuRd);
            plt.title('L=%d'%L + ' ' +'Temperatura=' + str(t) + ' ' + 'Czas=%d'%i)
            nazwa = "wykres"+'L'+str(L)+'T'+str(t)+'n'+str(i)+".png"
            filenames.append(nazwa)    
            plt.savefig(nazwa)
        if i == 10:       
            X, Y = np.meshgrid(range(L), range(L))     
            plt.pcolormesh(X, Y, config, cmap=plt.cm.PuRd);
            plt.title('L=%d'%L + ' ' +'Temperatura=' + str(t) + ' ' + 'Czas=%d'%i)
            nazwa = "wykres"+'L'+str(L)+'T'+str(t)+'n'+str(i)+".png"
            filenames.append(nazwa)    
            plt.savefig(nazwa)
        if i == 100: 
            X, Y = np.meshgrid(range(L), range(L))     
            plt.pcolormesh(X, Y, config, cmap=plt.cm.PuRd);
            plt.title('L=%d'%L + ' ' +'Temperatura=' + str(t) + ' ' + 'Czas=%d'%i)
            nazwa = "wykres"+'L'+str(L)+'T'+str(t)+'n'+str(i)+".png"
            filenames.append(nazwa)    
            plt.savefig(nazwa)
        if i == 1000:     
            X, Y = np.meshgrid(range(L), range(L))     
            plt.pcolormesh(X, Y, config, cmap=plt.cm.PuRd);
            plt.title('L=%d'%L + ' ' +'Temperatura=' + str(t) + ' ' + 'Czas=%d'%i)
            nazwa = "wykres"+'L'+str(L)+'T'+str(t)+'n'+str(i)+".png"
            filenames.append(nazwa)    
            plt.savefig(nazwa)        
        if i == 10000:    
            X, Y = np.meshgrid(range(L), range(L))     
            plt.pcolormesh(X, Y, config, cmap=plt.cm.PuRd);
            plt.title('L=%d'%L + ' ' +'Temperatura=' + str(t) + ' ' + 'Czas=%d'%i)
            nazwa = "wykres"+'L'+str(L)+'T'+str(t)+'n'+str(i)+".png"
            filenames.append(nazwa)    
            plt.savefig(nazwa)
        if i == 100000:    
            X, Y = np.meshgrid(range(L), range(L))     
            plt.pcolormesh(X, Y, config, cmap=plt.cm.PuRd);
            plt.title('L=%d'%L + ' ' +'Temperatura=' + str(t) + ' ' + 'Czas=%d'%i)
            nazwa = "wykres"+'L'+str(L)+'T'+str(t)+'n'+str(i)+".png"
            filenames.append(nazwa)    
            plt.savefig(nazwa)
        if i == 1000000:    
            X, Y = np.meshgrid(range(L), range(L))     
            plt.pcolormesh(X, Y, config, cmap=plt.cm.PuRd);
            plt.title('L=%d'%L + ' ' +'Temperatura=' + str(t) + ' ' + 'Czas=%d'%i)
            nazwa = "wykres"+'L'+str(L)+'T'+str(t)+'n'+str(i)+".png"
            filenames.append(nazwa)    
            plt.savefig(nazwa)
                
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave('symulacja' + 'L' + str(L) + 'T' + str(t) + '.gif', images, fps=0.8) 


# ---

# ## Trajektorie

# In[67]:


@numba.jit
def symulacja_trajektorie(L, v):
                 
    mcSteps = 10**6    

    T = 1.7
    M = np.zeros(mcSteps)

    config = stan_poczatkowy(L)
    iT=1.0/T
        
    for i in range(mcSteps):
        ruch_jednego_spinu(config, iT, L)            
        Mag = magnetyzacja(config) 
            
        M[i] = Mag
            
        pliktxt_mag = open('magnetyzacja_trajektorieL' + str(L) + 'v' + str(v) + '.txt', 'a')
        pliktxt_mag.write(str(Mag))
        pliktxt_mag.write('\n')
        pliktxt_mag.close()
            
    return M

