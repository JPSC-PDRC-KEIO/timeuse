
from numpy import NaN


def to_minutes(hours_minutes: str) -> int:
    """
    時間のデータを分単位に変更する

    :param hour_minutes: 3桁の文字列で上2桁が時間を下1桁が分（10分単位）を示す．無配偶の夫などの非該当項目は空白が入っている．
    :type hour_minutes: str
    :return: 数値に直した分を返す.無回答，非該当は0
    :rtype: int
    """
    assert len(hours_minutes) == 3, "時間のデータが3桁ではありません"
    ms = NaN
    if hours_minutes == "999":
        ms = 0
    elif hours_minutes == "   ":
        ms = 0
    else:
        h = int(hours_minutes[:2])
        m = int(hours_minutes[2])
        ms = h*60 + m*10

    return ms


def display_hours_minutes(arg):
    # 何時何分表示”00:00”に変更
    h_m = ([str(int(x[0]) * 10 + int(x[1])) + ':' + x[2] + '0'
            if x != '999' else "0:00" for x in arg])
    return h_m
