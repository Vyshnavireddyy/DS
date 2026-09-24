import pandas as pd
df=pd.read_json('sample1.json')
print(df)
dup_df=pd.concat([df,df])
print(dup_df.shape)
dup_dp=dup_df.drop_duplicates()
print(dup_dp)
print(df.describe())
