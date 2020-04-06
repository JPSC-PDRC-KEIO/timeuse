import csv
from dataclasses import dataclass, field, fields
from typing import List, Tuple

import numpy as np


@dataclass
class Hours:
    commute: int
    work: int
    study: int
    housework: int
    hobby: int
    sleep: int


@dataclass
class FixedLenPosition:
    commute: Tuple[int, int]
    work: Tuple[int, int]
    study: Tuple[int, int]
    housework: Tuple[int, int]
    hobby: Tuple[int, int]
    sleep: Tuple[int, int]

class PersonPosition:

    wife_weekday_pos: List[Tuple] = field(
        default_factory=lambda: [
            (177, 180),
            (180, 183),
            (183, 186),
            (186, 189),
            (201, 204),
            (213, 216),
        ]
    )

    wife_holiday_pos: List[Tuple] = field(
        default_factory=lambda: [
            (216, 219),
            (219, 222),
            (222, 225),
            (225, 228),
            (240, 243),
            (252, 255),
        ]
    )
    husband_weekday_pos: List[Tuple] = field(
        default_factory=lambda: [
            (255, 258),
            (258, 261),
            (261, 264),
            (264, 267),
            (279.282),
            (291, 294),
        ]
    )
    husband_holiday_pos: List[Tuple] = field(
        default_factory=lambda: [
            (294, 297),
            (297, 300),
            (300, 303),
            (303, 306),
            (318, 321),
            (330, 333),
        ]
    )


class DataFactory:
    def __init__(self, person, day_type):
        self.person = person
        self.day_type = day_type

    def make(self):
        pass
        # Hours(commute, work, study, housework, hobby, sleep)


class Name:
    pass


if __name__ == "__main__":
    d = FixedLenPosition()
    print(d.wife_weekday_pos)
    purpose = [f.name for f in fields(Hours)]
