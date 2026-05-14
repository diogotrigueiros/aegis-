import pandas as pd
from pathlib import Path

class SimulationLogger:
    def __init__(self):
        self.records = []

    def log(self, turn, population, disasters):
        self.records.append({
            "turn": turn,
            "population": population,
            "disasters": disasters
        })

        if turn % 50 == 0:
            self.export()

    def export(self):
        Path("data/logs").mkdir(parents=True, exist_ok=True)

        df = pd.DataFrame(self.records)
        df.to_csv("assets/city_logs.csv", index=False)
