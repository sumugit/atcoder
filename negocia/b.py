import numpy as np

def ridge(X, y, alpha):
    beta = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X) + alpha * np.identity(X.shape[1])), X.T), y)
    return beta

X = np.random.rand(100, 10)
y = np.random.rand(100)
alpha = 0.01

print(ridge(X, y, alpha))