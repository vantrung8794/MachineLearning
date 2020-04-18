from sklearn import datasets, linear_model
import numpy as np


X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
y = np.array([[49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis=1)

repr = linear_model.LinearRegression(fit_intercept=False)
repr.fit(Xbar, y)

print('Solutions by scikit-learn : ', repr.coef_)