import numpy as np
from sklearn.cluster import KMeans

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
