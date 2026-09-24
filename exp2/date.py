import pandas as pd
df=pd.DataFrame({
    'date': ['2006-11-7','2006/11/07','nov 7 2006','2006.11.07']
})
print("Original DataFrame \n",df)
df['date']=pd.to_datetime(df['date'],errors='coerce').dt.strftime('%Y-%m-%d')
print(df)