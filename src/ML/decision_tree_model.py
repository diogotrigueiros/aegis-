import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Cria e treina um classificador de árvore de decisão com dados de exemplo.
# A função devolve o modelo treinado para inferência posterior.
def train_decision_tree():
    data = pd.DataFrame({
        "tax": [1,2,3,4,5,6],
        "polution": [10,20,30,40,50,60],
        "out_of_town": [0,0,0,1,1,1]
    })

    X = data[["tax", "polution"]]
    y = data["out_of_town"]

    model = DecisionTreeClassifier()
    model.fit(X, y)

    return model
