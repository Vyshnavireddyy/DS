import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
iris = load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
df['species']=iris.target
plt.figure(figsize=(10,10))
sns.heatmap(df.iloc[:,:4].corr(),annot=True,cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
#bubblechart
plt.figure(figsize=(10,10))
plt.scatter(df['sepal length (cm)'],df['sepal width (cm)'],s=df['petal length (cm)']*20,alpha=0.5,c=df['species'])
plt.title("Bubble chart")
plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")
plt.show()
#pairplot
plt.figure(figsize=(10,10))
sns.pairplot(df.iloc[:,:4])
plt.suptitle("Pair plot of iris features",y=1.02)
plt.show()
#advanced plot violinplot
plt.figure(figsize=(10,10))
sns.violinplot(x=df['species'],y=df['sepal length (cm)'])
plt.title("Violin plot : sepal length")
plt.xticks([0,1,2],iris.target_names)
plt.show()
