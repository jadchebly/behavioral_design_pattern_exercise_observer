from domain.weather import Observer, WeatherData


class HeatAlert(Observer):
    """Sends an alert when temperature exceeds a threshold."""
    def __init__(self, notifier, threshold_c: float = 30.0) -> None:
        self.threshold_c = threshold_c
        self.notifier = notifier

    def update(self, data: WeatherData) -> None:
        """TODO: Implement the heat alert logic.
        
        This method is called when the WeatherStation has new measurements.
        
        Requirements:
        1. Check if the temperature meets or exceeds self.threshold_c
        2. If it does, send an alert using self.notifier.send()
        3. Alert message format: "Heat alert: {temp}°C"
        
        Hints:
        - Use data.temperature_c to get the temperature
        - Use >= to compare with self.threshold_c
        - Format temperature to 1 decimal place (.1f)
        - Call self.notifier.send(message) to send the alert
        """
        # TODO: Your implementation here
        pass
