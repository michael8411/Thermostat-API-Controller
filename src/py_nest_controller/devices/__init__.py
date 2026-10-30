"""High level device API."""

from py_nest_controller.devices.discovery import list_thermostats
from py_nest_controller.devices.thermostat import Thermostat

__all__ = ["Thermostat", "list_thermostats"]
