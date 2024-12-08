import datetime
import requests as req
from bs4 import BeautifulSoup as bs

# 健保VPN
url = "https://medvpn.nhi.gov.tw/iwse5000/IWSE5001S01.aspx?sc=1"

# 首頁網址
prefix = 'https://medvpn.nhi.gov.tw'

# 用 requests 的 get 方法把網頁抓下來

res = req.get(url)
# 指定 lxml 作為解析器
soup = bs(res.text, "lxml")

# 取得昨天的日期
tonow = datetime.datetime.now()
year=tonow.year-1911
month=tonow.month
date=tonow.day-1
yesterday=str(year)+"."+str(month).zfill(2)+"."+str(date)

# line權杖
token = 'YOUR_TOKEN'

# 顯示連結列表
for a in soup.select('div.in-box li'): 
    date=a.get_text().split('/')[1][1:10]    
    if date==yesterday:
        headers = {
                    "Authorization": "Bearer " + token,
                    "Content-Type": "application/x-www-form-urlencoded"
            }
        params = {"message": date+"昨日VPN業務公告:\n" + a.get_text()}
        r = req.post("https://notify-api.line.me/api/notify",
                    headers=headers, params=params)
        print(r.status_code)  #200
