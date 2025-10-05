import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc("font", size=14)
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
data = pd.read_csv('candy-data.csv', header=0)
data = data.dropna()

#set the value of x and y from 2 columns
pd.crosstab(data.crispedricewafer, data.caramel).plot(kind='bar')

caramel_pct_1 = data['caramel'].mean() * 100
caramel_pct_0 = 100 - caramel_pct_1

crisped_pct_1 = data['crispedricewafer'].mean() * 100
crisped_pct_0 = 100 - crisped_pct_1

print(f"Percentage of products with caramel: {caramel_pct_1:.2f}%")
print(f"Percentage of products without caramel: {caramel_pct_0:.2f}%")
print(f"Percentage of products with crisped rice wafer: {crisped_pct_1:.2f}%")
print(f"Percentage of products without crisped rice wafer: {crisped_pct_0:.2f}%")
plt.title("Product Crisped Rice Wafer and Caramel")
plt.xlabel("Crisped Rice Wafer")
plt.ylabel("Caramel")
plt.show()