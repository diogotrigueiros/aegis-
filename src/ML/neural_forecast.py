import torch
import torch.nn as nn

# Modelo simples de previsão com uma única camada linear.
# Recebe entradas de dimensão 1 e produz uma saída de dimensão 1.
class ForecastModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.layer = nn.Linear(1, 1)

    def forward(self, x):
        return self.layer(x)
