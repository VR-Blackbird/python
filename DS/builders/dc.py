from collections import namedtuple
from typing import NamedTuple
from dataclasses import dataclass

namedtup = namedtuple("Coordinates", "lat lon")
moscow = namedtup(lat=13.2, lon=15.3)
sydney = namedtup(19.8, 80.3)


typed_tuple = NamedTuple("Coordinates", lat=float, lon=float)
jaipur = typed_tuple(12, 13)


class Coordinates(NamedTuple):
    lat: float
    lon: float

    def __repr__(self) -> str:
        ns = "N" if self.lat >= 0 else "S"
        we = "E" if self.lon >= 0 else "W"

        return f"{abs(self.lat):.1f}` {ns} and {abs(self.lon):.1f}` {we}"


coord = Coordinates(13.343, 18.129)


@dataclass(frozen=True)
class Coordinates:
    lat: float
    lon: float

    def __repr__(self) -> str:
        ns = "N" if self.lat >= 0 else "S"
        we = "E" if self.lon >= 0 else "W"

        return f"{abs(self.lat):.1f}` {ns} and {abs(self.lon):.1f}` {we}"
