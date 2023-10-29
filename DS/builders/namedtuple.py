from collections import namedtuple
from typing import NamedTuple


City = namedtuple("City", "name country population coordinates")

value1 = ("Tokyo", "JP", 190, (12.5, 13.2))

tokyo = City._make(value1)

tokyo_dict = tokyo._asdict()


# Default value for namedtuple class
Coordinate = namedtuple("Coordinate", "lat lon reference", defaults=[0, "WDSD12"])

cor1 = Coordinate(1)


class Coordinate(NamedTuple):
    lat: float
    lon: float
    reference: str = "WSD12"

    def __repr__(self) -> str:
        ns = "N" if self.lat >= 0 else "S"
        we = "E" if self.lon >= 0 else "W"

        return f"{abs(self.lat):.1f}` {ns} and {abs(self.lon):.1f}` {we}"


coor2 = Coordinate(12, 13)