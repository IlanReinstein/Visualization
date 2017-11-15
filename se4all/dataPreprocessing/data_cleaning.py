#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 09:48:57 2017

@author: IlanReinstein
"""


import pandas as pd
import glob

#Path to all the files
fpath = 'se4all/raw_data/*.csv'

#CNew column names
col_list = ['perc_cob', 'viv_ocup', 
            'viv_ocup_elec', 'deficit_viv', 
            'pob', 'hab_per_viv', 'rate_of_cov', 
            'pob_acceso', 'pob_no_acceso']


#List of countries
paises = ['Argentina', 'Barbados', 'Belize', 'Bolivia', 'Brazil', 
          'Chile', 'Colombia', 'Costa Rica',' Cuba', 'Ecuador', 
          'Granada', 'Guatemala', 'Guyana', 'Haiti', 'Honduras', 
          'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 
          'Peru', 'Dominican Republic', 'El Salvador', 'Suriname', 
          'Trinidad and Tobago', 'Uruguay', 'Venezuela']
    

def data_cleaner(file):
    '''
    Cleaning procedure for each of the csv files.
    Filter year, remove unwanted columns, reindexing the table,
    change strings to numeric values.
    '''
    temp = pd.read_csv(file, index_col = 0)
    temp = temp[temp.index <= 2015]
    temp.index = temp.index.astype(int)
    filt_col = [col for col in temp.columns 
                if col.startswith('Tasa') 
                or col.startswith('Unnamed')]
    temp = temp.drop(filt_col, axis = 1)
    temp.columns = col_list
    temp = temp.astype(str)
    temp.rate_of_cov = temp.rate_of_cov.str.replace('%','')
    temp.perc_cob = temp.perc_cob.str.replace('%','')
    temp = temp.apply(lambda x: x.str.replace(',',''))
    temp = temp.astype(float)
    temp['country'] = file.split('/')[2].split('.')[0]
    temp.index.names = ['year']
    return temp

def read_all(fpath, long = False):
    '''
    Read all csvs from the Excel file and merges them into one big table.
    long: Default is False. If True, returns long format table.
    '''
    final_table = pd.DataFrame()
    
    for file in glob.glob(fpath):
        temp = data_cleaner(file)
        temp = reorder(temp)
        final_table = final_table.append(temp)     
       
    return final_table
    

def reorder(table):
    '''
    Reorder columns. Brings country column to the front for easier
    manipulation and filtering.
    '''
    cols = table.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    return table[cols]

    
data = read_all(fpath)
data.to_csv('data.csv')