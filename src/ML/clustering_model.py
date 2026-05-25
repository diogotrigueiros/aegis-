import numpy as np
from sklearn.cluster import KMeans

# Executa a clusterização K-means em dados de exemplo.
# Agrupa observações em 2 clusters e devolve as etiquetas atribuídas.
def run_clustering():
    data = np.array([
        [10, 20],
        [15, 18],
        [80, 90],
        [85, 95]
    ])

    model = KMeans(n_clusters=2, n_init=10)
    model.fit(data)

    return model.labels_
