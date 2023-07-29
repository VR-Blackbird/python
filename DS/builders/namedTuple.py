from collections import namedtuple
from typing import NamedTuple
from dataclasses import dataclass

Coordinates = namedtuple("Coordinate", "lat lon")
Coor = NamedTuple("Coordinate", [("lat", float), ("lon", float)])

moscow = Coordinates(55.3, 12.34)
lucknow = Coordinates(55.3, 12.34)
print(moscow == lucknow)


m2 = Coor(55.3, 12.34)
print(m2)
print(moscow == m2)


@dataclass(frozen=True)
class CoorClass:
    lat: float
    lon: float

    def __str__(self) -> str:
        ns = "N" if self.lat >= 0 else "S"
        we = "E" if self.lon >= 0 else "W"
        return f"{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}"
