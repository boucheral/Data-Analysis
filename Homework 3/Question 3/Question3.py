###########################################################################################################################
## Question 3                                                                                                            ##
## - Use cricket_matches dataset                                                                                         ##
## - Calculate the average score for each team which hosted and won the game                                             ##
## - display with df.head()                                                                                              ##
## - Generate a CSV output                                                                                               ##
###########################################################################################################################

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import datetime

## Use cricket_matches dataset
df = pd.read_csv('../Data/cricket_matches.csv')
df.head()

## filter rows where the team that won was the home team
df = df[df['home'] == df['winner']]
df.head()

def winningScore(x) :
    if x['winner'] == x['innings1'] :
        return x['innings1_runs']
    elif x['winner'] == x['innings2']:
        return x['innings2_runs']
    else :
        return 0

## I don't know anything about cricket but I tried to figure out how the scoring worked.
## As best I can tell it's the number of runs in the inning that they played. If that's incorrect please take mercy on me. 
df["winning_score"] = df.apply(lambda row : winningScore(row), axis=1)
df.head()

## Averages of winning scores of winning homegames
averages = pd.pivot_table(df[['home', 'winning_score']], index='home', aggfunc='mean')
## Display with df.head()
averages.head()

## Save to csv
averages.to_csv("../Results/Question3.csv")

