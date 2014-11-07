import unittest
from 程式.走里長 import 走里長

class 走里長試驗(unittest.TestCase):
	def setUp(self):
		self.走里長 = 走里長()
		
	def test_人名相倚(self):
		self.assertEqual(self.走里長._是毋是仝人('魏文賢', '魏文贀'), True)
		self.assertEqual(self.走里長._是毋是仝人('張小燕\nMurinu．Paibulungu', '張小燕'), True)
		self.assertEqual(self.走里長._是毋是仝人('拉瑪達‧伊斯瑪哈善\nLamata‧Ismahasan', '拉瑪達‧伊斯瑪哈善'), True)
		self.assertEqual(self.走里長._是毋是仝人('高文生\nRaera Kuljelje', '高文生（Raera．Kuljelje）'), True)
		self.assertEqual(self.走里長._是毋是仝人('修一', '（？）修一'), True)
		
	def test_人名無相倚(self):
		self.assertEqual(self.走里長._是毋是仝人('選委會', '監票系統'), False)
		self.assertEqual(self.走里長._是毋是仝人('選委會', '監票系統'), False)
		self.assertEqual(self.走里長._是毋是仝人('選委會', '監票系統'), False)
		
	def test_選委會資料無一致(self):
		self.assertEqual(self.走里長._是毋是仝人('林三田', '黃山田'), False)
		self.assertEqual(self.走里長._是毋是仝人('黃山田', '林三田'), True)
		self.assertEqual(self.走里長._是毋是仝人('陳瀛洲', '林家珍'), False)
		self.assertEqual(self.走里長._是毋是仝人('林家珍', '陳瀛洲'), True)
		