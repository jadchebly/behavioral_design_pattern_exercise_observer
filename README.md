# Weather Station Observer Pattern Exercise

## Overview

This is a hands-on programming exercise to implement the **Observer Pattern** using a weather monitoring system. You will complete a partially implemented weather station that notifies multiple observers when weather conditions change.

## Learning Objectives

By completing this exercise, you will:

- **Understand the Observer Pattern**: Learn how subjects notify observers about state changes
- **Practice loose coupling**: Implement a system where subjects and observers are decoupled
- **Apply SOLID principles**: Use dependency inversion and single responsibility principles
- **Work with abstract base classes**: Implement concrete classes from abstract interfaces
- **Handle collections of observers**: Manage dynamic subscription/unsubscription

## The Observer Pattern

The Observer Pattern defines a one-to-many dependency between objects. When one object (the **Subject**) changes state, all dependent objects (**Observers**) are automatically notified and updated.

### Key Components

1. **Subject (WeatherStation)**: Maintains a list of observers and notifies them of state changes
2. **Observer Interface**: Defines the contract that all observers must implement
3. **Concrete Observers**: Specific implementations that react to notifications
4. **WeatherData**: The data structure containing the state information

## System Architecture

```
WeatherStation (Subject)
    ├── Maintains list of observers
    ├── attach(observer) - Subscribe an observer
    ├── detach(observer) - Unsubscribe an observer
    └── notify_observers() - Alert all observers of changes

Observer (Abstract Interface)
    └── update(data) - Method called when subject changes

CurrentConditionsDisplay (Concrete Observer)
    └── Displays current weather readings

HeatAlert (Concrete Observer)
    └── Sends alerts when temperature exceeds threshold
```

## Project Structure

```
weather_app/
├── domain/
│   └── weather.py          # Core domain models (WeatherStation, Observer)
├── observers/
│   ├── current_display.py  # Display observer implementation
│   └── alerting.py         # Alert observer implementation
├── infrastructure/
│   └── notifiers.py        # Notification infrastructure
├── application/
│   └── bootstrap.py        # System setup and configuration
├── presentation/
│   └── cli.py              # Command-line interface
└── tests/
    ├── test_integration_cli.py
    └── test_integration_system.py
```

## What You Need to Implement

The codebase is partially implemented. You need to complete these key parts:

### 1. WeatherStation Observer Management (`domain/weather.py`)
- Implement `attach(observer)` method to subscribe observers
- Implement `detach(observer)` method to unsubscribe observers
- Add notification logic in `set_measurements()` to notify all observers

### 2. Observer Implementations
- Complete `CurrentConditionsDisplay.update()` in `observers/current_display.py`
- Complete `HeatAlert.update()` in `observers/alerting.py`

### 3. System Integration
- Ensure the bootstrap properly sets up the observer relationships

## Getting Started

1. **Review the existing code** to understand the structure
2. **Run the tests** to see what's currently failing:
   ```bash
   python -m pytest tests/ -v
   ```
3. **Implement the missing parts** following the TODO comments
4. **Test your implementation** until all tests pass

## Expected Behavior

When complete, your system should:

- **Display readings**: Show temperature and humidity for every measurement
- **Send heat alerts**: Notify when temperature >= 30.0°C
- **Support multiple observers**: Handle dynamic subscription/unsubscription
- **Pass all tests**: Both integration tests should pass

### Sample Output

```bash
python presentation/cli.py --temp 28.0 --humidity 50
# Output: [Display] Temp: 28.0°C | Humidity: 50%

python presentation/cli.py --temp 32.0 --humidity 40
# Output: 
# [Display] Temp: 32.0°C | Humidity: 40%
# [Notify] Heat alert: 32.0°C
```

## Testing Your Implementation

Run the tests to verify your implementation:

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_integration_system.py -v

# Run with output capture to see print statements
python -m pytest tests/test_integration_system.py -v -s
```

## Success Criteria

- All tests pass  
- Weather station properly notifies observers  
- Display observer shows readings correctly  
- Heat alert observer triggers at the right temperature  
- CLI produces expected output  

## Extension Ideas

Once you've completed the basic implementation, consider these extensions:

1. **Add new observer types**: Humidity alerts, data logging, statistics tracking
2. **Implement observer priorities**: Some observers get notified before others
3. **Add observer filtering**: Observers can specify what changes they care about
4. **Improve error handling**: Handle cases where observers fail during updates

## Key Concepts Reinforced

- **Separation of Concerns**: Each observer has a single responsibility
- **Open/Closed Principle**: Easy to add new observers without modifying existing code
- **Loose Coupling**: Weather station doesn't know details about specific observers
- **Dynamic Behavior**: Observers can be added/removed at runtime

Good luck with the implementation!