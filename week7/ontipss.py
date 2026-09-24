import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from week5.pca import tips

tips_df=sns.load_dataset("tips")
df=pd.DataFrame(tips.data,columns=tips.feature_names)
df['species']=tips.target
plt.figure(figsize=(10,10))
sns.heatmap(df.iloc[:,:4].corr(),annot=True,cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
#bubblechart
plt.figure(figsize=(10,10))
plt.scatter(df['sex'],df['size'],s=df['day']*20,alpha=0.5,c=df['species'])
plt.title("Bubble chart")
plt.xlabel("sex")
plt.ylabel("size")
plt.show()
#pairplot
plt.figure(figsize=(10,10))
sns.pairplot(df.iloc[:,:4])
plt.suptitle("Pair plot of tips features",y=1.02)
plt.show()
#advanced plot violinplot
plt.figure(figsize=(10,10))
sns.violinplot(x=df['species'],y=df['sex'])
plt.title("Violin plot : sepal length")
plt.xticks([0,1,2],tips.target_names)
plt.show()
