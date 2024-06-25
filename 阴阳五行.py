from enum import Enum
from dataclasses import dataclass
import csv

class 阴阳(Enum):
    阴 = 1
    阳 = 2


class 五行(Enum):
    金 = 1
    木 = 2
    水 = 3
    火 = 4
    土 = 5


@dataclass
class 阴阳五行:
    名字: str
    五行对象: 五行
    阴阳对象: 阴阳


class 相生关系(Enum):
    '''
    生克关系枚举类
    以"我"为金举例
    克我: 克制我的五行，如火克金
    生我: 孕化我的五行，如土生金
    同我: 和我相同的五行，如金同金
    我生: 我孕化的五行，如金生水
    我克: 我克制的五行，如金克木
    TODO: 五行力量强弱概念的引入(我生但生不动，我克但克不动，克我克不动，生我生不动)
    '''
    克我 = 1
    生我 = 2
    同我 = 3
    我生 = 4
    我克 = 5


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
    def 相生关系判断(self, 日主五行: 五行, 流年五行: 五行) -> 相生关系:
        if 日主五行 == 流年五行:
            return 相生关系.同我
        elif self.相生.get(日主五行) == 流年五行:
            return 相生关系.我生
        elif self.相生.get(流年五行) == 日主五行:
            return 相生关系.生我
        elif self.相克.get(日主五行) == 流年五行:
            return 相生关系.我克
        else:
            return 相生关系.克我


# 函数：转换字符串为五行枚举类
def convert_str_to_五行(value: str) -> 五行:
    try:
        return 五行[value]
    except KeyError:
        raise ValueError(f"'{value}' 不是有效的五行值")
    

# 函数：转换字符串为阴阳枚举类
def convert_str_to_阴阳(value: str) -> 阴阳:
    try:
        return 阴阳[value]
    except KeyError:
        raise ValueError(f"'{value}' 不是有效的阴阳值")


# 函数：读取 CSV 文件并转换为 DTO
def read_csv_to_dto(file_path: str) -> dict[str, 阴阳五行]:
    dtos = dict()
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            dto = 阴阳五行(
                名字 = row['名字'],
                五行对象 = convert_str_to_五行(row['五行']),
                阴阳对象 = convert_str_to_阴阳(row['阴阳'])
            )
            dtos[row['名字']] = dto
    return dtos

天干: dict[str, 阴阳五行] = read_csv_to_dto("./data/天干.csv")
地支: dict[str, 阴阳五行] = read_csv_to_dto("./data/地支.csv")