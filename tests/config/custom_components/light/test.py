"""
custom_components.light.test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Provides a mock switch platform.

Call init before using it in your tests to ensure clean test data.
"""
from homeassistant.const import STATE_ON, STATE_OFF
from tests.common import MockToggleDevice


DEVICES = []


def init(empty=False):
    """ (re-)initalizes the platform with devices. """
    global DEVICES

    DEVICES = [] if empty else [
        MockToggleDevice('Ceiling', STATE_ON),
        MockToggleDevice('Ceiling', STATE_OFF),
        MockToggleDevice(None, STATE_OFF)
    ]


def setup_platform(hass, config, add_devices_callback, discovery_info=None):
    """ Returns mock devices. """
    add_devices_callback(DEVICES)
