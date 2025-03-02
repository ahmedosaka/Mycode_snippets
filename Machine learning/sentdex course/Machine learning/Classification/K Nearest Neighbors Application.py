import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.model_selection import train_test_split
import pandas as pd

df= pd.read_csv('breast-cancer-wisconsin.data')
# print(df.head())

df.replace('?', -99999, inplace=True)

df.drop(['id'], 1, inplace=True)
# print(df.columns)


X= np.array(df.drop(['class'],1))
y= np.array(df['class'])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train,y_train)


accuracy= clf.score(X_test,y_test)
print(accuracy)