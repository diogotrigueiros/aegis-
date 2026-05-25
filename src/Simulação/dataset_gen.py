import pandas as pd
from pathlib import Path

# Classe que regista os dados da simulação e exporta-os para CSV.
class SimulationLogger:
    def __init__(self):
        self.records = []
        self.project_root = Path(__file__).parent.parent.parent
        self.output_path = self.project_root / "assets" / "city_logs1.csv"

    # Adiciona uma entrada de registo para o turno atual.
    # Normaliza o número de desastres para um valor entre 1 e 3.
    def log(self, turn, population, disasters):
        disasters = min(max(int(disasters), 1), 3)

        self.records.append({
            "turn": turn,
            "population": 60,
            "disasters": disasters
        })

        if turn % 50 == 0:
            self.export()

    # Exporta todos os registos acumulados para um ficheiro CSV.
    def export(self):
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        df = pd.DataFrame(self.records)
        df.to_csv(self.output_path, index=False)
        print(f"Dataset exported to {self.output_path}")


if __name__ == "__main__":
    logger = SimulationLogger()

    for turn in range(1, 151):
        logger.log(turn, population=60, disasters=((turn - 1) % 3) + 1)

    logger.export()
