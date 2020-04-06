import csv
from dataclasses import dataclass, field, fields
from typing import List, Tuple

import attr
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
class PersonHours(Hours):
    ID: int
    # wed: str


@dataclass
class FixedPosition:
    commute: Tuple[int, int]
    work: Tuple[int, int]
    study: Tuple[int, int]
    housework: Tuple[int, int]
    hobby: Tuple[int, int]
    sleep: Tuple[int, int]


@dataclass
class PersonFixedPosition:
    wife_weekday = FixedPosition(
        commute=(177, 180),
        work=(180, 183),
        study=(183, 186),
        housework=(186, 189),
        hobby=(201, 204),
        sleep=(213, 216),
    )

    wife_holiday = FixedPosition(
        commute=(216, 219),
        work=(219, 222),
        study=(222, 225),
        housework=(225, 228),
        hobby=(240, 243),
        sleep=(252, 255),
    )

    husband_weekday = FixedPosition(
        commute=(216, 219),
        work=(219, 222),
        study=(222, 225),
        housework=(225, 228),
        hobby=(240, 243),
        sleep=(252, 255),
    )

    husband_holiday = FixedPosition(
        commute=(294, 297),
        work=(297, 300),
        study=(300, 303),
        housework=(303, 306),
        hobby=(318, 321),
        sleep=(330, 333),
    )


@attr.s
class DataFactory:
    fixed_data = attr.ib()
    hour_type = attr.ib()

    @hour_type.validator
    def check_hour_type(self, attribute, value):
        trgt_type = [
            "wife_weekday",
            "wife_holiday",
            "husband_weekday",
            "husband_holiday",
        ]
        if not isinstance(value, str):
            raise TypeError("name must be str")
        if value not in trgt_type:
            raise Exception("invalid hour_type")

    def create(self):
        position = getattr(PersonFixedPosition(), self.hour_type).__dict__

        with open(self.fixed_data, "r") as f:
            for i in f:
                hours = {k: i[v[0] : v[1]] for (k, v) in position.items()}
                hours["ID"] = i[0:4]
                person = PersonHours(**hours)
                print(person.commute)

        # Hours(commute, work, study, housework, hobby, sleep)


class Name:
    pass


if __name__ == "__main__":
    d = PersonFixedPosition()
    ww = getattr(d, "wife_weekday")
    wh = getattr(d, "wife_holiday")
    hw = getattr(d, "husband_weekday")
    hh = getattr(d, "husband_holiday")
    print(hh.__dict__)
    purpose = [f.name for f in fields(Hours)]

    a = DataFactory("P27_3.txt", "husband_weekday")
    a.create()
