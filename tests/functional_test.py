import os


def test_weather_cli_as_module():
    """
    Verify CLI tool can't be run as a Python module
    """
    exit_status = os.system('python3 -m weather.py dubai')
    print("Output is")

    print(exit_status)
    assert exit_status == 256


def test_weather_cli_help_arg():
    """
    Verify this CLI tool has no option for --help argument
    """
    exit_status = os.system('python3 -m weather.py --help')
    print("Output is")

    print(exit_status)
    assert exit_status == 256