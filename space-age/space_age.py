SECONDS_IN_EARTH_YEAR = 31557600
ORBITAL_PERIODS = {
    'earth': 1,
    'mercury': 0.2408467,
    'venus': 0.61519726,
    'mars': 1.8808158,
    'jupiter': 11.862615,
    'saturn': 29.447498,
    'uranus': 84.016846,
    'neptune': 164.79132,
}


def age_on_planet(seconds_alive, planet):
    """Return age on a given planet."""
    annual_seconds = SECONDS_IN_EARTH_YEAR * ORBITAL_PERIODS[planet]
    return round(seconds_alive / annual_seconds, 2)


class SpaceAge:

    """
    This class doesn't need to exist.

    https://www.youtube.com/watch?v=o9pEzgHorH0
    """

    def __init__(self, seconds):
        self.seconds = seconds

    def __getattr__(self, attr):
        if attr.startswith('on_'):
            return lambda: age_on_planet(self.seconds, attr[3:])
