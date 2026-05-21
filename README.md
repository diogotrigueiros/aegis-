# Aegis - Projeto final de IIA

Um projeto de simulação em tempo real que modela a resposta a desastres numa cidade, utilizando inteligência artificial e aprendizagem automática para otimizar operações de emergência.

##  Descrição

Aegis simula um ambiente urbano dinâmico com cidadãos, desastres e veículos de emergência. O sistema utiliza algoritmos de IA para encaminhar recursos, prever situações de crise e otimizar estratégias de resposta.

##  Funcionalidades

- **Simulação em Tempo Real**: Ambiente urbano dinâmico com cidadãos e eventos de desastre
- **Encaminhamento Inteligente**: Algoritmo A* para roteirização ótima de veículos de emergência
- **Decisões de Crise**: Minimax para estratégias de gestão de crises
- **Aprendizagem Automática**: Modelos de clustering, árvore de decisão e redes neurais
- **Otimização Genética**: Algoritmos genéticos para evolução de estratégias
- **Visualização Interativa**: Renderização Pygame com animação em tempo real
- **Análise de Dados**: Registo automático de métricas em CSV

##  Estrutura do projeto

```
src/
├── main.py
├── config.py
├── AI/
│   ├── astar.py
│   ├── minimax_crisis.py
│   └── rules_engine.py
├── ML/
│   ├── clustering_model.py
│   ├── decision_tree_model.py
│   └── neural_forecast.py
├── Otimização/
│   └── genetic_algorithm.py
├── Simulação/
│   ├── city.py
│   ├── citizen.py
│   ├── disaster.py
│   └── vehicle.py
└── Visualização/
    └── pygame_renderer.py
```

## Como executar o projeto

### Dependencias necessárias

- Python 3.8+
- Pygame
- NumPy
- Scikit-learn

### Instalação

```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instalar dependências
pip install pygame numpy scikit-learn pandas
```

### Execução do programa

```bash
python src/main.py
```

> **Nota**: Se o programa não funcionar no Git Bash, aconselha-se vivamente a executá-lo numa PowerShell.

## Componentes principais

| Componente | Descrição |
|-----------|-----------|
| **A*** | Pathfinding ótimo para veículos |
| **Minimax** | Decisões estratégicas de crise |
| **Clustering** | Análise de padrões de cidadãos |
| **Árvore de Decisão** | Priorização de emergências |
| **Rede Neural** | Previsão de desastres |
| **Algoritmo Genético** | Otimização de estratégias |

## Dataset

As métricas da simulação são registadas em `assets/city_logs.csv` para análise e treino de modelos.

## Tecnologias utilizadas

- Python 3.8+
- Pygame
- NumPy
- Scikit-learn
- Pandas

