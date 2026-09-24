import pandas as pd
df=pd.DataFrame({
    'X':[10,20,30,40,50],
    'Y':[12,24,30,40,60]
})
cm=df.corr(method='pearson')
print("Pearson Correlation matrix:\n", cm)
