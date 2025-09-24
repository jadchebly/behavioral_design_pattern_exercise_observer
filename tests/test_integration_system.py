import re
from application.bootstrap import build_weather_system

def test_end_to_end_system_prints_display_and_alert(capsys):
    station = build_weather_system()

    # Cool reading
    station.set_measurements(28.0, 50.0)
    out1 = capsys.readouterr().out
    assert "[Display] Temp: 28.0°C | Humidity: 50%" in out1
    assert "Heat alert" not in out1

    # Hot reading
    station.set_measurements(32.0, 40.0)
    out2 = capsys.readouterr().out
    assert "[Display] Temp: 32.0°C | Humidity: 40%" in out2
    assert re.search(r"\[Notify\].*Heat alert: 32\.0°C", out2), out2
