###########################################################################################################################
## Question 4                                                                                                            ##
## - Use movie_awards dataset                                                                                            ##
## - Create a win and nomination column as well as win and nomination columns for each of the different award categories ##
## - Display a few rows of the output using df.head()                                                                    ##
## - Generate a CSV output                                                                                               ##
###########################################################################################################################

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

## Use movie_awards dataset
df = pd.read_csv('../Data/movies_awards.csv')
df.head()

def isNumber(x) :
    try: 
        int(x)
        return True
    except ValueError:
        return False

def getNumber(x):
    for n in x.split(' ') :
        if isNumber(n) :
            return int(n)
    return 0
    
def getAwardValues(row) :
    x = row['Awards']
    ##  0    1    2      3      4     5      6     7    8      9
    ##[Win, Nom, OWin, ONom, GGWin, GGNom, BWin, BNom, PEWin, PENom]
    results = [0,0,0,0,0,0,0,0,0,0]
    if x is np.nan :
        return results
    
    sent = x.split('.')
    for x in sent :
        if 'oscar' in x.lower() :
            if "nominated" in x.lower() :
                results[3] = getNumber(x)
            if 'won' in x.lower() :
                results[2] = getNumber(x)
            
        if 'bafta' in x.lower() :
            if "nominated" in x.lower() :
                results[7] = getNumber(x)
            if 'won' in x.lower() :
                results[6] = getNumber(x)
            
        if 'globe' in x.lower() :
            if "nominated" in x.lower() :
                results[5] = getNumber(x)
            if 'won' in x.lower() :
                results[4] = getNumber(x)
            
        if 'emmy' in x.lower() :
            if "nominated" in x.lower() :
                results[9] = getNumber(x)
            if 'won' in x.lower() :
                results[8] = getNumber(x)
        
        if '&' in x :
            temp = x.split('&')
            for t in temp :
                if 'win' in t.lower() :
                    results[0] = getNumber(t)
                elif 'nomination' in t.lower() :
                    results[1] = getNumber(t)
        
        if not any(word in x.lower() for word in ['oscar', 'emmy', 'bafta', 'globe', '&']) :
            if 'win' in x.lower() :
                results[0] = getNumber(x)
            elif 'nomination' in x.lower() :
                results[1] = getNumber(x)
                
    return results

awards = df.apply(lambda row: pd.Series(getAwardValues(row)), axis=1)
awards.columns = ['Wins', 'Nominations', 'Oscar Wins', 'Oscar Nominations', 'Golden Globe Wins', 'Golden Globe Nominations',
                  'BAFTA Wins', 'BAFTA Nominations', 'Primetime Emmy Wins', 'Primetime Emmy Nominations']
awards.head()

newdf = df.join(awards)
newdf.head()

## Save to csv
newdf.to_csv("../Results/Question4.csv")

