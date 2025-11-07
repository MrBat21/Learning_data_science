import pandas as pd

coffee = pd.read_csv('C:/Users/Admin/OneDrive/Documents/Coding/Python/Learning_data_science/warmup_data/coffee.csv')

print(coffee.loc[4:7, ["Units Sold"]])
coffee.iloc#[Rows, Columns] #only using index