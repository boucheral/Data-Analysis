###########################################################################################################################
## Question 1 - Part 1                                                                                                   ##
## - Use vehicle_collision dataset                                                                                       ##
## - For each month in 2016, find out the percentage of collisions in Manhattan out of the year's total accidents in NYC ##
## - Display a few rows of the output using df.head()                                                                    ##
## - Generate a CSV output with 4 columns ('Month', 'Manhattan', 'NYC', 'Percentage')                                    ##
###########################################################################################################################

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import datetime

## Use vehicle_collision dataset
df = pd.read_csv('../../Data/vehicle_collisions.csv', parse_dates=['DATE'])
df.head()

def countM(x):
    count = 0
    for n in x :
        if n in ["MANHATTAN"] :
            
            count = count + 1
            
    return count

def percent(x):
    count = 0
    total = 0
    for n in x :
        total = total + 1
        if n in ["MANHATTAN"] :
            count = count + 1
            
    return count/total

df16 = df[(datetime.date(2016,1,1) <= df['DATE']) & (df["DATE"] < datetime.date(2017,1,1))]
df16.head()

months = {1:"Jan", 2:"Feb", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"Aug", 9:"Sept", 10:"Oct",11:"Nov", 12:"Dec"}

def month(x) :
    return months[x.month]


df16["Month"] = df16.apply(lambda row : month(row["DATE"]), axis=1)
df16.head()


result = df16.groupby("Month").agg({"BOROUGH": {"Manhattan" : lambda x : countM(x), 
                                    "NYC" : "count", 
                                    "Percent" : lambda x : percent(x)}})
result


## Generate a CSV output with 4 columns ('Month', 'Manhattan', 'NYC', 'Percentage')

result.to_csv("../../Results/Question1Part1.csv")

