import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

df = df.drop(columns=["class", "adult_male", "who", "embark_town", "alive", "deck"])

df = df.dropna(subset=["age", "embarked"])

df["sex"] = df["sex"].map({"male" : 0, "female" : 1})

df["embarked"] = df["embarked"].map({"S" : 0, "C" : 1, "Q" : 2})

X = df.drop(columns="survived")
y = df["survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#print("X_train:", X_train.shape)
#print("X_test:", X_test.shape)
#print("y_train:", y_train.shape)
#print("y_test:", y_test.shape)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
#print("Accuracy:", accuracy)
#print("Feature names:", X.columns.tolist())
#print("Coefficients:", model.coef_)
#print("Intercept:", model.intercept_)

probs = model.predict_proba(X_test)
survival_probs = probs[:, 1]

custom_preds = (survival_probs > 0.75).astype(int)

custom_accuracy = accuracy_score(y_test, custom_preds)

#print("Custom Accuracy:", custom_accuracy)
precision = precision_score(y_test, custom_preds)
recall = recall_score(y_test, custom_preds)
#print("Precision:", precision)
#print("Recall:", recall)

#print('\n' * 2)

#print("Original Accuracy:", accuracy)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
#print("Precision:", precision)
#print("Recall:", recall)

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Died", "Survived"])
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix (Default Threshold)")
plt.show()


cm2 = confusion_matrix(y_test, custom_preds)
disp2 = ConfusionMatrixDisplay(confusion_matrix=cm2, display_labels=["Died", "Survived"])
disp2.plot(cmap=plt.cm.Greens)
plt.title
plt.title("Confusion Matrix (Custom Threshold)")
plt.show()