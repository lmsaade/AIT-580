import pandas as pd
df = pd.read_csv('storm_data_2020s.csv')

# Add record number column to dataset
df['Record Number'] = df.index

# What state had the largest number of instances
print(df.STATE.mode())
print(df['STATE'].value_counts())
# Texas had 27,195 instances of weather events

# What are the top 3 extreme event types for that state?
dftexas = df[df['STATE'] ==  'TEXAS']
print(dftexas['EVENT_TYPE'].value_counts())
# Texas' top 3 weather events are hail (6414), drought (4629), and thunderstorm wind (4593)

#When do they typically occur?
dftop3 = dftexas[dftexas['EVENT_TYPE'].isin(['Hail', 'Drought', 'Thunderstorm Wind'])]
print(dftop3['MONTH_NAME'].value_counts())
#Texas' top 3 weather events typically occur in May (4218), April (2821), and June (2074)

hist = dftexas.hist(column='YEAR', bins = 10)
print(hist)
