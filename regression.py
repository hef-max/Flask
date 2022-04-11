import numpy as np
import joblib
import sklearn.model_selection as ms
import pandas as pd
from regression_dev import *
from sklearn.linear_model import LinearRegression
x = np.array([40,20,25,20,30,50,40,20,50,40,25,50])
y = np.array([385,400,395,365,475,440,490,420,560,525,480,510])



# students = {'hours': [29, 9, 10, 38, 16, 26, 50, 10, 30, 33, 43, 2, 39, 15, 44, 29, 41, 15, 24, 50],
#             'test_results': [65, 7, 8, 76, 23, 56, 100, 3, 74, 48, 73, 0, 62, 37, 74, 40, 90, 42, 58, 100]}

# student_data = pd.DataFrame(data=students)
# x = student_data.hours
# y = student_data.test_results

model = np.polyfit(x, y, 1)

filename = 'model.sav'
joblib.dump(model, filename)

predict = np.poly1d(model)
predict(20)


# model = LinearRegression()
# model.fit(X, y)

# print("intercept=", model.intercept_)
# print("slope=", model.coef_)

# filename = 'model.sav'
# joblib.dump(model, filename)

# load_model = joblib.load(filename)
# nilai = 20
# print(model.predict(nilai))