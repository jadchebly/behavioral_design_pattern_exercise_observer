from domain.weather import WeatherStation
from observers.current_display import CurrentConditionsDisplay
from observers.alerting import HeatAlert
from infrastructure.notifiers import PrintNotifier


def build_weather_system() -> WeatherStation:
    """TODO: Complete the system setup.
    
    This function should:
    1. Create a WeatherStation instance
    2. Create observer instances (CurrentConditionsDisplay and HeatAlert)
    3. Attach the observers to the weather station
    4. Return the configured weather station
    
    The observers should be:
    - CurrentConditionsDisplay: Shows current readings
    - HeatAlert: Alerts when temperature >= 30.0°C (uses PrintNotifier)
    """
    station = WeatherStation()

    # Create observers
    display = CurrentConditionsDisplay()
    heat_alert = HeatAlert(PrintNotifier(), threshold_c=30.0)

    # TODO: Attach observers to the station
    # Hint: Use station.attach(observer) for each observer
    # station.attach(display)
    # station.attach(heat_alert)

    return station
