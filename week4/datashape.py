import pandas as pd
import seaborn as sns
df=sns.load_dataset("titanic")
"""
print("Data shape:",df.shape)
print(df.head())
print(df.info())
print(df.describe())
"""
df['age'].fillna(df['age'].median())
df['embarked'].fillna(df['embarked'].mode())
df.drop_duplicates(inplace=True)
df=pd.get_dummies(df,columns=['sex','class','embarked'],drop_first=True)
df['family_size']=df['sibsp']+df['parch']
print(df.head())