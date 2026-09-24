import pandas as pd
import numpy as np
df=pd.DataFrame({'Age':[25,30,np.nan,40,35],
'Department':['hr','finance','Finance',np.nan,'IT']})
print("Original dataset")
print(df)
df_bfill=df.copy()
df_bfill.bfill(inplace=True)
print(df_bfill)