import pandas as pd
from scipy.stats import spearmanr
df=pd.DataFrame({
    'X':[10,20,30,40,50],
    'Y':[12,24,30,40,60]
})
cv,pv=spearmanr(df['X'],df['Y'])
print(f"Spearman Correlation Coef:{cv}")
print(f"P-value:{pv}")

