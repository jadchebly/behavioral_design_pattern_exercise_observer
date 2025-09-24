from domain.weather import WeatherStation
from observers.current_display import CurrentConditionsDisplay
from observers.alerting import HeatAlert
from infrastructure.notifiers import PrintNotifier


def build_weather_system() -> WeatherStation:
    station = WeatherStation()

    display = CurrentConditionsDisplay()
    heat_alert = HeatAlert(PrintNotifier(), threshold_c=30.0)

    station.attach(display)
    station.attach(heat_alert)

    return station
