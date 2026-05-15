def evaluate_city_risk(temperature, humidity):
    if temperature > 40 and humidity < 20:
        return "HIGH FIRE RISK"

    return "NORMAL"
