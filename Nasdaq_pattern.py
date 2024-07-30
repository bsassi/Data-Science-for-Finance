#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


# _Analyse microstructure des mouvements de prix du Nasdaq100 \- Version 1_   
# 
# 

# In[4]:


J = pd.read_excel('6FDJUIN.xlsx')
J['time'] = pd.to_datetime(J['time'], format='%H:%M:%S').dt.time
J['time_str'] = J['time'].astype(str) # Convertir time en chaînes de caractères
J.head()


# Petit rappel : 
# 
# - Close1 : correspond au prix de clôture pour la journée du 03/06 \(lundi\)
# - Close2 : correspond au prix de clôture pour la journée du 04/06 \(mardi\)
# - Close3 : correspond au prix de clôture pour la journée du 05/06 \(mercredi\)
# - Close4 : correspond au prix de clôture pour la journée du 06/06 \(jeudi\)
# - Close5 : correspond au prix de clôture pour la journée du 07/06 \(vendredi\)  
# - Close6 : correspond au prix de clôture pour la journée du 10/06 \(lundi\)
# - Close7 : correspond au prix de clôture pour la journée du 11/06 \(mardi\)
# 
# 

# In[5]:


# Plot

close_columns = [col for col in J.columns if 'close' in col]

time_labels = J['time_str'][::15]

# Plot each 'close' column over time with improved x-axis labeling
fig, axes = plt.subplots(len(close_columns), 1, figsize=(12, 6 * len(close_columns)), sharex=True)

for ax, col in zip(axes, close_columns):
    ax.plot(J['time_str'], J[col], label=col, color = 'blue')
    ax.set_ylabel(col)
    ax.legend()
    ax.grid(True)
    ax.set_xticks(time_labels.index)
    ax.set_xticklabels(time_labels)

# Set x-axis label for the last subplot
axes[-1].set_xlabel('Time')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)
plt.show()


# In[6]:


# Statistiques descriptives 

# Initialize a dictionary to store descriptive statistics for each 'close' column
descriptive_stats = {}

# Loop through each 'close' column and calculate descriptive statistics
for col in close_columns:
    descriptive_stats[col] = J[col].describe()

# Convert the dictionary to a DataFrame for better visualization
descriptive_stats_df = pd.DataFrame(descriptive_stats)
print(descriptive_stats_df)


# In[7]:


# Histogramme 

fig, axes = plt.subplots(len(close_columns), 1, figsize=(12, 6 * len(close_columns)))

for ax, col in zip(axes, close_columns):
    ax.hist(J[col], bins=20, color='blue', edgecolor='black')
    ax.set_title(f'Histogramme de {col}')
    ax.set_xlabel('Valeur')
    ax.set_ylabel('Fréquence')

plt.tight_layout()
plt.show()


# In[11]:


# Filtrer les données entre 9:30 et 10:00 - Open Market
start_time = pd.to_datetime('09:30:00', format='%H:%M:%S').time()
end_time = pd.to_datetime('10:00:00', format='%H:%M:%S').time()

filtered_data = J[(J['time'] >= start_time) & (J['time'] <= end_time)]

# Définir les colonnes 'close' retenu pour l'analyse
close_columns = [col for col in J.columns if 'close' in col]

# Calcule des statistiques descriptives pour les données filtrées
for col in close_columns:
    stats = filtered_data[col].describe()
    print(f"Statistiques descriptives pour {col} de 9:30 à 10:00:")
    print(stats)
    print("\n")


# In[12]:


# Plot 

# Plot Close pour les 30 premières minutes
fig, axes = plt.subplots(len(close_columns), 1, figsize=(12, 6 * len(close_columns)), sharex=True)

for ax, col in zip(axes, close_columns):
    ax.plot(filtered_data['time'].astype(str), filtered_data[col], label=col, color='blue')
    ax.set_ylabel(col)
    ax.legend()
    ax.grid(True)

axes[-1].set_xlabel('Time')
plt.xticks(rotation=45)
plt.show()


# In[13]:


# Même analyse pour les 30 dernières minutes du marchés 

# Filtrer les données entre 15:30 et 16:00
start_time = pd.to_datetime('15:30:00', format='%H:%M:%S').time()
end_time = pd.to_datetime('16:00:00', format='%H:%M:%S').time()

filtered_data = J[(J['time'] >= start_time) & (J['time'] <= end_time)]


# In[14]:


# Statistiques descriptives 

# Définir les colonnes 'close'
close_columns = [col for col in J.columns if 'close' in col]

# Calculer les statistiques descriptives pour les données filtrées
for col in close_columns:
    stats = filtered_data[col].describe()
    print(f"Statistiques descriptives pour {col} de 15:30 à 16:00:")
    print(stats)
    print("\n")


# In[15]:


fig, axes = plt.subplots(len(close_columns), 1, figsize=(12, 6 * len(close_columns)), sharex=True)

for ax, col in zip(axes, close_columns):
    ax.plot(filtered_data['time'].astype(str), filtered_data[col], label=col, color='blue')
    ax.set_ylabel(col)
    ax.legend()
    ax.grid(True)


axes[-1].set_xlabel('Time')
plt.xticks(rotation=45)
plt.show()


# <u>**Notre analyse s'arrête ici, avec les recommandations suivantes :** </u>
# 
# - Explorer d'autres patterns \(au sein d'autres variables que 'close i' pour tout i ∈ \[1, 7\]\)
# 
# - Etudier l'existence d'une relation statistique entres les 30 premières minutes du marchés et les 30 dernières minutes. 
# 
# - Augmenter la période d'étude afin de détecter des schémas de récurrences
# 
# - Réaliser du feature engineering pour détecter de nouvelles relations \(exemple: faire un ratio entre le high/low et étudier le comportement dynamique au cours de T\)
# 
# **Une fois que ces étapes seront réalisées, il faudra passer à l'étape d'élaboration de stratégies de trading basée sur les découvertes précédentes.**  
# 
# 
