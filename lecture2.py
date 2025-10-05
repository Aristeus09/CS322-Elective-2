import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#set font and canvas color
plt.rc("font", size=14)
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
#read_data
data = pd.read_csv('banking.csv', header=0)
data = data.dropna()
#count values of the column to be read
data['y'].value_counts()
count_no_sub = len(data[data['y'] == 0])
count_sub = len(data[data['y'] == 1])
pct_no_sub = count_no_sub / (count_no_sub + count_sub) #total subscriptions
pct_sub = count_sub / (count_no_sub + count_sub) #total subscriptions
print("Percentage of customers without subscriptions:{:.2f}"
      .format(pct_no_sub * 100))
print("Percentage of customers with subscriptions:{:.2f}"
      .format(pct_sub * 100))
#graph the data
sns.countplot(x='y', data=data, palette='hls')
plt.title("Customer Subscription Graph")
plt.show()

