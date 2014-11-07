from 程式.分類資料 import 分類資料
import unittest
import os
from 程式.讀檔案 import 讀檔案

class 分類資料試驗(unittest.TestCase):
	def setUp(self):
		self.分類資料 = 分類資料()
		self.這馬所在 = os.path.dirname(os.path.abspath(__file__))
		self.讀檔案 = 讀檔案()
	def test_合法里長選區(self):
		合法選區 = ['金門縣烏坵鄉小坵村', '基隆市中正區新富里', '嘉義縣阿里山鄉茶山村', '宜蘭縣南澳鄉澳花村',
			'宜蘭縣南澳鄉澳花村', '澎湖縣七美鄉南港村', '高雄市那瑪夏區南沙魯里', '連江縣東引鄉樂華村', '屏東縣牡丹鄉高士村',
			'桃園市復興區羅浮里', '新竹縣五峰鄉桃山村', '新竹市東區關新里', '新竹市北區中雅里', '新竹市香山區南港里',
			'花蓮縣卓溪鄉卓清村', '苗栗縣泰安鄉士林村', ]
		for 選區 in 合法選區:
			self.assertEqual(self.分類資料._判斷是毋是里長選區(選區), True)
	def test_判斷是毋是里長選區(self):
		違法選區 = ['金門縣烏坵鄉', '1', '2.3', '男', ]
		for 選區 in 違法選區:
			self.assertEqual(self.分類資料._判斷是毋是里長選區(選區), False)
	def test_揣出選區(self):
		檔名 = os.path.join(self.這馬所在, '..', '2014候選人號次', '21金門縣－到齊', '金門縣村里長.xls')
		資料 = self.讀檔案.讀第一頁出來(檔名)
		self.assertEqual(self.分類資料._這欄是毋是里長選區(資料, 0), True)
	def test_名毋是號次(self):
		檔名 = os.path.join(self.這馬所在, '..', '2014候選人號次', '21金門縣－到齊', '金門縣村里長.xls')
		資料 = self.讀檔案.讀第一頁出來(檔名)
		self.assertEqual(self.分類資料._這欄是毋是抽籤號次(資料, 2), False)
	def test_揣出著的號次(self):
		檔名 = os.path.join(self.這馬所在, '..', '2014候選人號次', '21金門縣－到齊', '金門縣村里長.xls')
		資料 = self.讀檔案.讀第一頁出來(檔名)
		self.assertEqual(self.分類資料._這欄是毋是抽籤號次(資料, 6), True)
	def test_揣出號次(self):
		檔名 = os.path.join(self.這馬所在, '..', '2014候選人號次', '21金門縣－到齊', '金門縣村里長.xls')
		資料 = self.讀檔案.讀第一頁出來(檔名)
		self.assertEqual(self.分類資料._抽籤號次是佗幾个(資料), [6])
	def test_嘉義縣村里長揣出號次(self):
		檔名 = os.path.join(self.這馬所在, '..', '2014候選人號次', '15嘉義縣－到齊', '嘉義縣村里長.xls')
		資料 = self.讀檔案.讀第一頁出來(檔名)
		self.assertEqual(self.分類資料._這欄是毋是抽籤號次(資料, 4), True)
		self.assertEqual(self.分類資料._抽籤號次是佗幾个(資料), [4])
	def test_基隆村里長揣出號次(self):
		檔名 = os.path.join(self.這馬所在, '..', '2014候選人號次', '07基隆市－到齊', '里長.xls')
		資料 = self.讀檔案.讀第一頁出來(檔名)
		self.assertEqual(len(self.分類資料.合資料(資料)), 279)
