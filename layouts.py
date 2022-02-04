from typing import Literal, List
from pydantic import BaseModel, Field, validator


class HoursColSpecs(BaseModel):
    """[summary]
    各項目（通勤，仕事，etc.）について固定長データの位置
    """
    commute: tuple[int, int]
    work: tuple[int, int]
    study: tuple[int, int]
    housework: tuple[int, int]
    hobby: tuple[int, int]
    sleep: tuple[int, int]


class ResponseUnitLayout(BaseModel):
    """[summary]
    データの種類（本人・夫と平日・休日）と固定長の情報をセットにしたもの
    """
    rspndnt_type: Literal["herself", "hsbnd"]
    day_type: Literal["weekday", "holiday"]
    hours: HoursColSpecs


class ResponseAllUnitsLayout(BaseModel):
    """[summary]
    対象者のIDと4種のデータセット（本人・夫 X 平日・休日）の組み合わせ.
    すべて固定長の情報.
    """
    id: tuple[int, int] = (0, 4)
    units: List[ResponseUnitLayout] = []
    col_specs: list[tuple] = []
    var_labels: list[str] = []
    rspndnt_labels: list[str] = []
    day_labels: list[str] = []
    has_id: bool = False

    @validator('units')
    def check_units_len(cls, units):
        assert len(units) <= 4,  "5個以上の情報がunitsに入っています"

    @property
    def col_specs_id(self) -> list[tuple]:
        assert not self.has_id, "すでにIDがspecに設定されています"
        self.has_id = True
        s = self.col_specs.copy()
        s.insert(0, self.id)
        return s
