from 程式.讀檔案 import 讀檔案
import os
from 程式.分類資料 import 分類資料
from 程式.掠資料表 import 掠資料表

class 走里長():
	投票 = '里長'
	def _整理資料(self, 檔案所在):
		_讀檔案 = 讀檔案()
		_分類資料 = 分類資料()
		整理資料 = []
		全部檔名 = _讀檔案.揣出全部的檔案(檔案所在)
		for 檔名 in 全部檔名:
			if self.投票 in 檔名:
				if 檔名.endswith('.xls') or 檔名.endswith('.xlsx'):
					try:
						資料 = _讀檔案.讀第一頁出來(檔名)
						整理資料.extend(_分類資料.合資料(資料))
	# 					print((資料[-10:]))
	# 					print((整理資料[-10:]))
					except Exception as 錯誤:
						print(檔名)
						print(錯誤)
						raise
				elif 檔名.endswith('.txt'):
					try:
						資料 = _讀檔案.讀文字檔(檔名)
						if len(資料) > 3:
							整理資料.extend(_分類資料.合資料(資料))
					except Exception as 錯誤:
						print(檔名)
						print(錯誤)
						raise
		return 整理資料
	def 比對資料(self, 檔案所在, 資料):
		整理資料 = self._整理資料(檔案所在)
		_掠資料表 = 掠資料表()
		_掠資料表.feed(資料)
		候選人資料表 = _掠資料表.資料[1:]
		
		選區表 = {}
		for 候選人資料 in 候選人資料表:
			候選人編號 = 候選人資料[0]
			候選人名 = 候選人資料[1]
			選區 = self._選區正規化(候選人資料[3])
			if 選區 not in 選區表:
				選區表[選區] = []
			選區表[選區].append((候選人名, 候選人編號, []))
			
		for 選區, 名, 號次, 男女 in 整理資料:
			選區 = self._選區正規化(選區)
			擺 = 0
			for 選區表名, 選區表編號, 選區表目前資料 in 選區表[選區]:
				if 名 == 選區表名:
					選區表目前資料.append((號次, 男女))
					擺 += 1
			if 擺 == 0:
				for 選區表名, 選區表編號, 選區表目前資料 in 選區表[選區]:
					著的字 = 0
					for 字 in 名:
						if 字 in 選區表名:
							著的字 += 1
					if self._是毋是仝人(名, 選區表名):
						選區表目前資料.append((號次, 男女))
						擺 += 1
			if 擺 != 1:
				raise RuntimeError('有問題!!仝一个投票所有人仝名!!{0},{1},{2},{3}'
							.format(名, 號次, 選區, 選區表[選區]))
		配對結果 = []
		for 選區, 候選人陣列 in 選區表.items():
			for (選區表名, 選區表編號, 選區表目前資料) in 候選人陣列:
				if len(選區表目前資料) > 1:
					raise RuntimeError('有問題!!仝一个有濟人對著!!{0},{1},{2}'.format(選區, 選區表名, 選區表目前資料))
				elif len(選區表目前資料) == 1:
					配對結果.append((選區表編號, 選區表目前資料[0][0], 選區表目前資料[0][1]))
				elif len(選區表目前資料) == 0:
					print('{0}選區的{1},{}，無資料'.format(選區, 選區表編號, 選區表名))
		配對結果.sort()
		return 配對結果
	def _是毋是仝人(self, 選委會, 監票系統):
		if (選委會, 監票系統) in [('黃山田', '林三田'), ('林家珍', '陳瀛洲'), ('謝鄭阿玉', '陳美蓮')]:
			return True
		著的字 = 0
		for 字 in 監票系統:
			if 字 in 選委會:
				著的字 += 1
		if 著的字 + 著的字 >= len(監票系統):
			return True
		if 著的字 + 著的字 >= len(選委會):
			return True
# 		if 監票系統.startswith(選委會) or 監票系統.endswith(選委會):
# 			return True
# 		if 選委會.startswith(監票系統) or 選委會.endswith(監票系統):
# 			return True
		if 選委會 in 監票系統 or 監票系統 in 選委會:
			return True
		return False
	def _選區正規化(self, 選區):
		return 選區.replace('\ueebe', '舘').replace('台', '臺').replace('\ue001', '（石曹）')
	
if __name__ == '__main__':
	_比對里長 = 走里長()
	_這馬所在 = os.path.dirname(os.path.abspath(__file__))
	_檔案所在 = os.path.join(_這馬所在, '..', '2014候選人號次')
	配對結果 = _比對里長.比對資料(_檔案所在, open(os.path.join(_這馬所在, '..', 'db_data.html')).read())
	結果檔案 = open(os.path.join(_這馬所在, '..', '結果檔案.txt'), 'w')
	for 系統內人編號, 抽著號碼, 男女 in 配對結果:
		print('{0},{1},{2}'.format(系統內人編號, 抽著號碼, 男女), file=結果檔案)
