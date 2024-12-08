import datetime
import requests as req
from bs4 import BeautifulSoup as bs

# 國建署官網
url = "https://www.hpa.gov.tw/Home/Index.aspx"

# 首頁網址
prefix = 'https://www.hpa.gov.tw/'

# 用 requests 的 get 方法把網頁抓下來
res = req.get(url)

# 指定 lxml 作為解析器
soup = bs(res.text, "lxml")

# 取得昨天的日期
tonow = datetime.datetime.now()
year=tonow.year-1911
month=tonow.month
date=tonow.day-10
yesterday=str(year)+"年"+str(month).zfill(2)+"月"+str(date).zfill(2)+"日"
token = 'YOUR_TOKEN'

# 顯示連結列表
for a in soup.select('div.newsList.bulletinBlock li'): 
#找到符合昨天日期的公告
    if a.text[0:10]==yesterday:
        headers = {
                    "Authorization": "Bearer " + token,
                    "Content-Type": "application/x-www-form-urlencoded"
            }
        params = {"message": "昨日國建署公告:\n"+(a.text)+(prefix+a.a.get("href"))}
        r = req.post("https://notify-api.line.me/api/notify",
                    headers=headers, params=params)