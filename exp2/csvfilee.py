import pandas as pd
df=pd.read_csv('../week3/Iris.csv')
print(df.head(2))
print(df.tail(2))
print(df)
print(df.info(2))
print(df.shape)
#df=pd.read_csv('iris.csv')