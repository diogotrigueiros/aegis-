import torch
import torch.nn as nn

class ForecastModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.layer = nn.Linear(1, 1)

    def forward(self, x):
        return self.layer(x)
