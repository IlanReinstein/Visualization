#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:44:12 2017

@author: IlanReinstein
"""

import pandas as pd

paises = ['Argentina', 'Barbados', 'Belize', 'Bolivia', 'Brazil', 
          'Chile', 'Colombia', 'Costa Rica',' Cuba', 'Ecuador', 
          'Grenada', 'Guatemala', 'Guyana', 'Haiti', 'Honduras', 
          'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 
          'Peru', 'Dominican Republic', 'El Salvador', 'Suriname', 
          'Trinidad and Tobago', 'Uruguay', 'Venezuela']

data = pd.read_csv('se4all/dataPreprocessing/data.csv', index_col = False)


def filter_data(df, year = 2015, var = 'perc_cob'):
    '''
    Replaces names of the countries for compatibility with Topojson files.
    Default year and variable of interest: 2015 and perc_cob (% population with access)
    Possible years: 1970-2015
    Other variables: 'perc_cob', 'viv_ocup', 
                    'viv_ocup_elec', 'deficit_viv', 
                    'pob', 'hab_per_viv', 'rate_of_cov', 
                    'pob_acceso', 'pob_no_acceso'
    '''
    df_clean = df[df.year == year]
    df_clean.loc[:,'country'] = paises
    df_clean = df_clean.loc[:,[var, 'country']]
    return df_clean


acceso_2015 = filter_data(data)

acceso_2015.to_csv('se4all/vis1/data/data.csv')