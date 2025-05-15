import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors


np.random.seed(32)

names = ["Naruto Uzumaki", "Sasuke Uchiha", "Sakura Haruno", "Kakashi Hatake",
    "Shikamaru Nara", "Hinata Hyuga", "Neji Hyuga", "Rock Lee",
    "Tenten", "Gaara", "Kankuro", "Temari",
    "Killer Bee", "Darui", "Chojuro", "Mei Terumi",
    "Onoki", "Kurotsuchi", "Hanzo", "Konan"
]

ages = np.random.randint(15, 40, size=20)


village_choices = ["Hidden Leaf", "Hidden Sand", "Hidden Mist", "Hidden Cloud", "Hidden Rock"]

villages = np.random.choice(village_choices, size=20)

chakra = np.random.uniform(0, 100, size=20)

graduated = np.random.choice([True, False], size=20)

data = {
        "Name": names,
        "Age" : ages, 
        "Village" : villages,
        "Chakra" : chakra,
        "Graduated" : graduated
}

df = pd.DataFrame(data)



avg_age = df.groupby("Village")["Age"].mean()
print(avg_age)

fig, ax = plt.subplots(2, 2, figsize=(12, 6))


ax[0,0].bar(avg_age.index, avg_age, width=0.5)
ax[0,0].set_title("Average Age per Village")
ax[0,0].set_xlabel("Village")
ax[0,0].set_ylabel("Average Age")
ax[0,0].grid(True)


grad_count = df["Graduated"].value_counts()
ax[0,1].pie(grad_count, 
            labels=grad_count.index, 
            autopct = "%1.0f%%",
            colors=["skyblue", "lightgray"],
            startangle=90)

ax[0,1].set_title("Graduation Status")




ax[1, 0].hist(df["Chakra"], bins=10, color="purple", edgecolor="black")
ax[1,0].set_title("Chakra Level Distribution")
ax[1,0].set_xlabel("Chakra Level")
ax[1,0].set_ylabel("Number of Ninja")
ax[0, 1].grid(True)

ax[1, 1].scatter(df["Age"], df["Chakra"], color="teal", marker="o")
ax[1, 1].set_title("Chakra vs Age")
ax[1, 1].set_xlabel("Age")
ax[1, 1].set_ylabel("Chakra Level")
colors = df["Graduated"].map({True: "green", False: "red"})
ax[1, 1].scatter(df["Age"], df["Chakra"], color=colors, marker="o")
ax[1, 1].grid(True)




mplcursors.cursor(ax[0, 0].containers[0])  
mplcursors.cursor(ax[0, 1], hover=True)    
mplcursors.cursor(ax[1, 1], hover=True) 
mplcursors.cursor(ax[1, 0], hover=True)

fig.savefig("ninja_dashboard.png", dpi=300)


plt.tight_layout()
plt.show()