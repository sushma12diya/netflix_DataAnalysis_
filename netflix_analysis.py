import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titles.csv")

print(df.head())

type_count = df["type"].value_counts()

type_count.plot(kind="bar")

plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")

plt.show()