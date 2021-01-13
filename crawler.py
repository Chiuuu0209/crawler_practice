# 抓取c_chat原始碼
import urllib.request as req
# 建立request物件附加headers資訊
url="https://www.ptt.cc/bbs/C_Chat/index.html"
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

# print(data)
# 抓取原始碼
import bs4
root=bs4.BeautifulSoup(data,"html.parser")

# print(root.title)
# <title>看板 C_Chat 文章列表 - 批踢踢實業坊</title>

# print(root.title.string)
# 看板 C_Chat 文章列表 - 批踢踢實業坊

titles=root.find_all("div",class_="title")

for title in titles:
    if title.a != None:
        print(title.a.string)
# print(titles)