from html.parser import HTMLParser

class 掠資料表(HTMLParser):
	def __init__(self):
		super(掠資料表, self).__init__()
		self.資料 = []
		self.愛記錄 = False
	def handle_starttag(self, tag, attrs):
		if tag == "tr":
			self.資料.append([])
		elif tag == "td":
			self.愛記錄 = True
	def handle_endtag(self, tag):
		if tag == "td":
			self.愛記錄 = False
	def handle_data(self, data):
		if self.愛記錄:
			self.資料[-1].append(data.strip())

