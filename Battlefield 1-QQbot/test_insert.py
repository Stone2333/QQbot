import requests
from lxml import etree
import re
import Mysql_Insert

def get_Weapons(Query_Weapons: str) -> str:
    base_url = "https://battlefieldtracker.com/bf1/profile/pc/{}/weapons"
    url = base_url.format(Query_Weapons)
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

        Mysql_Insert.Insert_weapons(Query_Weapons, WeaponsName, KILLS, KPM, Accuracy, Headshots, WeaponsName1, KILLS1, KPM1, Accuracy1, Headshots1, WeaponsName2, KILLS2, KPM2, Accuracy2, Headshots2)
    except:
        a = ''
        return a


def get_Vehicles(Query_Vehicles: str) -> str:
    base_url = "https://battlefieldtracker.com/bf1/profile/pc/{}/vehicles"
    url = base_url.format(Query_Vehicles)
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
    # 3.使用xpath对象中的xpath方法查出每个数据的标签
    # data = xpath.xpath(".//div[@class='class']")
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

        Mysql_Insert.Insert_vehicles(Query_Vehicles, name, kills, kpm, Destroyed, name1, kills1, kpm1, Destroyed1, name2, kills2, kpm2, Destroyed2)
        # d = []
        # res2 = (' \n'.join(d))
        # return res2
    except:
        c = 'ID错误或网络问题，请稍后重试'
        return c

def get_Recent_Sessions(Quer_Recent_Sessions: str) -> str:
    url2 = "https://battlefieldtracker.com/bf1/profile/pc/"
    url = url2 + Quer_Recent_Sessions
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    html = response.content.decode("utf-8")
    xpath = etree.HTML(html)
    try:
        SPM1 = xpath.xpath("//div[@class='sessions'][1]/div[@class='session-stats']/div[1]/div[1]//text()")[0]
        Kd1 = xpath.xpath(
            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]//text()")[
            0]
        KPM1 = xpath.xpath("//div[@class='sessions'][1]/div[@class='session-stats']/div[3]/div[1]//text()")[0]
        try:
            TimePlayed1 = xpath.xpath(
                "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[6]/div[1]//text()")[
                0]
        except:
            TimePlayed1 = ''
        SPM2 = xpath.xpath(
            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]//text()")[
            0]
        Kd2 = xpath.xpath(
            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]//text()")[
            0]
        KPM2 = xpath.xpath(
            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[1]//text()")[
            0]
        try:
            TimePlayed2 = xpath.xpath(
                "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[6]/div[1]//text()")[
                0]
        except:
            TimePlayed2 = ''
        SPM3 = xpath.xpath(
            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[1]/div[1]//text()")[
            0]
        Kd3 = xpath.xpath(
            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[2]/div[1]//text()")[
            0]
        KPM3 = xpath.xpath(
            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[3]/div[1]//text()")[
            0]
        try:
            TimePlayed3 = xpath.xpath(
                "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[6]/div[1]//text()")[
                0]
        except:
            TimePlayed3 = ''

        Mysql_Insert.Insert_recent_sessions(Quer_Recent_Sessions,SPM1,Kd1,KPM1,TimePlayed1,SPM2,Kd2,KPM2,TimePlayed2,SPM3, Kd3, KPM3, TimePlayed3)
    except:
        a = '无法查询到最近战绩'
        return a


def get_Overview(Query_Overview: str) -> str:
    # 爬取html
    base_url = "https://battlefieldtracker.com/bf1/search?platform=pc&name="
    url = base_url + Query_Overview
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    # proxies = {
    #     'http': 'username:password@125.123.122.178:9999',
    # }
    response = requests.get(url, headers=headers)

    html = response.content.decode("utf-8")
    # 过滤html
    pattern = '"Field":.*?,"Value":(.*?)\},\{'
    string = re.findall(pattern, html, re.S)
    # 查列表赋值给对象
    res = list(string)
    try:
        # BTRSCORE = "BTR分数:" + res[0]
        # BTR_MIN = "BTR/分钟:" + res[1]
        SCORE_MIN = res[2]
        KD_RATIO = res[3]
        WIN_PERCENT = res[4]
        KILLS_GAME = res[5]
        KILLS_MIN = res[6]
        INFANTRY_KPM = res[7]
        INFANTRY_KD = res[8]
        VEHICLE_KILLS = res[9]
        VEHICLE_KPM = res[10]
        SKILL = res[11]
        ACCURACY = res[15]
        # 存进列表
        # res1 = [Query_Overview, SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN, INFANTRY_KPM, INFANTRY_KD,VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY]
        # print(res1)
        # 去逗号
        Mysql_Insert.Insert_overview(Query_Overview, SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN, INFANTRY_KPM, INFANTRY_KD, VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY)
    except:
        str1 = 'ID错误或网络问题，请稍后重试'
        return str1


if __name__=="__main__":
    get_Overview("BF_StoneGOGOGO")
    # get_Weapons("BF_StoneGOGOGO")
    # get_Vehicles("BF_StoneGOGOGO")
    # get_Recent_Sessions("BF_StoneGOGOGO")
