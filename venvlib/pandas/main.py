import pandas as pd

df = pd.read_csv("ninja_data.csv")
print('\n' * 3)
print("Ninja Table:", '\n')
print(df)
print('\n' * 3)

df.loc[len(df)] = {
                    "Name" : "Orochimaru",
                    "Village" : "Hidden Sound",
                    "Age" : None,
                    "Rank" : 5
                    }

print("Adding Orochimaru...", '\n')
print(df)
print('\n' * 3)

print(df.isnull())       
print(df.isnull().sum())

print('\n' * 3)

df["Age"] = df["Age"].fillna(0)  
print(df)
