import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from week5.pca import tips

tips_df=sns.load_dataset("tips")
df=pd.DataFrame(tips.data,columns=tips.feature_names)
df['species']=tips.target
plt.figure(figsize=(6,6))
sns.histplot(df['sex'],bins=20,kde=True)
plt.title("Histogram of sex")
plt.show()
plt.figure(figsize=(6,6))
sns.boxplot(x=df['sex'])
plt.title("Boxplot of sex")
plt.show()
species_count=df['species'].value_counts()
plt.figure(figsize=(6,6))
sns.pie(species_count,labels=tips.target_names,autopct='%1.1f%%')
plt.title("Distribution of species")
plt.show()