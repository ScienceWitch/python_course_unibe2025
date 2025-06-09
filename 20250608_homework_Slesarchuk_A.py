import pandas as pd

data = pd.read_csv('x_y_to_fit.csv', delimiter='\t')
print(data.head())

from sklearn.model_selection import train_test_split

# split data
train_data, temp_data = train_test_split(data, test_size=0.4)
val_data, test_data = train_test_split(temp_data, test_size=0.5)
print('train_size = {}, validation_size = {}, test_size ={}'.format(len(train_data), len(val_data), len(test_data)))

x_train = train_data[['x']].values
y_train = train_data['y'].values
x_val = val_data[['x']].values
y_val = val_data['y'].values

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# try polynomial degrees from 1 to 10
max_degree = 10
validation_errors = []

for degree in range(1, max_degree + 1):
    poly = PolynomialFeatures(degree)
    x_poly_train = poly.fit_transform(x_train)
    x_poly_val = poly.transform(x_val)
    
    model = LinearRegression()
    model.fit(x_poly_train, y_train)
    
    y_val_pred = model.predict(x_poly_val)
    val_mse = mean_squared_error(y_val, y_val_pred)
    validation_errors.append(val_mse)

# Identify the best degree based on validation error
best_degree = np.argmin(validation_errors) + 1
best_val_error = validation_errors[best_degree - 1]
print(best_degree, best_val_error)

# Combine training and validation sets
train_val_data = pd.concat([train_data, val_data])
x_train_val = train_val_data[['x']].values
y_train_val = train_val_data['y'].values

# Prepare test data
x_test = test_data[['x']].values
y_test = test_data['y'].values

# Train the best model (degree 2) on the combined data
poly_best = PolynomialFeatures(best_degree)
x_poly_train_val = poly_best.fit_transform(x_train_val)
x_poly_test = poly_best.transform(x_test)

best_model = LinearRegression()
best_model.fit(x_poly_train_val, y_train_val)

# Evaluate on the test set
y_test_pred = best_model.predict(x_poly_test)
test_mse = mean_squared_error(y_test, y_test_pred)
print(test_mse)


# visualize
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

x_plot = np.linspace(data['x'].min(), data['x'].max(), 500).reshape(-1, 1)
x_plot_poly = poly_best.transform(x_plot)
y_plot = best_model.predict(x_plot_poly)

plt.figure(figsize=(10, 6))
plt.scatter(train_data['x'], train_data['y'], label='Training Data', color='blue')
plt.scatter(val_data['x'], val_data['y'], label='Validation Data', color='orange')
plt.scatter(test_data['x'], test_data['y'], label='Test Data', color='green')
plt.plot(x_plot, y_plot, label='Polynomial Degree Fit', color='red', linewidth=2)

plt.title('Polynomial Regression Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()


