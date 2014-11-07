import xlrd
import os

class 讀檔案:
	全部縣市 = ["臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市",
		"基隆市", "新竹市", "嘉義市",
		"新竹縣", "苗栗縣", "彰化縣", "南投縣", "雲林縣", "嘉義縣", "屏東縣",
		"宜蘭縣", "花蓮縣", "臺東縣", "澎湖縣", "金門縣", "連江縣"]
	def 揣出全部的檔案(self, 所在):
		全部檔案 = []
		for 這个所在, 資料夾名, 檔名 in os.walk(所在):
			for 檔 in 檔名:
				全部檔案.append(os.path.join(這个所在, 檔))
		return 全部檔案
	def 讀第一頁出來(self, 檔名):
		表格檔 = xlrd.open_workbook(檔名)
		表名 = 表格檔.sheet_names()
		if len(表名) > 1:
			raise RuntimeError('表超過1頁以上')
		表格 = 表格檔.sheet_by_name(表名[0])
		全部資料 = []
		for 第幾逝 in range(表格.nrows):
			一逝資料 = []
			for 表資料 in 表格.row_values(第幾逝):
				if isinstance(表資料, float):
					一逝資料.append(str(int(表資料)).strip())
				else:
					一逝資料.append(str(表資料).strip())
				全部資料.append(一逝資料)
		return 全部資料
	def 讀文字檔(self, 檔名):
		上長列 = 0
		for 一逝資料 in open(檔名):
			割開 = 一逝資料.split()
			if len(割開) > 上長列:
				上長列 = len(割開)
		全部資料 = []
		for 一逝資料 in open(檔名):
			全部資料.append(一逝資料.split())
			while len(全部資料[-1]) < 上長列:
				全部資料[-1].append('')
		return 全部資料
