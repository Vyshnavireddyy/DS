import pandas as pd
from sklearn.preprocessing import MinMaxScaler
data = pd.DataFrame({
    'A':[10,20,30,40,50],
    'B':[5,15,25,35,45]
})
print(data)
scalar=MinMaxScaler()
normalized=scalar.fit_transform(data)
normalized_df=pd.DataFrame(normalized,columns=data.columns)
print("Normalized Data (Min-Max Scaler): ")
print(normalized_df)
