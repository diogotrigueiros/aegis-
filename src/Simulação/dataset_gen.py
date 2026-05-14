import pandas as pd
from pathlib import Path

class SimulationLogger:
    def __init__(self):
        self.records = []
        self.project_root = Path(__file__).parent.parent.parent
        self.output_path = self.project_root / "assets" / "city_logs.csv"

    def log(self, turn, population, disasters):
        self.records.append({
            "turn": turn,
            "population": population,
            "disasters": disasters
        })

        if turn % 50 == 0:
            self.export()

    def export(self):
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        df = pd.DataFrame(self.records)
        df.to_csv(self.output_path, index=False)
        print(f"Dataset exportado para {self.output_path}")


if __name__ == "__main__":
    logger = SimulationLogger()

    for turn in range(1, 151):
        logger.log(turn, population=1000 + turn*10, disasters=turn % 10)

    logger.export()
