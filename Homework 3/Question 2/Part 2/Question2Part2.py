###########################################################################################################################
## Question 2 - Part 2                                                                                                   ##
## - Use employee_compensation dataset                                                                                   ##
## - Filter data by calendar year and find average salary for every employee                                             ##
## - Find the people who's overtime salary is greater than 5% of salaries                                                ##
## - For each 'Job Family' these people are associated with, calculate the percentage of total benefits with respect to  ##
##     total compensation.                                                                                               ##
## - display with df.head()                                                                                              ##
## - Generate a CSV output                                                                                               ##
###########################################################################################################################

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import datetime

## Use employee_compensation dataset
df = pd.read_csv('../../Data/employee_compensation.csv')
df.head()

## Filter data by calendar year and find average salary for every employee
yeardf = df[df['Year Type'] == 'Calendar']
yeardf

yeardf.groupby('Employee Identifier').aggregate("mean")
yeardf.head()

## Find the people who's overtime salary is greater than 5% of salaries
newdf = yeardf[yeardf['Overtime'] / yeardf['Salaries'] >= 0.05]
newdf.head()

## For each 'Job Family' these people are associated with, 
## calculate the percentage of total benefits with respect to total compensation. 

newdf['Percent Tot Benefits'] = (newdf['Total Benefits'] / newdf['Total Compensation']).multiply(100)
PTBdf = newdf[['Job Family','Total Benefits', 'Total Compensation', 'Percent Tot Benefits']].groupby('Job Family').aggregate("mean")
PTBdf.head()

##Generate a CSV output
PTBdf.to_csv("Question2Part2.csv")

