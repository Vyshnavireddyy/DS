import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
iris = load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
df['species']=iris.target
plt.figure(figsize=(6,6))
sns.histplot(df['sepal length (cm)'],bins=20,kde=True)
plt.title("Histogram of sepal length (cm)")
plt.show()
plt.figure(figsize=(6,6))
sns.boxplot(x=df['sepal length (cm)'])
plt.title("Boxplot of sepal length (cm)")
plt.show()
species_count=df['species'].value_counts()
plt.figure(figsize=(6,6))
sns.pie(species_count,labels=iris.target_names,autopct='%1.1f%%')
plt.title("Distribution of species")
plt.show()