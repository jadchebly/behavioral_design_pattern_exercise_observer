from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass(frozen=True)
class WeatherData:
    temperature_c: float
    humidity_pct: float


class Observer(ABC):
    @abstractmethod
    def update(self, data: WeatherData) -> None:
        pass


class WeatherStation:
    """Subject in the Observer pattern."""
    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self._last: WeatherData | None = None

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def set_measurements(self, temperature_c: float, humidity_pct: float) -> None:
        data = WeatherData(temperature_c, humidity_pct)
        self._last = data
        for obs in list(self._observers):
            obs.update(data)

    def last(self) -> WeatherData | None:
        return self._last
