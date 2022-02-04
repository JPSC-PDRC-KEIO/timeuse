from dataclasses import dataclass
from pathlib import Path
import itertools as it

import layouts
import factory
import checker

wife_weekday_spec = layouts.HoursColSpecs(
    commute=(177, 180),
    work=(180, 183),
    study=(183, 186),
    housework=(186, 189),
    hobby=(201, 204),
    sleep=(213, 216),
)

wife_holiday_spec = layouts.HoursColSpecs(
    commute=(216, 219),
    work=(219, 222),
    study=(222, 225),
    housework=(225, 228),
    hobby=(240, 243),
    sleep=(252, 255),
)

husband_weekday_spec = layouts.HoursColSpecs(
    commute=(255, 258),
    work=(258, 261),
    study=(261, 264),
    housework=(264, 267),
    hobby=(279, 282),
    sleep=(291, 294),
)

husband_holiday_spec = layouts.HoursColSpecs(
    commute=(294, 297),
    work=(297, 300),
    study=(300, 303),
    housework=(303, 306),
    hobby=(318, 321),
    sleep=(330, 333),
)


if __name__ == "__main__":

    rspndnt_labels = ["herself", "hsbnd"]
    day_labels = ["weekday", "holiday"]
    specs_vars = [wife_weekday_spec, wife_holiday_spec,
                  husband_weekday_spec, husband_holiday_spec]
    specs_dict = dict(
        zip(it.product(rspndnt_labels, day_labels), specs_vars))
    uf = factory.UnitsFactory()
    for k, v in specs_dict.items():
        uf.create(rspndnt_type=k[0], day_type=k[1], colspecs=v)

    d = factory.DataFactory(data="p29_3.txt", units=uf.all_units).parse()
    # print(d.head())

    #print(inspect.getmembers(checker.Checker, inspect.ismethod))
    print(checker.Checker.all([1, 70, 0, 23, 10, 132]))
