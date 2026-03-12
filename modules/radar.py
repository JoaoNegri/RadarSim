
class pulseRadar:
    def __init__(self, x: float, y: float, orientation: float, pulse_length: float, pulse_interval: float, amplitude: float):
        """
        Initialize a radar of type pulseRadar.

        :param x: The x-coordinate of the radar position in meters.
        :param y: The y-coordinate of the radar position in meters.
        :param orientation: The orientation of the radar in degrees (90º is pointing up).
        :param pulse_length: The length of the radar pulse in milliseconds.
        :param pulse_interval: The interval between radar pulses in milliseconds.
        :param amplitude: The amplitude in volts of the radar pulse.
        """
        self.x = x
        self.y = y
        self.orientation = orientation
        self.pulse_length = pulse_length # ms
        self.pulse_interval = pulse_interval #ms
        self.amplitude = amplitude # volts
