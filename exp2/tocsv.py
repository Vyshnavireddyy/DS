import pandas as pd
data=['10','20','30','40','50','60','70','80','90']
df=pd.DataFrame(data)
print(df)
print(df.to_csv('data.csv',index=False))
