import requests
from lxml import etree
import re


async def get_Vehicles(Query_Vehicles: str) -> str:
    url = "https://battlefieldtracker.com/bf1/profile/pc/{}/vehicles"
    url_join = url.format(Query_Vehicles)
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    # proxies = {
    #     'http': 'username:password@125.123.122.178:9999',
    # }
    response = requests.get(url_join, headers=headers)
    htmlContent = response.content.decode("utf-8")
    xpath = etree.HTML(htmlContent)
    # 从每个数据标签中找出载具的信息
    a = 0
    try:
        name = xpath.xpath("//td[@class='details']/div[@class='title']/text()")[a]
        name_1 = name.replace("\n", "")
        name_2 = name_1.replace("\r", "")
        kills = xpath.xpath("//td[@class='stat detailed'][1]/div[@class='value']/text()")[a]
        kpm = xpath.xpath("//td[@class='stat detailed'][2]/div[@class='value']/text()")[a]
        Destroyed = xpath.xpath("//td[@class='stat'][1]/text()")[a]

        b = 1
        name1 = xpath.xpath("//td[@class='details']/div[@class='title']/text()")[2]
        name1_1 = name1.replace("\n", "")
        name1_2 = name1_1.replace("\r", "")
        kills1 = xpath.xpath("//td[@class='stat detailed'][1]/div[@class='value']/text()")[b]
        kpm1 = xpath.xpath("//td[@class='stat detailed'][2]/div[@class='value']/text()")[b]
        Destroyed1 = xpath.xpath("//td[@class='stat'][1]/text()")[b]

        c = 2
        name2 = xpath.xpath("//td[@class='details']/div[@class='title']/text()")[4]
        name2_1 = name2.replace("\n", "")
        name2_2 = name2_1.replace("\r", "")
        kills2 = xpath.xpath("//td[@class='stat detailed'][1]/div[@class='value']/text()")[c]
        kpm2 = xpath.xpath("//td[@class='stat detailed'][2]/div[@class='value']/text()")[c]
        Destroyed2 = xpath.xpath("//td[@class='stat'][1]/text()")[c]

        Namelist = {'ASSAULT TANK ': '圣沙蒙', 'ASSAULT TRUCK ': '菊花车', 'Attack Plane ': '攻击机', 'Horse ': '马',
                    'Landship ': '巡航坦克', 'HEAVY BOMBER ': '重型轰炸机 ', 'Light Tank ': '轻型坦克', 'Heavy Tank ': '重型坦克',
                    'Stationary Weapon ': '固定武器', 'Artillery Truck ': '火炮车', 'Behemoth ': '巨兽', 'Bomber ': '轰炸机'
            , 'Boat ': '船', 'Fighter ': '战斗机'}
        name = Namelist[name_2]
        name1 = Namelist[name1_2]
        name2 = Namelist[name2_2]
        Vehicles_list = ["\n载具名称:" + name, "击杀:" + kills, "KPM:" + kpm, "击毁载具:" + Destroyed,
             "载具名称:" + name1, "击杀:" + kills1, "KPM:" + kpm1, "击毁载具:" + Destroyed1,
             "载具名称:" + name2, "击杀:" + kills2, "KPM:" + kpm2, "击毁载具:" + Destroyed2,
             ]
        Vehicles_str = (' \n'.join(Vehicles_list))
        return Vehicles_str
    except:
        error = 'ID错误或网络问题，请稍后重试'
        return error
