"""
Created on Sun Feb 21 14:40:13 2016

@author: moses
"""

import pandas as pd

dfBatting = pd.read_csv('data/baseball-csvs/Batting.csv')

dfBatting['BA'] = dfBatting['H'] / dfBatting['AB']

dfBatting['OBP'] = (dfBatting['H'] + dfBatting['BB'] + dfBatting['HBP'])\
    / (dfBatting['AB'] + dfBatting['BB'] + dfBatting['HBP'] + dfBatting['SF'])
    
dfBatting['SLG'] = (dfBatting['H'] + dfBatting['2B'] + 2*dfBatting['3B'] +\
    3*dfBatting['HR']) / dfBatting['AB']

dfSals = pd.read_csv('data/baseball-csvs/Salaries.csv')

dfBatting = dfBatting[dfBatting.yearID >= 1985]

mergeddf = pd.merge(dfBatting, dfSals, on=['playerID','yearID'])
mergeddf.drop(['G_old', 'teamID_y', 'lgID_y'], axis=1, inplace=True)
mergeddf.rename(columns = {'teamID_x':'teamID', 'lgID_x':'lgID'}, inplace=True)

oak2001 = mergeddf[(mergeddf['teamID'] == 'OAK') & (mergeddf['yearID'] == 2001)]

my_mask = oak2001['playerID'].isin(['giambja01', 'damonjo01', 'isrinja01', 'saenzol01']) 

lostboysdf = oak2001[my_mask][['playerID', 'teamID', 'AB', 'HR', 'SLG', 'OBP', 'salary']]

avgOBP = lostboysdf['OBP'].mean()
totAB = lostboysdf['AB'].sum()


all2001 = mergeddf[mergeddf.yearID == 2001][['playerID', 'teamID', 'AB', 'HR', 'OBP', 'SLG', 'salary']]
all2001 = all2001[all2001['AB'] >= 300]
all2001 = all2001[all2001['salary'] <= 5000000]

batters = all2001.sort_values('AB', ascending=False)
onbasers = all2001.sort_values('OBP', ascending = False)
budgeters = all2001.sort_values('salary', ascending = False)
