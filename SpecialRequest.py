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

plt.close('all')

#%%


def shade_weekends(Year,Ax,Color):
    Year = int(Year) ## just to be sure
    ## Make list of weekend days
    datetime_array = pd.date_range(dt.datetime(Year,5,1),dt.datetime(Year,10,1),freq='D')
    weekends = []    
    for i in range(len(datetime_array)):
        if datetime_array[i].weekday()>=5:
            print datetime_array[i]
            weekends.append(datetime_array[i])   
    ## Shade over weekend days in the plot
    for day in weekends:
        Ax.axvspan(day, day+dt.timedelta(days=1),facecolor= Color, edgecolor='none', alpha=.2)
    ## One just for labeling purposes
    Ax.axvspan(0,1,facecolor= Color, edgecolor='none', alpha=.2, label = str(Year)+' Weekends')
    return

#%%

## Data directories
maindir = 'C:/Users/alex.messina/Documents/GitHub/CountyHydrographs/'

## READ IN RAW DATA
All_Flow = pd.DataFrame.from_csv(maindir+'Seven_Combined.csv')
sites = All_Flow['Site ID'].unique()
sites  = [x for x in sites if str(x) != 'nan']

for site in sites:
    print site
    site_data = All_Flow[All_Flow['Site ID'] == site]
    #print len(site_data)

#%%
    
    ## Subset dataseries for each site by Year (Year1 = 2015, Year2 = 2016)
    Year1 = site_data[site_data['Year'] == 2015]
    Year2 = site_data[site_data['Year'] == 2016]
    ## Open plot window and title by Site Name
    fig, ax1 = plt.subplots(1,1,figsize=(14,6))
    fig.suptitle('Site: '+site,fontsize=16)
    ## Set X axis labels visible/invisible (you can make the secondary X axis visible to make sure the dates line up, then turn off so not confusing)
    ax1.tick_params(labelbottom=True, labeltop=False)
    ### Plot Year 1 flow
    ax1.plot_date(Year1['Flow (gpm)'].index,Year1['Flow (gpm)'],ls='-',marker='None',c='r',label='2015')
    
    ## Add Secondary X axis for Year 2
    ax2 = ax1.twiny()
    ax2.tick_params(labelbottom=False, labeltop=False) ## Turn labeltop=True to check both axes
    ### Plot Year 2 flow
    ax2.plot_date(Year2['Flow (gpm)'].index,Year2['Flow (gpm)'],ls='-',marker='None',c='g',label='2016')

    ## Set X axis limits
    ax1.set_xlim(dt.datetime(2015,7,31),dt.datetime(2015,9,1))
    xloc = plt.MaxNLocator(20)
    ax1.xaxis.set_major_locator(xloc)
    #ax1.set_xticks(pd.date_range(dt.datetime(2015,7,31),dt.datetime(2015,9,1),freq='D')[::3]) ## Every three days
    ax2.set_xlim(dt.datetime(2016,7,31),dt.datetime(2016,9,1))
    
    ## Format X axis labels
    for ax in fig.axes:
        ax.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m/%d %H:%M'))
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=30, fontsize=10)
    
    ## Format Y axis label and limits
    ax1.set_ylabel('Flow (gpm)')
    ax1.set_ylim(-3)
       
    ### Shade over weekends
    shade_weekends(2015,ax1,'red')
    shade_weekends(2016,ax2,'green')
    
    ## Legends
    leg = ax1.legend(fancybox=True, loc=9, bbox_to_anchor=(0.70,1.2))# loc='upper left')
    #leg.get_frame().set_alpha(1)
    for legobj in leg.legendHandles:
        legobj.set_linewidth(2.0)
    leg = ax2.legend(fancybox=True, bbox_to_anchor=(1,1.2))# loc='upper right')
    for legobj in leg.legendHandles:
        legobj.set_linewidth(2.0)
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)

    plt.savefig(maindir+site+'full range.png')

#%%



         
    
    


