import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

iris = pd.read_csv('dataset/Iris.csv')
iris.drop('Id', axis=1, inplace=True)
X = iris[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = iris['Species']

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3)
model = LogisticRegression()
model.fit(X_train, y_train)

pickle.dump(model, open('model.pkl', 'wb'))