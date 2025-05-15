import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")

sns.barplot(x = "species", y="body_mass_g", data=df)
plt.title("Average Body Mass by Species")
plt.ylabel("Body Mass (g)")
plt.show()

sns.histplot(data=df, x="flipper_length_mm", bins=20, kde=True)
plt.title("Flipper Length Distribution")
plt.show()

sns.scatterplot(data=df, x = "bill_length_mm", y = "bill_depth_mm", hue = "species")
plt.title("Bill Dimensions by Species")
plt.show()

sns.boxplot(data=df, x="species", y="body_mass_g")
plt.title("Body Mass Spread by Species")
plt.show()

sns.violinplot(data=df, x="species", y="body_mass_g")
plt.title("Body Mass Distribution by Species")
plt.show()
