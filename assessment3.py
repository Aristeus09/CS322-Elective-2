import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#set font and canvas color
plt.rc("font", size=14)
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
#read data
data = pd.read_csv('candy-data.csv', header=0)
data = data.dropna()
#count values of the column to be read
data['winpercent'].value_counts()
prod_price_below = len(data[data['pricepercent'] < 0.5])
prod_price_above = len(data[data['pricepercent'] > 0.5 ])
data['saleable'] = np.where(data['pricepercent'] > 0.5, 'above 0.5', 'below 0.5')  # Label products as 'above' or 'below' based on pricepercent
price_below = prod_price_below / (prod_price_below + prod_price_above)
price_above = prod_price_above / (prod_price_below + prod_price_above)

print("Number of products below 0.5:", prod_price_below)
print(f"Percentage of products below 0.5: {price_below * 100:.2f}%")
print("Number of products above 0.5:", prod_price_above)
print(f"Percentage of products above 0.5: {price_above * 100:.2f}%")
print("Total Customers:", (prod_price_below + prod_price_above))
#graph the data
sns.countplot(x='saleable', data=data, palette='hls')
plt.title("Customer Loan Graph")
plt.show()