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
        """TODO: Implement observer subscription.
        
        Add the observer to the _observers list if not already present.
        Hint: Use 'not in' to check if observer is already subscribed.
        """
        # TODO: Your implementation here
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """TODO: Implement observer unsubscription.
        
        Remove the observer from the _observers list if present.
        Hint: Use 'in' to check if observer exists before removing.
        """
        # TODO: Your implementation here
        if observer in self._observers:
            self._observers.remove(observer)

    def set_measurements(self, temperature_c: float, humidity_pct: float) -> None:
        """TODO: Complete the notification logic.
        
        1. Create a WeatherData object with the measurements
        2. Store it in self._last
        3. Notify all observers by calling their update() method
        
        Hint: Iterate over self._observers and call update(data) on each one.
        Consider using list(self._observers) to avoid issues if observers modify the list.
        """
        data = WeatherData(temperature_c, humidity_pct)
        self._last = data
        # TODO: Add observer notification logic here
        for observer in self._observers:
            observer.update(data)



    def last(self) -> WeatherData | None:
        return self._last
