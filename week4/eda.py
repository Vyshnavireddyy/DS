import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df=pd.read_csv("student.csv")
sns.histplot(df['Attendance'],bins=15,kde=True)
plt.title("Attendance")
plt.show()