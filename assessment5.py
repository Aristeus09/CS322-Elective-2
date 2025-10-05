import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc("font", size=14)
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
data = pd.read_csv('candy-data.csv', header=0)
data = data.dropna()

#set the value of x and y from 2 columns
pd.crosstab(data.peanutyalmondy, data.nougat).plot(kind='bar')

nougat_pct_1 = data['nougat'].mean() * 100
nougat_pct_0 = 100 - nougat_pct_1

peanut_pct_1 = data['peanutyalmondy'].mean() * 100
peanut_pct_0 = 100 - peanut_pct_1

print(f"Percentage of products with nougat: {nougat_pct_1:.2f}%")
print(f"Percentage of products without nougat: {nougat_pct_0:.2f}%")
print(f"Percentage of products with peanut almond: {peanut_pct_1:.2f}%")
print(f"Percentage of products without peanut almond: {peanut_pct_0:.2f}%")
plt.title("Product Peanut Almond and Nougat")
plt.xlabel("Peanut Almond")
plt.ylabel("Nougat")
plt.show()