import seaborn as sns
titanic=sns.load_dataset("titanic")
print(titanic.head())
#tips and titanic and iris
ob="Classified survey (Yes/No)"
sc="Accuracy > 80%"
c="Limited features , missing values, imbalanced classes"
print("Objective : ",ob)
print("Accuracy : ",sc)
print("Constraints : ",c)