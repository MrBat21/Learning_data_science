import pandas as pd

olympic = pd.read_excel('C:/Users/Admin/OneDrive/Documents/Coding/Python/Learning_data_science/warmup_data/olympics-data.xlsx')

#print(olympic.loc[olympic['height_cm'] > 215, ['name', 'height_cm']])
#print(olympic[olympic['height_cm']>215])

#print(olympic[olympic['name'].str.contains("Mike|Desire")])
