配合監票者聯盟現有資料庫`db_data.html`
佮選委會的抽籤號碼配對

先共pdf轉txt
```bash
sudo apt-get install poppler-utils #裝ubuntu的pdftotext套件
find .. -name '*里長*df'-exec pdftotext -layout {} \;
python3 程式/走里長.py
```
結果佇`結果檔案.txt`
