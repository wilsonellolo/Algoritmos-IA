from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn import preprocessing
import matplotlib.pyplot as plt

# Crear el dataset

# Para outlook
outlook = ['sunny', 'sunny', 'overcast', 'rain', 'rain', 'rain', 'overcast',
           'sunny', 'sunny', 'rain', 'sunny', 'overcast', 'overcast', 'rain']

# Para temperature
temperature = ['hot', 'hot', 'hot', 'mild', 'cool', 'cool',
               'cool', 'mild', 'cool', 'mild', 'mild', 'mild', 'hot', 'mild']

# Para humidity
humidity = ['high', 'high', 'high', 'high', 'normal', 'normal', 'normal',
            'high', 'normal', 'normal', 'normal', 'high', 'normal', 'high']

# Para windy
windy = ['false', 'true', 'false', 'false', 'false', 'true', 'true',
         'false', 'false', 'false', 'true', 'true', 'false', 'true']

# Para play
play = ['N', 'N', 'P', 'P', 'P', 'N', 'P', 'N', 'P', 'P', 'P', 'P', 'P', 'N']


# Crear el codificador de etiquetas
le = preprocessing.LabelEncoder()


# Convertir strings en numeros
outlook_encoded = le.fit_transform(outlook)
temperature_encoded = le.fit_transform(temperature)
humidity_encoded = le.fit_transform(humidity)
windy_encoded = le.fit_transform(windy)
label = le.fit_transform(play)

print("outlook: ", outlook_encoded)
print("temp: ", temperature_encoded)
print("humidity: ", humidity_encoded)
print("windy: ", windy_encoded)
print("PLAY: ", label)


# Combinar atributos en una misma lista
features = list(zip(outlook_encoded, temperature_encoded,
                    humidity_encoded, windy_encoded))
print(features)


model = GaussianNB()
model.fit(features, label)
predicted = model.predict([[2, 1, 0, 0]])  # sunny, hot, high, false
print("predicted Value: ", predicted)
