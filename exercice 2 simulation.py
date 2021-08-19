# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 00:22:58 2021

@author: Slim Zéférino AGBAHOUNGBA
"""


import numpy as np
import matplotlib.pyplot as plt



# 1. Tirons les realisations de 10 variables aléatoires suivant 
# une loi de Khi-deux à deux dégré de liberté
n=10
yi=np.random.chisquare(2,n)
yi

#2. Calculons la realisation  de la moyenne empirique Yn_bar
yn_bar=np.sum(yi)/n
yn_bar

#3. Calculons la realisation de cette variable zn transformée
zn=np.sqrt(n)*(yn_bar-2)/2
zn

#Repetons cette proccedure 5000 fois pour obtenir l'echantillon de la 
#la variable zn
n=1000 #taille de l'echatillon'
N=5000# nbre de repetitions 5000 fois

#reprise des questions 1 a 3

############### Pour la question 1
yn=np.random.chisquare(2,(n,N))
yn

############### Pour la question 2
yn_bar=np.sum(yn, axis=0)*1/n
yn

############## Pour la question 3
zn=np.sqrt(n)*(yn_bar-2)/2
zn

#5. Constuisons l'histogramme de ces 5000 réalistions qui sera comparer 
# a la densité d'une loi normal centrée reduite N(0,1)

#histogramme de zn
plt.hist(zn,20)
plt.title('histogramme zn avec n=1000')
plt.xlabel('taille d''enchantollon n =1000')
plt.ylabel('nobre de realisations n=5000')


# la densité d'une loi normal centrée reduite N(0,1)
### densité de 5000 réalisations d'une variable aléatoire suivant une loi normale
import matplotlib.pyplot as plt
import numpy as np
mu, sigma = 0, 1
s = np.random.normal(mu, sigma, 5000)
count, bins, ignored = plt.hist(s, 20, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=3, color='y')
plt.show()

#Comparaison 

import matplotlib.pyplot as plt
import numpy as np
mu, sigma = 0,1
# Create the bins and histogram
count, bins, ignored = plt.hist(zn, 20, normed=True)
# Plot the distribution curve
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=3, color='y')
plt.show()

bins


#### CONCLUSION: Nous pouvons dire que l'histogramme des 5000 réalisations 
##### de la variable transformée Z est celui de la densité d'une loi normale centrée réduite
