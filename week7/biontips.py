import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from week7.ontips import tips_df

plt.figure(figsize=(6,4))
sns.histplot(tips_df['total_bill'], bins=20, kde=True)
plt.title("Histogram of Total Bill")
plt.xlabel("Total Bill ($)")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x='day',y='tip',data=tips_df)
plt.title("Boxplot of Tip Amount by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Tip Amount ($)")
plt.show()

day_counts=tips_df['day'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(day_counts,labels=day_counts.index,autopct='%1.1f%%')
plt.title("Pie Chart of Diners by Day")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x='total_bill',y='tip',hue='sex',data=tips_df)
plt.title("Scatterplot of Total Bill vs Tip by Sex")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip Amount ($)")
plt.show()

plt.figure(figsize=(6,4))
sns.pointplot(x='day', y='total_bill', data=tips_df, errorbar=None)
plt.title("Average Total Bill by Day of the Week")
plt.xlabel("Day of the Week")
plt.ylabel("Average Total Bill ($)")
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x='smoker',y='tip',data=tips_df)
plt.title("Bar Chart: Mean Tip Amount by Smoker Status")
plt.xlabel("Smoker (Yes/No)")
plt.ylabel("Mean Tip Amount ($)")
plt.show()


plt.figure(figsize=(8,6))
sns.heatmap(tips_df[['total_bill', 'tip', 'size']].corr(),annot=True,cmap='coolwarm')
plt.title("Correlation Heatmap of Numerical Features")
plt.show()

plt.figure(figsize=(6,4))

plt.scatter(tips_df['total_bill'], tips_df['tip'], s=tips_df['size']*20, alpha=0.5, c=pd.factorize(tips_df['sex'])[0], cmap='viridis')
plt.title("Bubble Chart: Total Bill vs Tip (Bubble Size by Party Size, Color by Sex)")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip Amount ($)")
plt.colorbar(label='Sex (0=Female, 1=Male)')
plt.show()

sns.pairplot(tips_df[['total_bill', 'tip', 'size', 'sex']], hue='sex')
plt.suptitle("Pair Plot of Tips Numerical Features", y=1.02)
plt.show()

plt.figure(figsize=(6,4))
sns.violinplot(x='time',y='total_bill',data=tips_df)
plt.title("Violin Plot of Total Bill by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Total Bill ($)")
plt.show()