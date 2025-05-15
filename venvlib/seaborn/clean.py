import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")

print(df.head())
print(df.info())

df = df.drop(columns=["class", "adult_male", "who", "embark_town", "alive", "deck"])

df = df.dropna(subset=["age", "embarked"])

df["sex"] = df["sex"].map({"male" : 0, "female" : 1})

df["embarked"] = df["embarked"].map({"S" : 0, "C" : 1, "Q" : 2})

print(df.head())
print(df.info())