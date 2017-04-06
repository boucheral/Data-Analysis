###########################################################################################################################
## Question 1 - Part 2                                                                                                   ##
## - Use vehicle_collision dataset                                                                                       ##
## - For each borough, find the distribution of each collision scale                                                     ##
## - Display a few rows of the output using df.head()                                                                    ##
## - Generate a CSV output with 5 columns ('borough', 'one-vehicle', 'two-vehicles', 'three-vehicles', 'more-vehicles)   ##
###########################################################################################################################

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

## Use vehicle_collision dataset
df = pd.read_csv('../../Data/vehicle_collisions.csv', parse_dates=['DATE'])
df.head()

df2 = DataFrame( data = {'borough' : df['BOROUGH'], 'one-vehicle' : df['VEHICLE 1 TYPE'], 'two-vehicles' : df['VEHICLE 2 TYPE'], 'three-vehicles' : df['VEHICLE 3 TYPE'], 'more-vehicles' : df['VEHICLE 4 TYPE']} )
df2.head()

for index, row in df2.iterrows() :
    if pd.isnull(row['two-vehicles']) :
        row['one-vehicle'] = 1
        row['two-vehicles'] = 0
        row['three-vehicles'] = 0
        row['more-vehicles'] = 0
    elif pd.isnull(row['three-vehicles']) :
        row['one-vehicle'] = 0
        row['two-vehicles'] = 1
        row['three-vehicles'] = 0
        row['more-vehicles'] = 0
    elif pd.isnull(row['more-vehicles']) :
        row['one-vehicle'] = 0
        row['two-vehicles'] = 0
        row['three-vehicles'] = 1
        row['more-vehicles'] = 0
    else :
        row['one-vehicle'] = 0
        row['two-vehicles'] = 0
        row['three-vehicles'] = 0
        row['more-vehicles'] = 1
        
df2.head()

## For each borough, find the distribution of each collision scale
df2['one-vehicle'] = pd.to_numeric(df2['one-vehicle'])
df2['two-vehicles'] = pd.to_numeric(df2['two-vehicles'])
df2['three-vehicles'] = pd.to_numeric(df2['three-vehicles'])
df2['more-vehicles'] = pd.to_numeric(df2['more-vehicles'])
collisions = pd.pivot_table(df2, index="borough", aggfunc='sum')
collisions

## Generate csv
collisions.to_csv('../../Results/Question1Part2.csv')

