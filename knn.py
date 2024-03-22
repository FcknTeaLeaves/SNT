
import numpy as np 

'''Données d'entraînement
donnees_entrainement = np.array([[2, 4], [1, 3], [2, 3], [3, 2], [2, 1], [5, 6], [4, 5], [4, 6], [6, 6], [5, 4]])
etiquettes_entrainement = np.array(['blue', 'blue', 'blue', 'blue', 'blue', 'orange', 'orange', 'orange', 'orange', 'orange']) 

Nouveau point à prédire 
nouveau_point = np.array([3, 3])

Donner le k optimum'''




donnees_entrainement = np.array([[2, 4], [1, 3], [2, 3], [3, 2], [2, 1], [5, 6], [4, 5], [4, 6], [6, 6], [5, 4]])
etiquettes_entrainement = np.array(['blue', 'blue', 'blue', 'blue', 'blue', 'orange', 'orange', 'orange', 'orange', 'orange']) 

nouveau_point = [3, 3]


def distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

row0 = donnees_entrainement[0]
for row in donnees_entrainement:
 distance = distance(row0, row)
 print(distance)

#https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

prediction = knn(donnees_entrainement, etiquettes_entrainement, nouveau_point, k)

print("La prédiction pour le nouveau point est:", prediction)

# Fonction KNN pour prédire l'étiquette du nouveau point
def knn(donnees_entrainement, etiquettes_entrainement, nouveau_point, k):
    
    distances = []
    
    for i in range(len(donnees_entrainement)):
        dist = distance(donnees_entrainement[i], nouveau_point)
        distances.append((dist, etiquettes_entrainement[i]))
    
    distances = sorted(distances)[:k]  # Trie les distances et garde les k plus proches
    voisins = [label for (_, label) in distances]


    prediction = max(set(voisins), key=voisins.count)
    return prediction