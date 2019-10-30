import requests
from lxml import etree
import re

async def get_Weapons(wuqi: str) -> str:
    base_url = "https://battlefieldtracker.com/bf1/profile/pc/{}/weapons"
    url = base_url.format(wuqi)
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    # proxies = {
    #     'http': 'username:password@125.123.122.178:9999',
    # }
    response = requests.get(url, headers=headers)
    htmlContent = response.content.decode("utf-8")
    # 2.将html解析成一个xpath对象
    xpath = etree.HTML(htmlContent)
    # 过滤网页
    a = 11
    b = 0
    try:
        name = xpath.xpath("//tbody/tr/td[@class='details']//div[@class='title']//text()")
        name = [x.strip() for x in name if x.strip() != ''][a]
        kills = xpath.xpath("//td[@class='stat detailed'][1]/div[@class='value']/text()")[a]
        kpm = xpath.xpath("//td[@class='stat detailed'][2]/div[@class='value']/text()")[a]
        Accuracy = xpath.xpath("//td[@class='stat detailed'][3]/div[@class='value']/text()")[b]
        Headshots = xpath.xpath("//tbody/tr/td[@class='stat'][1]/text()")[a]
        c = 12
        d = 1
        name1 = xpath.xpath("//tbody/tr/td[@class='details']//div[@class='title']//text()")
        name1 = [x.strip() for x in name1 if x.strip() != ''][c]
        kills1 = xpath.xpath("//td[@class='stat detailed'][1]/div[@class='value']/text()")[c]
        kpm1 = xpath.xpath("//td[@class='stat detailed'][2]/div[@class='value']/text()")[c]
        Accuracy1 = xpath.xpath("//td[@class='stat detailed'][3]/div[@class='value']/text()")[d]
        Headshots1 = xpath.xpath("//tbody/tr/td[@class='stat'][1]/text()")[c]
        e = 13
        f = 2
        name2 = xpath.xpath("//tbody/tr/td[@class='details']//div[@class='title']//text()")
        name2 = [x.strip() for x in name2 if x.strip() != ''][e]
        kills2 = xpath.xpath("//td[@class='stat detailed'][1]/div[@class='value']/text()")[e]
        kpm2 = xpath.xpath("//td[@class='stat detailed'][2]/div[@class='value']/text()")[e]
        Accuracy2 = xpath.xpath("//td[@class='stat detailed'][3]/div[@class='value']/text()")[f]
        Headshots2 = xpath.xpath("//tbody/tr/td[@class='stat'][1]/text()")[e]

        c = ["\n武器名称:" + name, "击杀:" + kills, "Kpm:" + kpm, "准度:" + Accuracy, "爆头击杀:" + Headshots,
             "武器名称:" + name1, "击杀:" + kills1, "Kpm:" + kpm1, "准度:" + Accuracy1, "爆头击杀:" + Headshots1,
             "武器名称:" + name2, "击杀:" + kills2, "Kpm:" + kpm2, "准度:" + Accuracy2, "爆头击杀:" + Headshots2,
             ]
        res2 = (' \n'.join(c))
        return res2
    except:
        a = 'ID错误或网络问题，请稍后重试'
        return a
    # return f'{Weapons}武器数据如下xxx'