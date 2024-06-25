import unittest

from 流年流月 import 十神, 流年流月处理
from 阴阳五行 import 天干, 五行, 相生关系, 五行处理

# 测试代码
class Test五行处理(unittest.TestCase):
    def test_相生关系判断(self):
        self.assertEqual(五行处理.相生关系判断(五行.金, 五行.金), 相生关系.同我)
        self.assertEqual(五行处理.相生关系判断(五行.木, 五行.木), 相生关系.同我)
        self.assertEqual(五行处理.相生关系判断(五行.水, 五行.水), 相生关系.同我)
        self.assertEqual(五行处理.相生关系判断(五行.火, 五行.火), 相生关系.同我)
        self.assertEqual(五行处理.相生关系判断(五行.土, 五行.土), 相生关系.同我)
        self.assertEqual(五行处理.相生关系判断(五行.金, 五行.水), 相生关系.我生)
        self.assertEqual(五行处理.相生关系判断(五行.木, 五行.火), 相生关系.我生)
        self.assertEqual(五行处理.相生关系判断(五行.水, 五行.木), 相生关系.我生)
        self.assertEqual(五行处理.相生关系判断(五行.火, 五行.土), 相生关系.我生)
        self.assertEqual(五行处理.相生关系判断(五行.土, 五行.金), 相生关系.我生)
        self.assertEqual(五行处理.相生关系判断(五行.水, 五行.金), 相生关系.生我)
        self.assertEqual(五行处理.相生关系判断(五行.火, 五行.木), 相生关系.生我)
        self.assertEqual(五行处理.相生关系判断(五行.木, 五行.水), 相生关系.生我)
        self.assertEqual(五行处理.相生关系判断(五行.土, 五行.火), 相生关系.生我)
        self.assertEqual(五行处理.相生关系判断(五行.金, 五行.土), 相生关系.生我)
        self.assertEqual(五行处理.相生关系判断(五行.金, 五行.木), 相生关系.我克)
        self.assertEqual(五行处理.相生关系判断(五行.水, 五行.火), 相生关系.我克)
        self.assertEqual(五行处理.相生关系判断(五行.木, 五行.土), 相生关系.我克)
        self.assertEqual(五行处理.相生关系判断(五行.火, 五行.金), 相生关系.我克)
        self.assertEqual(五行处理.相生关系判断(五行.土, 五行.水), 相生关系.我克)
        self.assertEqual(五行处理.相生关系判断(五行.木, 五行.金), 相生关系.克我)
        self.assertEqual(五行处理.相生关系判断(五行.火, 五行.水), 相生关系.克我)
        self.assertEqual(五行处理.相生关系判断(五行.土, 五行.木), 相生关系.克我)
        self.assertEqual(五行处理.相生关系判断(五行.金, 五行.火), 相生关系.克我)
        self.assertEqual(五行处理.相生关系判断(五行.水, 五行.土), 相生关系.克我)


class Test流年处理(unittest.TestCase):

    def test_流年运势计算(self):
        阳木 = 天干.get("甲")
        阴水 = 天干.get("癸")
        self.assertEqual(流年流月处理.流年运势计算(阴水, 阳木), 十神.伤官)

if __name__ == '__main__':
    unittest.main()