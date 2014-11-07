import re
import itertools

class 分類資料:
	選區判斷 = re.compile('.{2}[縣市].{1,4}[鄉鎮市區].{1,4}[村里]')
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
		else:
			raise RuntimeError('選著的數量無仝!!{0},{1},{2},{3}'.format(
					(選區), (名), (號次), (男女)))
		全部資料 = []
		for 選區欄, 名欄, 號次欄, 男女欄 in itertools.zip_longest(選區, 名, 號次, 男女):
			全部資料.extend(self._提出資料(資料, 選區欄, 名欄, 號次欄, 男女欄))
	def _提出資料(self, 資料, 選區欄, 名欄, 號次欄, 男女欄):
		資料整理 = []
		for 一筆 in 資料:
			if self._判斷是毋是里長選區(一筆[選區欄]):
				選區 = 一筆[選區欄]
				名 = 一筆[名欄]
				if 男女欄:
					男女 = [男女欄]
				else:
					男女 = 'False'
				if self._判斷是毋是抽籤號次(一筆[號次欄]):
					號次 = self._號次轉數字(一筆[號次欄])
				elif 一筆[號次欄].strip("'") == '':
					號次 = -1
				else:
					raise RuntimeError('號次有問題!!{0},{1}'.format(名, 一筆[號次欄]))
				資料整理.append((選區, 名, 號次, 男女))
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
	
