from sklearn.datasets import make_classification
import numpy as np
X , y = make_classification(n_samples=100 , n_features=2 , n_informative=1 , n_redundant=0 , n_classes=2 , n_clusters_per_class=1 , random_state=42 , hypercube=False ,class_sep=10)

import matplotlib.pyplot as plt

def step(z):
    return 1 if z>0 else 0

def Perceptron(X,y):
    X = np.insert(X,0,1,axis=1)
    weights = np.ones(X.shape[1])
    lr = 0.01

    for i in range(1000):
        j = np.random.randint(1,100)
        y_hat = step(np.dot(X[j],weights))
        weights = weights + lr*(y[j]-y_hat)*X[j]

    return weights[0],weights[1:]

intercept_ , coef_ = Perceptron(X,y)
slope = -(coef_[0]/coef_[1])
y_intercept = -(intercept_/coef_[1])

print('Details of the line :' )
print('Coef: ',coef_)
print('Intercept: ',intercept_ )
print('Slope: ',slope)
print('y_intercept: ',y_intercept)

x_input = np.linspace(-3,3,100)
y_input = slope*x_input + y_intercept

plt.figure(figsize=(10, 6))
plt.plot(x_input,y_input,color='red')
plt.scatter(X[y == 0, 0], X[y == 0, 1], color='blue', label='Negative points (0)', s=100)
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='green', label='Positive points (1)', s=100)
plt.legend()
plt.title("Class-wise Scatter Plot")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
