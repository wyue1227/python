from enum import Enum
from 阴阳五行 import 五行处理, 相生关系, 阴阳五行, 天干, 地支


class 十神(Enum):
    正官 = 1
    七杀 = 2
    正印 = 3
    偏印 = 4
    劫财 = 5
    比肩 = 6
    伤官 = 7
    食神 = 8
    正财 = 9
    偏财 = 10


class 流年:
    def __init__(self, 天干对象: 阴阳五行, 地支对象: 阴阳五行) -> None:
        self.天干对象 = 天干对象
        self.地支对象 = 地支对象

    def __str__(self) -> str:
        return f"流年(天干: {self.天干对象}, 地支: {self.地支对象})"

    def __repr__(self) -> str:
        return f"流年(天干对象={self.天干对象!r}, 地支对象={self.地支对象!r})"

class 流月:
    def __init__(self, 天干对象: 阴阳五行, 地支对象: 阴阳五行) -> None:
        self.天干对象 = 天干对象
        self.地支对象 = 地支对象

    def __str__(self) -> str:
        return f"流月(天干: {self.天干对象}, 地支: {self.地支对象})"

    def __repr__(self) -> str:
        return f"流月(天干对象={self.天干对象!r}, 地支对象={self.地支对象!r})"
    

class 流年流月处理:

    @classmethod
    def 流年运势计算(self, 日主: 阴阳五行, 流年: 阴阳五行) -> 十神:
        关系 = 五行处理.相生关系判断(日主.五行对象, 流年.五行对象)
        if 关系 == 相生关系.克我:
            if 流年.阴阳对象 == 日主.阴阳对象:
                return 十神.七杀
            else:
                return 十神.正官
        elif 关系 == 相生关系.生我:
            if 流年.阴阳对象 == 日主.阴阳对象:
                return 十神.偏印
            else:
                return 十神.正印
        elif 关系 == 相生关系.同我:
            if 流年.阴阳对象 == 日主.阴阳对象:
                return 十神.比肩
            else:
                return 十神.劫财
        elif 关系 == 相生关系.我生:
            if 流年.阴阳对象 == 日主.阴阳对象:
                return 十神.食神
            else:
                return 十神.伤官
        else:
            # 关系 == 相生关系.我克
            if 流年.阴阳对象 == 日主.阴阳对象:
                return 十神.偏财
            else:
                return 十神.正财
            
    @classmethod
    def 流年获取(self, 时间: str) -> 流年:

        # TODO 暂时写固定值，需要追加流年的真实数据获取
        流年_2024 = 流年(天干.get("甲"), 地支.get("辰"))
        return 流年_2024
    

    @classmethod
    def 流月获取(self, 时间: str) -> 流年:

        # TODO 暂时写固定值，需要追加流年的真实数据获取
        流年_2024 = 流年(天干.get("甲"), 地支.get("辰"))
        return 流年_2024