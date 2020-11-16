# 201314158
# Wilson Palma
# I.A. TAREA 7
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import tree
#x= deaths
#y = tests
# there are agruped by 10 years old
x = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
y = [[10], [20], [30], [40], [50], [60], [70], [80], [90]]
model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)
poly = PolynomialFeatures(degree=1, include_bias=True)
x_poly = poly.fit_transform(x)
model.fit(x_poly, y)
y_pred = model.predict(x_poly)
plt.scatter(x, y)
plt.plot(x, y_pred, color='r')
rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)
print('R2 (ajuste de la prediccion): ' + str(r2))
print('RMSE: ', rmse)

x_new_min = 0.0
x_new_max = 20.0
# plt.grid()
plt.xlim(x_new_min, x_new_max)
plt.ylim(0, 1000)
#title = 'Degree = { }; RMSE = { }; R2 = { }'.format(nb_degree,)

plt.title("Polynomial Linear Regression using scikit-learn and python 3\n")
plt.xlabel('x')
plt.ylabel('y')

plt.show()
# con una curva de grado 6 la prediccion es muy acertada.
# ya que llega a un R2 de 0.9995107622140
# ==========================
