import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def train_decision_tree():
    data = pd.DataFrame({
        "taxa": [1,2,3,4,5,6],
        "poluicao": [10,20,30,40,50,60],
        "sair_da_cidade": [0,0,0,1,1,1]
    })

    X = data[["taxa", "poluicao"]]
    y = data["sair_da_cidade"]

    model = DecisionTreeClassifier()
    model.fit(X, y)

    return model
