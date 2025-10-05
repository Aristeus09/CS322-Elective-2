import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#set font and canvas color
plt.rc("font", size=14)
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
#read_data
data = pd.read_csv('candy-data.csv', header=0)
data = data.dropna()
#count values of the column to be read
data['winpercent'].value_counts()
count_crice_prod = len(data[data['crispedricewafer'] == 0])
count_no_crice_prod = len(data[data['crispedricewafer'] == 1])
crice_no_prod = count_no_crice_prod / (count_no_crice_prod + count_crice_prod) #no produce of crisped rice
crice_prod = count_crice_prod / (count_no_crice_prod + count_crice_prod) #have produce of crisped rice
print("Percentage of no crisped rice wafer products: {:.2f}%"
      .format(crice_no_prod * 100))
print("Percentage of crisped rice wafer products: {:.2f}%"
      .format(crice_prod * 100))
#graph the data
sns.countplot(x='crispedricewafer', data=data, palette='hls')
plt.title("Crisped Rice Wafer Products Graph")
plt.show()