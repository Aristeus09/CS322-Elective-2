import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#set font and canvas color
plt.rc("font", size=14)
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
#read data
data = pd.read_csv('banking.csv', header=0)
data = data.dropna()
#count values of the column to be read
data['y'].value_counts()
count_wo_loan = len(data[data['loan'] == "no"])
count_w_loan = len(data[data['loan'] == "yes"])
pct_wo_loan = count_wo_loan / (count_wo_loan + count_w_loan)
pct_w_loan = count_w_loan / (count_wo_loan + count_w_loan)
print("Number of customers without loan:", count_wo_loan)
print("Percentage of customers without loan:{:.2f}".format(pct_wo_loan * 100))
print("Number of customers with loan:", count_w_loan)
print("Percentage of customers with loan:{:.2f}".format(pct_w_loan * 100))
print("Total Customers:", (count_wo_loan + count_w_loan))
#graph the data
sns.countplot(x='y', data=data, palette='hls')
plt.title("Customer Loan Graph")
plt.show()