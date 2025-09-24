import argparse
from application.bootstrap import build_weather_system


def main() -> None:
    parser = argparse.ArgumentParser(description="Weather Station CLI")
    parser.add_argument("--temp", type=float, required=True, help="Temperature in °C")
    parser.add_argument("--humidity", type=float, required=True, help="Humidity in %")
    args = parser.parse_args()

    station = build_weather_system()
    station.set_measurements(args.temp, args.humidity)


if __name__ == "__main__":
    main()
