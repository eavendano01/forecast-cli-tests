from hypothesis import given, settings, Verbosity
from hypothesis.strategies import text

import os

text_arg = text(min_size=0, max_size=None)


# happy paths
def test_weather_cli_valid_city():
    """
    Verify CLI tool returns result with a valid city
    """
    exit_status = os.system('python3 weather.py dubai')
    print("Output is")

    print(exit_status)
    assert exit_status == 0

#Edge cases


def test_weather_cli_invalid_city():
    """
    Verify CLI tool returns result with a valid city
    """
    exit_status = os.system('python3 weather.py invalid_city')
    print("Output is")

    print(exit_status)
    assert exit_status == 256


def test_weather_cli_no_city_arg():
    """
    Verify CLI tool returns result with a valid city
    """
    exit_status = os.system('python3 weather.py')
    print("Output is")

    print(exit_status)
    assert exit_status == 512

def test_weather_cli_multiple_args():
    """
    Verify CLI tool returns result with a valid city
    """
    exit_status = os.system('python3 weather.py dubai london')
    print("Output is")

    print(exit_status)
    assert exit_status == 512


'''
This method is intended to generate random values 
as arguments to spawn new edge cases.
Therefore, no assertions were added
'''
@settings(deadline=None, max_examples=20,verbosity=Verbosity.verbose)
@given(arg=text_arg)
def test_weather_cli_valid_city_vals(arg):
    """
    Verify CLI tool behaviour with random text as city arguments
    """
    command = 'python3 weather.py '+arg
    print(command)
    exit_status = os.system(command)
    print(exit_status)