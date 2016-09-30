# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 16:40:34 2016

@author: alex.messina
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib as mpl
from matplotlib import pyplot as plt
import pandas as pd
import datetime as dt
import numpy as np

## Set Pandas display options
pd.set_option('display.large_repr', 'truncate')
pd.set_option('display.width', 180)
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 13)

#plt.close('all')


#%%

## Data directories
maindir = 'C:/Users/alex.messina/Documents/GitHub/CountyHydrographs/'

## READ IN RAW DATA
All_Flow = pd.DataFrame.from_csv(maindir+'Seven_Combined.csv')
sites = All_Flow['Site ID'].unique()
sites  = [x for x in sites if str(x) != 'nan']

          
          
fig, ax1 = plt.subplots(1,1,figsize=(12,5))          
data = []
means = []
labels = []
for site in sites:
    print site
    site_data = All_Flow[All_Flow['Site ID'] == site]
    #print len(site_data)
    
    ## Subset dataseries for each site by Year (Year1 = 2015, Year2 = 2016)
    Year1 = site_data[site_data['Year'] == 2015]
    Year2 = site_data[site_data['Year'] == 2016]




    ## Add Year 1 to data
    data.append(Year1['Flow (gpm)'].dropna())
    means.append(Year1['Flow (gpm)'].mean())
    labels.append(site+'\n 2015')
    ## Add Year 2 to data
    data.append(Year2['Flow (gpm)'].dropna())
    means.append(Year2['Flow (gpm)'].mean())
    labels.append(site+'\n 2016')


ax1.boxplot(data,labels=labels,showmeans=True,showfliers=True,notch=True,whis=1000)
## Format Y axis
ax1.set_ylabel('Flow (gpm)')
ax1.set_ylim(-3)

## Dividing lines between sites/years
for i in np.arange(0.5,20,2):
    ax1.axvline(i,color='k')

#  SITE Labels like Titles
j = 0
for site in sites:
    #print site, .035+j
    ax1.text(.05+j, 0.95, site, transform=ax1.transAxes)
    j+=.14

plt.tight_layout()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    