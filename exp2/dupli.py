import pandas as pd
import numpy as np
df=pd.DataFrame({
    'id':[1,2,3,4,4],
    'name':['alice','bob','charlie','charlie','charlie'],
    'age':[10,20,30,40,40]
})
print("Original dataset")
print(df)
print("After removal")
df_s=df.drop_duplicates(subset=['age'])
#df_ex=df.drop_duplicates()
print(df_s)
df_n=df.drop_duplicates(subset=['name'])
print(df_n)
