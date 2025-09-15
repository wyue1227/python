from datetime import timedelta
from datetime import date
from borax.calendars.lunardate import LunarDate

dict_list = ['大安(上上)', '留连(中)', '速喜(上)', '赤口(中下)', '小吉(中上)', '空亡(下)']
time_list = ["子时：00-01点", "丑时：01-03点", "寅时：03-05点", "卯时：05-07点", "辰时：07-09点",
             "巳时：09-11点", "午时：11-13点", "未时：13-15点", "申时：15-17点", "酉时：17-19点",
             "戌时：19-21点", "亥时：22-23点", "次日子时：23-24点"]

# s_year = int(input("请输入年："))
# s_month = int(input("请输入月："))
# s_day = int(input("请输入日："))
# s_year = 2022
# s_month = 2
# s_day = 13

def get_fortune(lunar_date: LunarDate) -> dict:
    """返回某日的农历及运势信息"""

    month = lunar_date.month
    day = lunar_date.day

    # 本月运势
    index_month = (month - 1) % 6
    result_month = dict_list[index_month]

    # 本日运势
    index_day = (index_month + day - 1) % 6
    result_day = dict_list[index_day]

    # 时辰运势
    time_fortunes = [
        f"{time_list[i]} 运势：{dict_list[(i + index_day) % 6]}"
        for i in range(12)
    ]

    return {
        "lunar": lunar_date.strftime("%G"),   # 传统农历表示，如 二零二二年正月十三
        "month_fortune": result_month,
        "day_fortune": result_day,
        "time_fortunes": time_fortunes
    }


def comp_fortune(solar: date) -> dict:
    next_solar = solar + timedelta(days=1)
    ld1 = LunarDate.from_solar(solar)
    ld2 = LunarDate.from_solar(next_solar)
    result1 = get_fortune(ld1)
    result2 = get_fortune(ld2)
    last_time_fortunes = result2["time_fortunes"][0].replace(time_list[0], time_list[-1])
    result1["time_fortunes"].append(last_time_fortunes)
    return {
        "solar": f"{solar.year}年{solar.month}月{solar.day}日",
        **result1
    }


def print_fortune(fortune: dict):
    """格式化输出运势结果"""
    print("公历：", fortune["solar"])
    print("农历：", fortune["lunar"])
    print("===================")
    print("本月运势：", fortune["month_fortune"])
    print("===================")
    print("本日运势：", fortune["day_fortune"])
    print("===================")
    for tf in fortune["time_fortunes"]:
        print(tf)


# 示例调用
if __name__ == "__main__":
    solar = date(2022, 2, 13)
    result = comp_fortune(solar)
    print_fortune(result)
