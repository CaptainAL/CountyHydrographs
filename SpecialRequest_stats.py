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
import math

from scipy import stats

## Set Pandas display options
pd.set_option('display.large_repr', 'truncate')
pd.set_option('display.width', 180)
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 13)


#%%

## Data directories
maindir = 'C:/Users/alex.messina/Documents/GitHub/CountyHydrographs/'

## READ IN RAW DATA
All_Flow = pd.DataFrame.from_csv(maindir+'Seven_Combined.csv')
sites = All_Flow['Site ID'].unique()
sites  = [x for x in sites if str(x) != 'nan']


#%%
          
Stats = pd.DataFrame(columns=['Mean','Median','Mode','Max','Min','N','STD','95% CI_1','95% CI_2'])
for site in sites:
    print site
    site_data = All_Flow[All_Flow['Site ID'] == site]
    #print len(site_data)
    

    ## Subset dataseries for each site by Year (Year1 = 2015, Year2 = 2016)
    Year1 = site_data[site_data['Year'] == 2015]
    Year2 = site_data[site_data['Year'] == 2016]

    ## Append Year 1-2015
    mean, std = Year1['Flow (gpm)'].mean(), Year1['Flow (gpm)'].std()
    CIl, CIh = stats.norm.interval(0.95,loc=mean,scale=std/math.sqrt(len(Year1)))
    
    Stats = Stats.append(pd.DataFrame({'Mean':"%.2f"%mean,'Median':"%.2f"%Year1['Flow (gpm)'].median(),'Mode':"%.2f"%Year1['Flow (gpm)'].mode()[0],'Max':"%.2f"%Year1['Flow (gpm)'].max(),'Min':"%.2f"%Year1['Flow (gpm)'].min(),'N':Year1['Flow (gpm)'].count(),'STD':"%.2f"%std,'95% CI_1':"%.2f"%CIl,'95% CI_2':"%.2f"%CIh},index=[site+'-2015']))

    ## Append Year 2-2016
    mean, std = Year2['Flow (gpm)'].mean(), Year2['Flow (gpm)'].std()
    CIl, CIh = stats.norm.interval(0.95,loc=mean,scale=std/math.sqrt(len(Year2)))
    
    Stats = Stats.append(pd.DataFrame({'Mean':"%.2f"%mean,'Median':"%.2f"%Year2['Flow (gpm)'].median(),'Mode':"%.2f"%Year2['Flow (gpm)'].mode()[0],'Max':"%.2f"%Year2['Flow (gpm)'].max(),'Min':"%.2f"%Year2['Flow (gpm)'].min(),'N':Year2['Flow (gpm)'].count(),'STD':"%.2f"%std,'95% CI_1':"%.2f"%CIl,'95% CI_2':"%.2f"%CIh},index=[site+'-2016']))
    
    
    
    

Stats = Stats[['N','Max','Min','Mean','STD','95% CI_1','95% CI_2','Median','Mode']]
print Stats
#    print  site+'-2015: '+
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    