from 程式.讀檔案 import 讀檔案
import os
from 程式.分類資料 import 分類資料

if __name__ == '__main__':
	這馬所在 = os.path.dirname(os.path.abspath(__file__))
	投票='里長'
	檔案所在 = os.path.join(這馬所在, '..', '2014候選人號次')
	
	_讀檔案 = 讀檔案()
	_分類資料=分類資料()
	全部檔名=_讀檔案.揣出全部的檔案(檔案所在)
	for 檔名 in 全部檔名:
		if 投票 in 檔名 or 檔名 in ['東區.xls','西區.xls']:
			if 檔名.endswith('.xls') or 檔名.endswith('.xlsx'):
				try:
					資料=_讀檔案.讀第一頁出來(檔名)
					整理資料=_分類資料.合資料(資料)
# 					print((資料[-10:]))
# 					print((整理資料[-10:]))
				except Exception as 錯誤:
					print(檔名)
					print(錯誤)
# 					raise
# 				break
