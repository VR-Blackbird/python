from typing import ClassVar, NamedTuple
from dataclasses import dataclass, field


# class NewClass(NamedTuple):
#     a: int  # Instance attribute
#     b: str = "123"  # Instance Attribute
#     c: ClassVar[str] = "1234"  # Class Attribute, Class Var for proper type checking


@dataclass(frozen=True, order=True)
class DataClass:
    b: int
    a: str = "123"
    c = "1234"


@dataclass
class ClubMember:
    name: str
    guests: list[str] = field(default_factory=list)


@dataclass
class HackerClub(ClubMember):
    all_handles: ClassVar[set[str]] = set()  # For proper type checking with Mypy
    handle: str = ""

    def __post_init__(self):
        cls = self.__class__

        if self.handle == "":
            self.handle = self.name.split()[0] if " " in self.name else self.name
        if self.handle in cls.all_handles:
            msg = f"handle {self.handle!r} already exists."
            raise ValueError(msg)
        cls.all_handles.add(self.handle)
