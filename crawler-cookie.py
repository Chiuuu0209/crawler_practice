# 抓取Gossiping原始碼
import urllib.request as req
def getData(url):

    # 建立request物件附加headers資訊
    # Headers 包含cookie/user-agent 去模擬使用者
    request=req.Request(url,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    })
    # 建立request物件 
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="title")
    # 尋找所有 class=title 的 div檔案

    # 如果標題沒被刪除就印出來
    for title in titles:
        if title.a != None:
            print(title.a.string)

    # 找到內文是 ‹ 上頁 的 a 標籤 抓取下一頁連結
    nextlink=root.find("a",string="‹ 上頁")
    print(nextlink)
    # <a class="btn wide" href="/bbs/Gossiping/index39109.html">‹ 上頁</a>

    return nextlink["href"]
    # /bbs/Gossiping/index39109.html
    # 回傳網址
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<5:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1