# Avalia o risco na cidade com base na temperatura e humidade.
# Se a temperatura for muito elevada e a humidade muito baixa, indica alto risco de incêndio.
def evaluate_city_risk(temperature, humidity):
    if temperature > 40 and humidity < 20:
        return "HIGH RISK OF FIRE"

    return "NORMAL"
