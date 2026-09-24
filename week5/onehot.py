from sklearn.preprocessing import StandardScaler
import pandas as pd
df=pd.DataFrame({'Color': ['Red', 'Orange', 'Yellow','Green','Red']})
one_hot=pd.get_dummies(df,columns=['Color'])
print("\nOne Hot Encoding : ")
print(one_hot)