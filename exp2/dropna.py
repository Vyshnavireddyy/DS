import pandas as pd
import numpy as np
df=pd.DataFrame({'Age':[25,30,np.nan,40,35],
'Department':['hr','finance','Finance',np.nan,'IT']})
print("Original dataset")
print(df)
df_drop=df.dropna()
print("After dropping rows :\n",df_drop)
df_dropcol=df.dropna(axis=1)
print("After dropping columns :\n",df_dropcol)