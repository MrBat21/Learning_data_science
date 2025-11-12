import pandas as pd

bios = pd.read_excel('C:/Users/Admin/OneDrive/Documents/Coding/Python/Learning_data_science/warmup_data/olympics-data.xlsx')
bios_new = bios.copy()

bios_new['first_name'] = bios_new['name'].str.split(' ').str[0]
#print(bios_new)

bios_new['born_date'] = pd.to_datetime(bios_new['born_date'])
#print(bios_new.info())

bios_new['born_year'] = bios_new['born_date'].dt.year
print(bios_new)