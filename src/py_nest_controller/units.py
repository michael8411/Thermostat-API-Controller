"""Temperature conversion helpers.

The SDM API only accepts and returns Celsius, whatever scale the thermostat
displays. Consumers that work in Fahrenheit convert at the edge with these.

Source: https://developers.google.com/nest/device-access/api/thermostat
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius value to Fahrenheit.

    Args:
        celsius: Temperature in degrees Celsius.

    Returns:
        The same temperature in degrees Fahrenheit, unrounded.

    Raises:
        NotImplementedError: Until implemented.

    Implementation notes:
        1. Apply F = C * 9 / 5 + 32.
        2. Do not round here; leave rounding to the display layer.
    """
    raise NotImplementedError("To be implemented by developer")


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert a Fahrenheit value to Celsius for sending to the API.

    Args:
        fahrenheit: Temperature in degrees Fahrenheit.

    Returns:
        The same temperature in degrees Celsius, unrounded.

    Raises:
        NotImplementedError: Until implemented.

    Implementation notes:
        1. Apply C = (F - 32) * 5 / 9.
        2. Do not round here. The thermostat accepts fractional Celsius and
           rounds to its own display step.
    """
    raise NotImplementedError("To be implemented by developer")
