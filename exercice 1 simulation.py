# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 23:21:12 2021

@author: Slim Zéférino AGBAHOUNGBA
"""

import numpy as np
import matplotlib.pyplot as plt


# Soit Yi suit la loi uniforme [0,10] et E(Yi)=5
#1. Tirons des realistaions de Yi
Yi=np.random.uniform(0,10,5)
Yi

#2 Calculons la réalisation de la moyenne empirique Y_bar 
Y_bar=np.sum(Yi)/5
Y_bar

#3. répétons 5000 la réalisation de 1 et 2
n=5 # Nbre de realisations
N=5000 # Nbre de repetitions
Yj=np.random.uniform(0,10,(n,N)) #5000 realisations 

Y1_bar=np.sum(Yj, axis = 0)*1/n #Moyenne empirique des 5000 realisations 

#4. Construction des l'histogramme des 5000 realistaions 
plt.hist(Y1_bar)

#5. Répètons l'experience avec les valeurs suivantes:
    
    #############Pour n=10###############
    
n=10
N=5000
Y10=np.random.uniform(0,10,10)
Y10_bar=np.sum(Y10, axis=0)*1/n
plt.hist(Y10_bar)
plt.title('histogramme de la moyenne empirique avec n=10')
plt.xlabel('taille d''enchantollon n =10')
plt.ylabel('nobre de realisations n=5000')

#############Pour n =  100###############

n=100
N=5000
Y100=np.random.uniform(0,10,100)
Y100_bar=np.sum(Y100, axis=0)*1/n
plt.hist(Y100_bar)
plt.title('histogramme de la moyenne empirique avec n=100')
plt.xlabel('taille d''enchantollon n =100')
plt.ylabel('nobre de realisations n=5000')

###########Pour n=1000 ######################

n=1000
N=5000
Y1000=np.random.uniform(0,10,1000)
Y1000_bar=np.sum(Y100, axis=0)*1/n
plt.hist(Y1000_bar)
plt.title('histogramme de la moyenne empirique avec n=1000')
plt.xlabel('taille d''enchantollon n =1000')
plt.ylabel('nobre de realisations n=5000')

####################### Pour n=10000

n=10000
N=5000
Y10000=np.random.uniform(0,10,10000)
Y10000_bar=np.sum(Y100, axis=0)*1/n
plt.hist(Y10000_bar)
plt.title('histogramme de la moyenne empirique avec n=10000')
plt.xlabel('taille d''enchantollon n =10000')
plt.ylabel('nobre de realisations n=5000')


#Remarque :

#On remarque que Plus la taille de l'échantilon augmente et le nombre de repetition  de l'echantillon augmente
# on s'appoche d'une distribution de la loi de Poisson  
