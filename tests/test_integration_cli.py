import sys
from importlib import reload
import presentation.cli as cli

def run_cli_with_args(temp: float, humidity: float, capsys):
    argv_backup = sys.argv
    try:
        sys.argv = ["prog", "--temp", str(temp), "--humidity", str(humidity)]
        reload(cli)
        cli.main()
        return capsys.readouterr().out
    finally:
        sys.argv = argv_backup

def test_cli_cool_reading_only_displays(capsys):
    out = run_cli_with_args(28.0, 50.0, capsys)
    assert "[Display] Temp: 28.0°C | Humidity: 50%" in out
    assert "Heat alert" not in out

def test_cli_hot_reading_triggers_alert(capsys):
    out = run_cli_with_args(31.5, 42.0, capsys)
    assert "[Display] Temp: 31.5°C | Humidity: 42%" in out
    assert "Heat alert: 31.5°C" in out
