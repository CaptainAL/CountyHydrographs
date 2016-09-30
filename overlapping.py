# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 13:10:38 2016

@author: alex.messina
"""

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

#%%        
                  
for site in sites:
    print site
    site_data = All_Flow[All_Flow['Site ID'] == site]
    #print len(site_data)
    
    ## Subset dataseries for each site by Year (Year1 = 2015, Year2 = 2016)
    Year1 = site_data[site_data['Year'] == 2015]
    Year2 = site_data[site_data['Year'] == 2016]

    Year1['dt_index'] = Year1.index
    Year1['Day'] = Year1.index.day
    Year1['Month'] = Year1.index.month
    Year1['Hour'] = Year1.index.hour
    Year1.reindex()

    Year2['dt_index'] = Year2.index
    Year2['Day'] = Year2.index.day
    Year2['Month'] = Year2.index.month
    Year2['Hour'] = Year2.index.hour















