import inspect
from typing import List
import numpy as np


class Checker:
    names = locals().keys()

    def commute(cls):
        pass

    @staticmethod
    def has_over24(minutes_list: List[int]) -> bool:
        """各項目に24時間以上の値が記入されているケースを検出

        :param minutes_list: 各項目の時間を格納したリスト（分表記）
        :type minutes_list: List[int]
        :return: 24時間以上の項目が1つでもあればTrue
        :rtype: bool
        """
        caution = False
        minutes_array = np.array(minutes_list)
        # 999（無回答）を0に変換
        minutes_array[minutes_array == 999*60] = 0
        if np.sometrue(minutes_array >= 24*60):
            caution = True
        return caution

    @staticmethod
    def all_items_zero(minutes_list: List[int]) -> bool:
        """すべての項目が0になっているケースを検出

        :param minutes_list: 各項目の時間を格納したリスト（分表記）
        :type minutes_list: List[int]
        :return: すべての項目が0になっていればTrue
        :rtype: bool
        """
        caution = False
        minutes_array = np.array(minutes_list)
        if np.all(minutes_array == 0):
            caution = True
        return caution

    @staticmethod
    def total_not_24(minutes_list: List[int]) -> bool:
        """項目の合計が24時間にならないケースを検出

        :param minutes_list: 各項目の時間を格納したリスト（分表記）
        :type minutes_list: List[int]
        :return: 合計が24時間になっていなかったらTrue
        :rtype: bool
        """
        caution = False
        if sum(minutes_list) != 24*60:
            caution = True
        return caution

    @staticmethod
    def total_over_26(minuites_list: List[int]) -> bool:
        """項目の合計が26時間を超えるケースを検出．この場合，時間調整をしない．

        :param minuites_list: 各項目の時間を格納したリスト（分表記）
        :type minuites_list: List[int]
        :return: 合計が26時間より大であればTrue
        :rtype: bool
        """
        caution = False
        if sum(minuites_list) > 26*60:
            caution = True
        return caution

    @staticmethod
    def total_under_22(minuites_list: List[int]) -> bool:
        """項目の合計が22時間未満のケースを検出．この場合，時間調整をしない．

        :param minuites_list: 各項目の時間を格納したリスト（分表記）
        :type minuites_list: List[int]
        :return: 合計が22時間以下であればTrue
        :rtype: bool
        """
        caution = False
        if sum(minuites_list) < 22*60:
            caution = True
        return caution

    @classmethod
    def all(cls, minutes_list: List[int]) -> dict:
        rslts = {}
        functions = dict(inspect.getmembers(cls, inspect.isfunction))
        valid_order_func_names = filter(
            lambda key: key in functions, cls.names)
        for func_name in valid_order_func_names:
            local_vars = locals()
            #print("<local:", local_vars, ":local>")
            rslt = functions[func_name](minutes_list)
            rslts[func_name] = rslt
            #func_params = inspect.signature(functions[func_name]).parameters
            #passing_args = {p: local_vars[p] for p in func_params}
        return rslts
