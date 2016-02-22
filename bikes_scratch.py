"""
Created on Sun Feb 21 19:24:18 2016

@author: moses
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

dfbikes = pd.read_csv('data/bay_area_bikeshare/201402_trip_data_v2.csv', parse_dates=['start_date'])
dfstations = pd.read_csv('data/bay_area_bikeshare/201402_station_data_v2.csv',  parse_dates=['installation'])
dfweather = pd.read_csv('data/bay_area_bikeshare/201402_weather_data_v2.csv', parse_dates=['date'])
dfbikewithstations = pd.merge(dfbikes, dfstations, left_on='start_station', right_on='station_id')

dfDuration = dfbikes['duration']

dfDuration.describe()
dfDur = dfDuration[dfDuration <= 3000]
dfDur.hist(bins=100)

dfDates = dfbikes['start_date']
dfHour = dfDates.map(lambda x: x.hour)
dfHourMinute = dfDates.map(lambda x: int(x.strftime('%H%M')))

dfHour.hist(bins=24)

plt.scatter(dfDuration, dfHourMinute)

dfWeekdaydata = dfbikes[dfbikes['start_date'].map(lambda x: x.weekday() < 5)]
dfWeekenddata = dfbikes[dfbikes['start_date'].map(lambda x: x.weekday() >= 5)]

dfWeekdaydata['duration'][dfWeekdaydata['duration'] < 3000].hist(bins=100)
dfWeekenddata['duration'][dfWeekenddata['duration'] < 3000].hist(bins=100)

dfWeekdayhour = dfWeekdaydata['start_date'].map(lambda x: x.hour)
dfWeekendhour = dfWeekenddata['start_date'].map(lambda x: x.hour)

dfWeekdayhour.hist(bins=24)
dfWeekendhour.hist(bins=24)


dfbikes.start_station.unique()
dfbikewithstations.landmark.unique()

dfbikewithstations['hour_min'] = dfbikewithstations['start_date'].map(lambda x: x.time())
dfbikewithstations['hour'] = dfbikewithstations['start_date'].map(lambda x: x.hour)

pd.DataFrame.plot.scatter()

pshoo = dfbikewithstations[dfbikewithstations['hour'] == 9]

dfbikewithstations['weekday'] = dfbikewithstations['start_date'].map(lambda x: x.weekday())

dfbikewithstations.plot.scatter(x='hour_min', y='duration', c='isround', cmap='coolwarm', xlim=(-1, 2400), ylim=(0,2000))

#dfbs.plot.scatter(x = dfbs[dfbs.weekday == 0].duration, \
#y = dfbs[dfbs.weekday == 4].duration

dfbikewithstations['isround'] = dfbikewithstations['start_terminal'] == dfbikewithstations['end_terminal']

dfbs = dfbikewithstations

gstation = dfbs.groupby(['start_station','weekday'])
grouped_med_dur = gstation.duration.median()

zipdict = {'San Francisco':94107, 'Redwood City':94063, 'Palo Alto':94301, 'Mountain View':94041, 'San Jose':95113}
dfbs['zip'] = dfbs['landmark'].map(zipdict)
dfall = pd.merge(dfbs, dfweather, left_on=['zip','start_date'], right_on=['zip','date'])
