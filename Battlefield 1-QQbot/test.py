import requests
from lxml import etree
import re
import Mysql_Insert

def get_Weapons(wuqi: str) -> str:
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
        WeaponsName = [x.strip() for x in name if x.strip() != ''][a]
        KILLS = xpath.xpath("//td[@class='stat detailed'][1]/div[@class='value']/text()")[a]
        KPM = xpath.xpath("//td[@class='stat detailed'][2]/div[@class='value']/text()")[a]
        Accuracy = xpath.xpath("//td[@class='stat detailed'][3]/div[@class='value']/text()")[b]
        Headshots = xpath.xpath("//tbody/tr/td[@class='stat'][1]/text()")[a]
        c = 12
        d = 1
        name1 = xpath.xpath("//tbody/tr/td[@class='details']//div[@class='title']//text()")
        WeaponsName1 = [x.strip() for x in name1 if x.strip() != ''][c]
        KILLS1 = xpath.xpath("//td[@class='stat detailed'][1]/div[@class='value']/text()")[c]
        KPM1 = xpath.xpath("//td[@class='stat detailed'][2]/div[@class='value']/text()")[c]
        Accuracy1 = xpath.xpath("//td[@class='stat detailed'][3]/div[@class='value']/text()")[d]
        Headshots1 = xpath.xpath("//tbody/tr/td[@class='stat'][1]/text()")[c]
        e = 13
        f = 2
        name2 = xpath.xpath("//tbody/tr/td[@class='details']//div[@class='title']//text()")
        WeaponsName2 = [x.strip() for x in name2 if x.strip() != ''][e]
        KILLS2 = xpath.xpath("//td[@class='stat detailed'][1]/div[@class='value']/text()")[e]
        KPM2 = xpath.xpath("//td[@class='stat detailed'][2]/div[@class='value']/text()")[e]
        Accuracy2 = xpath.xpath("//td[@class='stat detailed'][3]/div[@class='value']/text()")[f]
        Headshots2 = xpath.xpath("//tbody/tr/td[@class='stat'][1]/text()")[e]

        Mysql_Insert.Write_Weapons(name, WeaponsName, KILLS, KPM, Accuracy, Headshots, WeaponsName1, KILLS1, KPM1, Accuracy1,
                            Headshots1, WeaponsName2, KILLS2, KPM2, Accuracy2, Headshots2)
    except:
        a = ''
        return a


