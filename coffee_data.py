import pandas as pd
import numpy as np

coffee = pd.read_csv('C:/Users/Admin/OneDrive/Documents/Coding/Python/Learning_data_science/warmup_data/coffee.csv')

#Accessing Data with Pandas
#print(coffee.iat[0,0])
#print(coffee.iloc[0,0])
#print(coffee.sort_values(["Units Sold"], ascending=False))

#Use row to access each data
#for index, row in coffee.iterrows():
    #print(index)

coffee['price'] = np.where(coffee['Coffee Type']=='Espresso', 3.99, 5.99)

#coffee.drop(columns=['price'], inplace=True)
print(coffee)
