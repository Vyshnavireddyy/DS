import pandas as pd
import numpy as np
df=pd.DataFrame({
    'name':['Alice','Bob','Charlie','Bunny','sarah','Raya9']})
df['name_lower']=df['name'].str.lower()
df['name_upper']=df['name'].str.upper()
print(df)