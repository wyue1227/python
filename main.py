from enum import Enum

class 相生关系(Enum):
    克我 = 1
    生我 = 2
    同我 = 3
    我生 = 4
    我克 = 5


class 五行(Enum):
    金 = 1
    木 = 2
    水 = 3
    火 = 4
    土 = 5


class 五行处理:

    相生 = {
        五行.金: 五行.水,
        五行.木: 五行.火,
        五行.水: 五行.木,
        五行.火: 五行.土,
        五行.土: 五行.金
    }

    相克 = {
        五行.金: 五行.木,
        五行.水: 五行.火,
        五行.木: 五行.土,
        五行.火: 五行.金,
        五行.土: 五行.水
    }

    @classmethod
    def 相生关系判断(self, 天干五行: '五行', 流年五行: '五行') -> 相生关系:
        if 天干五行 == 流年五行:
            return 相生关系.同我
        elif self.相生.get(天干五行) == 流年五行:
            return 相生关系.我生
        elif self.相生.get(流年五行) == 天干五行:
            return 相生关系.生我
        elif self.相克.get(天干五行) == 流年五行:
            return 相生关系.我克
        else:
            return 相生关系.克我


class 阴阳(Enum):
    阴 = 1
    阳 = 2

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


class 天干:
    
    def __init__(self, 五行对象: 五行, 阴阳对象: 阴阳) -> None:
        self.五行对象 = 五行对象
        self.阴阳对象 = 阴阳对象


class 八字:
        def __init__(self, 天干对象: 天干) -> None:
            self.天干对象 = 天干对象

class 流年处理:

    @classmethod
    def 流年运势计算(self, 日主天干: 天干, 流年天干: 天干) -> 十神:
        关系 = 五行处理.相生关系判断(流年天干.五行对象, 日主天干.五行对象)
        if 关系 == 相生关系.克我:
            if 流年天干.阴阳对象 == 日主天干.阴阳对象:
                return 十神.七杀
            else:
                return 十神.正官
        elif 关系 == 相生关系.生我:
            if 流年天干.阴阳对象 == 日主天干.阴阳对象:
                return 十神.偏印
            else:
                return 十神.正印
        elif 关系 == 相生关系.同我:
            if 流年天干.阴阳对象 == 日主天干.阴阳对象:
                return 十神.比肩
            else:
                return 十神.劫财
        elif 关系 == 相生关系.我生:
            if 流年天干.阴阳对象 == 日主天干.阴阳对象:
                return 十神.食神
            else:
                return 十神.伤官
        else:
            # 关系 == 相生关系.我克
            if 流年天干.阴阳对象 == 日主天干.阴阳对象:
                return 十神.偏财
            else:
                return 十神.正财