from sklearn.neural_network import MLPClassifier


# training set
# es como para el xor
# x1 x2  y
# 0  0   0
# 0  1   1
# 1  0   1
# 1  1   0
x = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 0]

# creando el modelo
model = MLPClassifier(activation='logistic', max_iter=200,
                      hidden_layer_sizes=(4,), alpha=0.001, solver='lbfgs')

# entrenar el modelo
model.fit(x, y)

# predecir salida
print('predictions: ', model.predict(x))
