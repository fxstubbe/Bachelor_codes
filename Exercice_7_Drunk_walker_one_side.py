#!/usr/bin/env python
# coding: utf-8

# ## Ex7: Considérer un promeneur se déplaçant sur un pont. Il part du centre du pont et, à chaque pas, il se déplace d'un mètre sur la droite ou sur la gauche. Sachant que le pont est large de 7m, estimer la probabilité qu'il tombe du pont après T pas (T allant jusque 100). Représenter les résultats graphiquement.
# 

# ### 1) Paramètres de la simulation

# Définition du pont et du point de départ sur le pont

# In[9]:


Left_side = -3
Right_side = 3
Start = 0


# Définition du nombre de pas maximum et du nombre de marcheurs

# In[2]:


Steps = 100
Walkers = 10000


# ### 2) Packages et Initialisation

# In[3]:


import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# Un data frame
#     - col 1 : distance avant la chute
#     - col 2 : marcheurs étant tombés
#     - col 1 : coté de la chute
# 

# In[14]:


rwalk = pd.DataFrame({'NB_Steps' : [steps for steps in range(Steps+1)] , 
                    'Falling_Walkers' : [0 for walkers in range(Steps+1)]}, 
                       columns=['NB_Steps', 'Falling_Walkers'])


# ### 3) Définition des fonctions

# ##### La fonction de marche
# 

# In[5]:


def Walk():
    deplacement = random.choice([-1,1])
    return deplacement


# ##### La fonction de distance de marche avant la chute

# Prends en argument :
#     - Le nombre maximum de pas que le marcheur peut faire
#     - L'extrémité gauche du pont
#     - L'extrémité droite du pont
#     - Le point de départ du marcheur
#     
# Retourne : 
#     - un tupple : ( côté de la chute, distance avant la chute ) 
#     

# In[18]:


def Falling_distance(max_steps, left_start, right_start, start_position):
    
    position = start_position
    distance = 0
    
    for steps in range (0, max_steps+1):
        position += Walk()
        distance += 1
        if position > right_start or position < left_start :
            return (distance)
            break
        


# ### 4) Simulation

# On lance plusieurs marcheurs en même temps et on incrémente le dataframe
# 

# In[25]:


for i in range (Walkers):
    FallingDistance  = Falling_distance(Steps, Left_side, Right_side, Start)
    if FallingDistance is None : 
        pass
    else: rwalk.loc[rwalk["NB_Steps"] == FallingDistance, 'Falling_Walkers'] += 1


# On ajoute une colonne, contenant la probabilité, au dataframe
# 

# In[26]:


col = rwalk.apply ( lambda row : ((row['Falling_Walkers']) / Walkers)*100, axis = 1 ) 
rwalk["% Falling"] = col


# ### 5) Visualisation

# In[29]:


sns.set()
sns.lineplot(x = 'NB_Steps', y = '% Falling', data = rwalk)
plt.ylim(0, rwalk['% Falling'].max()+2)
plt.xlim(0, None)

plt.show()


# On observe que la probabilité de tomber après T pas diminue avec T augmentant. En effet, la probabilité de tomber après T est assez faible, il est fort probable qu'il soit déjà tomber avant
