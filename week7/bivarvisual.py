import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
iris = load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
df['species']=iris.target
plt.figure(figsize=(10,10))
sns.scatterplot(x=df['sepal length (cm)'],y=df['sepal width (cm)'],hue=df['species'])
plt.title("sepal length vs sepal width")
plt.show()
#linechart
plt.figure(figsize=(10,10))
plt.plot(df['sepal length (cm)'])
plt.title("line chart of sepal length")
plt.xlabel("sample index")
plt.ylabel("sepal length")
plt.show()
#bargraph
plt.figure(figsize=(10,10))
sns.boxplot(x=df['species'],y=df['sepal length (cm)'])
plt.title("Bar chart : mean sepal length by species")
plt.xticks([0,1,2],iris.target_names)
plt.show()