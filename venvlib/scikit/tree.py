import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

df = df.drop(columns=["adult_male", "alive", "embark_town", "deck", "class", "who"])
df = df.dropna(subset=["age", "embarked"])

df["sex"] = df["sex"].map({"male": 0, "female" : 1})
df["embarked"] = df["embarked"].map({"S": 0, "C" : 1, "Q" : 2})

X = df.drop(columns="survived")
y = df["survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(max_depth=5, random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)


print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

plt.figure(figsize=(20,10))
plot_tree(model, feature_names=X.columns, class_names=["Died", "Survived"], filled=True)
plt.title("Decision Tree Visualization")
plt.show()



