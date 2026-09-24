import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
tips=sns.load_dataset("tips")
numeric_cols=tips.select_dtypes(include=['int64','float64'])
scaler=StandardScaler()
scaled_data=scaler.fit_transform(numeric_cols)
pca=PCA(n_components=2)
pca_result=pca.fit_transform(scaled_data)
pca_df=pd.DataFrame(data=pca_result,columns=['PC1','PC2'])
print("Explained variance ratio:",pca.explained_variance_ratio_)
print("\nPCA Result(First 5 rows):")
print(pca_df.head())
plt.scatter(pca_df['PC1'],pca_df['PC2'],alpha=0.5,color='pink')
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA projection of tips dataset")
plt.show()