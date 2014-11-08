##選委會資料處理
配合監票者聯盟現有資料庫`db_data.html`
佮選委會的抽籤號碼配對

這馬只處理資料分欄的檔案!!!

###安裝
```bash
sudo pip3 install xlrd
sudo apt-get install poppler-utils #裝ubuntu的pdftotext套件
```
###執行
```bash
find .. -name '*里長*df'-exec pdftotext -layout {} \; #先共pdf轉txt
python3 程式/走里長.py
```
結果佇`結果檔案.txt`
