import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import seaborn as sn
import matplotlib.pyplot as plt
#Build the data set
artists = {
         'age':[36,42,23,52,43,44,66,35,52,35,24,18,45],
         'experience': [10,12,4,4,21,14,3,14,13,5,3,3,9],
         'rank': [9,4,6,4,8,5,7,9,7,9,5,7,9],
         'nationality':[1,2,3,2,2,1,3,1,3,3,2,1,1],
         'go':[0,0,0,0,1,0,1,1,1,1,0,1,1]
}


#build dataframe from the dataset
df = pd.DataFrame(artists, columns=['age', 'experience', 'rank', 'nationality', 'go'])
#create logistic regression using the dataframe
X = df[['age', 'experience', 'rank', 'nationality']]
Y = df['go']
#apply the test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)
#apply logistic regression
logistic_regression = LogisticRegression()
logistic_regression.fit(X_train, Y_train)
y_pred = logistic_regression.predict(X_test)
print(X_test)
print(y_pred)
#build confusion matrix
confusion_matrix = pd.crosstab(Y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(confusion_matrix, annot=True)
#compute accuracy of prediction
print('Accuracy: ', (metrics.accuracy_score(Y_test, y_pred)) * 100)
#show the graph
plt.show()