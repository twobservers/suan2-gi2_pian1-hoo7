import re
import itertools

class 分類資料:
	選區判斷 = re.compile('.{2}[縣市].{1,4}[鄉鎮市區].{1,4}[村里]')
	臺北選區判斷 = re.compile('.{1,4}區.{1,4}[村里]')
	臺北里長候選人判斷 = re.compile('\({0,1}(\d+)\){0,1}(.*)')
	def 合資料(self, 資料):
		選區 = self._里長選區是佗幾个(資料)
		名 = self._里長名是佗幾个(資料)
		號次 = self._抽籤號次是佗幾个(資料)
		男女 = self._男女是佗幾个(資料)
		if len(set(選區) | set(名) | set(號次) | set(男女)) != len(選區) + len(名) + len(號次) + len(男女):
			raise RuntimeError('選擇有重複!!{0},{1},{2},{3}'.format(
					(選區), (名), (號次), (男女)))
		if len(選區) > 0 and len(選區) == len(名) and len(選區) == len(號次) and\
				(len(選區) == len(男女) or len(男女) == 0):
			pass
		elif len(選區) == 0 and len(選區) == len(名) and len(選區) == len(號次) and\
				len(男女) == 0:
			臺北選區 = self._臺北里長選區是佗幾个(資料)
			if len(臺北選區) == 1:
				return self._提出臺北選區資料(資料, 臺北選區[0])
			raise RuntimeError('干焦毋是臺北選區!!{0},{1},{2},{3}'.format(
					(選區), (名), (號次), (男女)))
		else:
			raise RuntimeError('選著的數量無仝!!{0},{1},{2},{3}'.format(
					(選區), (名), (號次), (男女)))
		全部資料 = []
		for 選區欄, 名欄, 號次欄, 男女欄 in itertools.zip_longest(選區, 名, 號次, 男女):
			全部資料.extend(self._提出資料(資料, 選區欄, 名欄, 號次欄, 男女欄))
		全部資料.sort()
		return 全部資料
	def _提出資料(self, 資料, 選區欄, 名欄, 號次欄, 男女欄):
		資料整理 = set()
		for 第幾筆, 一筆 in enumerate(資料):
			if self._判斷是毋是里長選區(一筆[選區欄]):
				選區 = 一筆[選區欄]
				名 = 一筆[名欄]
				if 男女欄:
					男女 = 一筆[男女欄]
				else:
					男女 = 'False'
				if self._判斷是毋是抽籤號次(一筆[號次欄]):
					號次 = self._號次轉數字(一筆[號次欄])
				elif 一筆[號次欄].strip("'") == '':
					號次 = -1
				elif 一筆[號次欄].strip() == '死亡':
					號次 = -1
				else:
					raise RuntimeError('號次有問題!!{0},{1}'.format(名, 一筆[號次欄]))
				if 號次 == -1 and self._判斷是毋是抽籤號次(名):  # 臺東縣有原住民名
					號次 = self._號次轉數字(名)
					名 = ''.join(itertools.chain(資料[第幾筆 - 1], 資料[第幾筆 + 1]))
				資料整理.add((選區, 名, 號次, 男女))
		return list(資料整理)
	def _提出臺北選區資料(self, 資料, 臺北選區):
		資料整理 = set()
		for 一筆 in 資料:
			里 = 一筆[臺北選區]
			if self._判斷是毋是臺北里長選區(里):
				for 所在 in range(len(一筆)):
					if 所在 != 臺北選區:
						號碼, 人名 = self._臺北里長候選人(一筆[所在])
						if 號碼 != None:
							資料整理.add(('臺北市' + 里, 人名, 號碼, False))
		return 資料整理
	def _判斷是毋是里長選區(self, 選區):
		return self.選區判斷.search(選區.strip()) != None
	def _這欄是毋是里長選區(self, 資料, 欄號):
		全部 = 0
		里長 = 0
		for 一筆 in 資料:
			if self._判斷是毋是里長選區(一筆[欄號]):
				里長 += 1
			全部 += 1
		return 里長 >= 全部 * 0.3
	def _里長選區是佗幾个(self, 資料):
		可能選擇 = []
		for 欄號 in range(len(資料[0])):
			if self._這欄是毋是里長選區(資料, 欄號):
				可能選擇.append(欄號)
		return 可能選擇
	def _臺北里長候選人(self, 名):
		結果 = self.臺北里長候選人判斷.search(名)
		if 結果 == None:
			return None, None
		return int(結果.group(1)), 結果.group(2)
	def _判斷是毋是臺北里長選區(self, 選區):
		return self.臺北選區判斷.search(選區.strip()) != None
	def _這欄是毋是臺北里長選區(self, 資料, 欄號):
		全部 = 0
		里長 = 0
		for 一筆 in 資料:
			if self._判斷是毋是臺北里長選區(一筆[欄號]):
				里長 += 1
			全部 += 1
		return 里長 >= 全部 * 0.3
	def _臺北里長選區是佗幾个(self, 資料):
		可能選擇 = []
		for 欄號 in range(len(資料[0])):
			if self._這欄是毋是臺北里長選區(資料, 欄號):
				可能選擇.append(欄號)
		return 可能選擇
	def _這欄是毋是里長名(self, 資料, 欄號):
		全部 = 0
		里長 = 0
		for 一筆 in 資料:
			if len(一筆[欄號]) == 3:
				里長 += 1
			全部 += 1
		return 里長 >= 全部 * 0.3
	def _里長名是佗幾个(self, 資料):
		可能選擇 = []
		for 欄號 in range(len(資料[0])):
			if self._這欄是毋是里長名(資料, 欄號):
				可能選擇.append(欄號)
		return 可能選擇
	def _號次轉數字(self, 抽籤號次):
		return int(抽籤號次.strip("'"))
	def _判斷是毋是抽籤號次(self, 抽籤號次):
		try:
			self._號次轉數字(抽籤號次)
		except:
			return False
		else:
			return True
	def _這欄是毋是抽籤號次(self, 資料, 欄號):
		全部 = 0
		里長 = 0
		for 一筆 in 資料:
			if '登記序號' in 一筆[欄號]:
				return False
			if self._判斷是毋是抽籤號次(一筆[欄號]):
				里長 += 1
			全部 += 1
		return 里長 >= 全部 * 0.3
	def _抽籤號次是佗幾个(self, 資料):
		可能選擇 = []
		for 欄號 in range(len(資料[0])):
			if self._這欄是毋是抽籤號次(資料, 欄號):
				可能選擇.append(欄號)
		return 可能選擇
	def _這欄是毋是男女(self, 資料, 欄號):
		全部 = 0
		里長 = 0
		for 一筆 in 資料:
			if 一筆[欄號] in ['男', '女']:
				里長 += 1
			全部 += 1
		return 里長 >= 全部 * 0.3
	def _男女是佗幾个(self, 資料):
		可能選擇 = []
		for 欄號 in range(len(資料[0])):
			if self._這欄是毋是男女(資料, 欄號):
				可能選擇.append(欄號)
		return 可能選擇
	
