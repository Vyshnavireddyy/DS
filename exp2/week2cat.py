import pandas as pd
import numpy as np
df=pd.DataFrame({'Age':[25,30,np.nan,40,35],
'Department':['hr','finance','Finance',np.nan,'IT']})
print("Original dataset")
print(df)
df_fillna=df.fillna(df.iloc[0])
print(df_fillna)