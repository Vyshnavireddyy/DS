import pandas as pd
import seaborn as sns
df=pd.read_csv("student.csv")
print(df.drop_duplicates())