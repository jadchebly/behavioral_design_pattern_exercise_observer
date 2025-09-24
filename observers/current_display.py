from domain.weather import Observer, WeatherData


class CurrentConditionsDisplay(Observer):
    """Shows the most recent reading on the console."""
    def __init__(self) -> None:
        self.last_displayed: WeatherData | None = None

    def update(self, data: WeatherData) -> None:
        """TODO: Implement the display update logic.
        
        This method is called when the WeatherStation has new measurements.
        
        Requirements:
        1. Store the data in self.last_displayed
        2. Print the current conditions in the format:
           "[Display] Temp: {temp}°C | Humidity: {humidity}%"
        
        Hints:
        - Use data.temperature_c for temperature
        - Use data.humidity_pct for humidity
        - Format temperature to 1 decimal place (.1f)
        - Format humidity as integer (.0f)
        """
        # TODO: Your implementation here
        pass
