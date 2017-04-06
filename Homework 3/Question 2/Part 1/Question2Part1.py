=###########################################################################################################################
## Question 2 - Part 1                                                                                                   ##
## - Use employee_compensation dataset                                                                                   ##
## - Find the highest paid dept in each organization group by caluclating the mean of total compensation for every dept. ##
## - Output should contain the organization group and the departments in each group with total comp from high to low     ##
## - Display a few rows of the output using df.head()                                                                    ##
## - Generate a CSV output                                                                                               ##
###########################################################################################################################

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import datetime

## Use employee_compensation dataset
df = pd.read_csv('../../Data/employee_compensation.csv')
df.head()

df['Organization Group'].fillna('Missing')
df['Department'].fillna('Missing')
df['Salaries'].fillna(0)

result = df[['Organization Group', 'Department', 'Total Compensation']].pivot_table(index=['Organization Group', 'Department'], aggfunc='mean').sort_values('Total Compensation', ascending=False)
result.head()

##to csv
result.to_csv('../../Results/Question2Part1.csv')

