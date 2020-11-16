# Wilson Palma
# 201314158
from sklearn.neighbors import NearestCentroid
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
X = np.array([[31, 3045, 5], [21, 5790, 15], [107, 28883, 25], [209, 28398, 35], [479, 18996, 45], [
             757, 12701, 55], [1032, 7673, 65], [575, 2317, 75], [241, 827, 85], [41, 134, 95], ])
# para mostrar sin aplicar clustering
plt.scatter(X[:, 0], X[:, 1], label='True Position')
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
print(kmeans.cluster_centers_)
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='rainbow')
# para imprimir centroides
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1], color='black')
plt.show()


# con lo siguiente ya podemos clasificar las clases,
# y poder  decir que clase es cada cosa


x = np.array([[13, 5], [12, 7], [30, 2], [37, 1], [18, 4], [19, 3], [
             25, 3], [12, 8], [22, 3], [27, 2], [45, 1], [33, 1], [26, 3]])
y = np.array(['I', 'I', 'R', 'I', 'I', 'I', 'R', 'I', 'R', 'R', 'I', 'I', 'R'])
clf = NearestCentroid()
clf.fit(x, y)
print(clf.predict([[15, 2], [23, 3], [45, 1]]))
