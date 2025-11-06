import pandas as pd

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=["A", "B", "C"], index =["x", "y", "z"])

head = df.head
info = df.info()
describe = df.describe()
shape = df.shape
numuniqe = df.nunique()
print(numuniqe)