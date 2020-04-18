from __future__ import division, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt


def getY(w1, w0, h):
    return w1 * h + w0


# Custom not scikit-learn

X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
y = np.array([[49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis=1)

A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)

print('w = ', w)

w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(145, 185, 2)
y0 = w_0 + w_1 * x0

plt.plot(X.T, y.T, 'ro')
plt.plot(x0, y0)
plt.axis([140, 190, 45, 75])
plt.xlabel('height (cm)')
plt.ylabel('Weight (kg)')

y1 = getY(w_1, w_0, 155)
y2 = getY(w_1, w_0, 160)
print(u'y1 %.2f ' % y1)
print(u'y2 %.2f' % y2)

plt.show()
