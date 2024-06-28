class SpaceAge:
    EARTH_ORBITAL_PERIOD   = 31557600     # seconds
    MERCURY_ORBITAL_PERIOD =   0.2408467  # Earth years
    VENUS_ORBITAL_PERIOD   =   0.61519726 # Earth years
    MARS_ORBITAL_PERIOD    =   1.8808158  # Earth years
    JUPITER_ORBITAL_PERIOD =  11.862615   # Earth years
    SATURN_ORBITAL_PERIOD  =  29.447498   # Earth years
    URANUS_ORBITAL_PERIOD  =  84.016846   # Earth years
    NEPTUNE_ORBITAL_PERIOD = 164.79132    # Earth years

    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self) -> float:
        return round(self.seconds / (SpaceAge.EARTH_ORBITAL_PERIOD * SpaceAge.MERCURY_ORBITAL_PERIOD), 2)

    def on_venus(self) -> float:
        return round(self.seconds / (SpaceAge.EARTH_ORBITAL_PERIOD * SpaceAge.VENUS_ORBITAL_PERIOD), 2)

    def on_mars(self) -> float:
        return round(self.seconds / (SpaceAge.EARTH_ORBITAL_PERIOD * SpaceAge.MARS_ORBITAL_PERIOD), 2)

    def on_jupiter(self) -> float:
        return round(self.seconds / (SpaceAge.EARTH_ORBITAL_PERIOD * SpaceAge.JUPITER_ORBITAL_PERIOD), 2)

    def on_saturn(self) -> float:
        return round(self.seconds / (SpaceAge.EARTH_ORBITAL_PERIOD * SpaceAge.SATURN_ORBITAL_PERIOD), 2)

    def on_uranus(self) -> float:
        return round(self.seconds / (SpaceAge.EARTH_ORBITAL_PERIOD * SpaceAge.URANUS_ORBITAL_PERIOD), 2)

    def on_neptune(self) -> float:
        return round(self.seconds / (SpaceAge.EARTH_ORBITAL_PERIOD * SpaceAge.NEPTUNE_ORBITAL_PERIOD), 2)

    def on_earth(self) -> float:
        return round(self.seconds / SpaceAge.EARTH_ORBITAL_PERIOD, 2)
