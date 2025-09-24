from domain.weather import Observer, WeatherData


class CurrentConditionsDisplay(Observer):
    """Shows the most recent reading on the console."""
    def __init__(self) -> None:
        self.last_displayed: WeatherData | None = None

    def update(self, data: WeatherData) -> None:
        self.last_displayed = data
        print(f"[Display] Temp: {data.temperature_c:.1f}°C | Humidity: {data.humidity_pct:.0f}%")
