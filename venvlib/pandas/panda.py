import pandas as pd 

data = {
        "Name" : ["Nagato", "Jiraiya", "Hidan", "Killer Bee"],
        "Age" : [29, 54, 345, 25],
        "Affiliation": ["Hidden Rain", "Hidden Leaf", "Akatsuki", "Hidden Cloud"],
        "Rank" : [2, 1, 4, 3]
}

df = pd.DataFrame(data)

print('\n' * 3)

print("Table:", '\n')

print(df)

print('\n' * 3)

print("Adding Orochimaru", '\n')

df.loc[len(df)] = {
                   "Name": "Orochimaru" ,
                   "Age" : 67 ,
                   "Affiliation" : "Hidden Sound", 
                   "Rank": 3

}

df.loc[2, "Rank"] = 5
df.loc[3, "Rank"] = 4


print('\n' * 3)

print(df)

print('\n' * 3)

print("Dropping Hidan", '\n')

df = df.drop(2)

print('\n' * 3)

print(df)

print('\n' * 3)


print("Sorting Ninja by Age", '\n')

df = df.sort_values("Age", ascending=False)

print('\n' * 3)

print(df)

df = df[df["Age"] > 40]

print('\n' * 3)

print(df)

df = df.reset_index(drop=True)

df.to_csv("ninja_data_updated.csv")