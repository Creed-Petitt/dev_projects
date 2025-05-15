import matplotlib.pyplot as plt
import pandas as pd
import mplcursors

df = pd.read_csv("../ninja_data.csv")


avg_age = df.groupby("Village")["Age"].mean()
spread = df.groupby("Village")["Name"].count()
trend = df.sort_values("Age").reset_index(drop=True)



fig, ax = plt.subplots(2, 2, figsize=(12, 5))

ax[0, 0].bar(avg_age.index, avg_age.values, width = 0.4, color ="orange")
ax[0, 0].set_title("Average Age of Each Village")
ax[0, 0].set_xlabel("Village")
ax[0, 0].set_ylabel("Average Age")
ax[0, 0].grid(True)
for i, val in enumerate(avg_age.values):
    ax[0, 0].text(i, val + 0.5, f"{val:.1f}", ha='center', va='bottom', fontsize=8)

ax[0, 1].pie(spread.values, labels=spread.index, autopct="%0.1f%%")
ax[0, 1].set_title("Village Distribution")

ax[1, 0].scatter(trend.index, trend["Age"], color = "red")
ax[1, 0].set_title("Scatter: Age vs Person Index")
ax[1, 0].set_xlabel("Person Index (sorted)")
ax[1, 0].set_ylabel("Age")
ax[1, 0].grid(True)

ax[1, 1].hist(df["Age"], bins=10, color="skyblue", edgecolor="black")
ax[1, 1].set_title("Age Distribution")
ax[1, 1].set_xlabel("Age")
ax[1, 1].set_ylabel("Count")
ax[1, 1].grid(True)

mplcursors.cursor(ax[0, 0].containers[0])  
mplcursors.cursor(ax[1, 0], hover=True)    
mplcursors.cursor(ax[1, 1], hover=True)


plt.tight_layout()
plt.show()
