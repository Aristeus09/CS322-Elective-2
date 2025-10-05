import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc("font", size=14)
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
data = pd.read_csv('banking.csv', header=0)
data = data.dropna()

#set the value of x and y from 2 columns
pd.crosstab(data.loan, data.y).plot(kind='bar')

plt.title("Customer with Loan and Subscription")
plt.xlabel("Customer with Loan")
plt.ylabel("Customer with Subscription")
plt.show()