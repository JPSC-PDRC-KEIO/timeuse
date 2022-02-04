from email import header
import pandas as pd
from pathlib import Path
from layouts import HoursColSpecs, ResponseUnitLayout, ResponseAllUnitsLayout


class UnitsFactory:
    def __init__(self) -> None:
        self.all_units = ResponseAllUnitsLayout()

    def create(
            self,
            rspndnt_type: str,
            day_type: str,
            colspecs: HoursColSpecs) -> None:

        u = self.create_unit(rspndnt_type,
                             day_type, colspecs)
        self.register_unit(u)
        self.register_col_specs(u)
        return None

    def create_unit(self, rspndnt_type: str, day_type: str, colspecs: HoursColSpecs):
        return ResponseUnitLayout(rspndnt_type=rspndnt_type, day_type=day_type, hours=colspecs)

    def register_unit(self, unit: ResponseUnitLayout) -> None:
        self.all_units.units.append(unit)

    def register_col_specs(self, unit: ResponseUnitLayout) -> None:
        specs_dict = unit.hours.dict()
        self.all_units.col_specs.extend(list(specs_dict.values()))
        self.all_units.var_labels.extend(list(specs_dict.keys()))
        l = len(specs_dict)
        r = [unit.rspndnt_type] * l
        d = [unit.day_type] * l
        self.all_units.rspndnt_labels.extend(r)
        self.all_units.day_labels.extend(d)


class DataFactory:
    def __init__(self, data: str | Path, units: ResponseAllUnitsLayout) -> None:
        self.fixed_width_data = data
        self.units = units

    def parse(self) -> pd.DataFrame:
        col = pd.MultiIndex.from_arrays([self.units.rspndnt_labels,
                                         self.units.day_labels,
                                         self.units.var_labels],
                                        names=["rspndnt", "day", "var"])
        data = pd.read_fwf(self.fixed_width_data,
                           colspecs=self.units.col_specs_id,
                           header=None, index_col=0)
        data.index.name = "id"
        data.columns = col
        return data
