def trigger_alarm(temperatures, threshold=75):
    return [
        sensor for sensor, temp in temperatures.items()
        if temp > threshold
    ]