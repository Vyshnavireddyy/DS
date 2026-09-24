import pandas as pd
df=pd.DataFrame({
    'TOC':[10,20,30,40,50],
    'CD':[12,24,30,40,60],
    'DS':[23,45,29,45,10]
})
cm=df.corr(method='pearson')
print("Pearson Correlation matrix:\n", cm)
d=pd.read_csv("Iris.csv")
print(d.corr(method='pearson',numeric_only=True))
