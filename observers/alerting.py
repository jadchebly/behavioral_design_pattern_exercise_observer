from domain.weather import Observer, WeatherData


class HeatAlert(Observer):
    """Sends an alert when temperature exceeds a threshold."""
    def __init__(self, notifier, threshold_c: float = 30.0) -> None:
        self.threshold_c = threshold_c
        self.notifier = notifier

    def update(self, data: WeatherData) -> None:
        if data.temperature_c >= self.threshold_c:
            self.notifier.send(f"🔥 Heat alert: {data.temperature_c:.1f}°C")
