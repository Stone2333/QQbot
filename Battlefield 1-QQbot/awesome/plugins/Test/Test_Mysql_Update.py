import requests
from lxml import etree
import re
import Mysql_Update



def get_Update_Weapons(Query_Weapons: str) -> str:
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
        try:
            Mysql_Update.Update_Weapons(Query_Weapons, WeaponsName, KILLS, KPM, Accuracy, Headshots, WeaponsName1, KILLS1, KPM1, Accuracy1, Headshots1, WeaponsName2, KILLS2, KPM2, Accuracy2, Headshots2)
        except:
            print(Query_Weapons, '爬虫更新武器失败')
        print(Query_Weapons, '爬虫更新武器成功')
    except:
        error = 'ID错误或网络问题，请稍后重试'
        return error

def get_Update_Vehicles(Query_Vehicles: str) -> str:
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
        try:
            Mysql_Update.Update_Vehicles(Query_Vehicles, name, kills, kpm, Destroyed, name1, kills1, kpm1, Destroyed1, name2, kills2, kpm2, Destroyed2)
        except:
            print(Query_Vehicles, "爬虫更新载具失败")
        print(Query_Vehicles, "爬虫更新载具成功")
    except:
        error = 'ID错误或网络问题，请稍后重试'
        return error

def get_Update_Recent_Sessions(Quer_Recent_Sessions: str) -> str:
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
        try:
            Mysql_Update.Update_Recent_Sessions(Quer_Recent_Sessions, SPM1,Kd1,KPM1,TimePlayed1,SPM2,Kd2,KPM2,TimePlayed2,SPM3, Kd3, KPM3, TimePlayed3)
        except:
            print(Quer_Recent_Sessions, '爬虫更新最近战绩失败')
        print(Quer_Recent_Sessions, '爬虫更新最近战绩成功')

    except:
        error = '无法查询到最近战绩'
        return error


def get_Update_Overview(Query_Overview: str) -> str:
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
        try:
            Overview = Mysql_Update.Update_Overview(Query_Overview, SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN, INFANTRY_KPM, INFANTRY_KD, VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY)
        except:
            print(Query_Overview, "爬虫更新战绩失败")
        print(Query_Overview, '爬虫更新战绩成功')

    except:
        error = 'ID错误或网络问题，请稍后重试'
        return error


def get_Update_Servers(Quer_Servers: str) -> str:
    Server = {'ZBW': '4548409440277', 'zbw': '4548409440277', 'QWQ': '4621146300215'}
    if Quer_Servers in Server:
        # Server = {'ZBW': '4548409440277', 'zbw': '4548409440277', '711': '4549052410528', 'FAZE': '4617118720211',
        #           'XD233-1#': '4460849620490', 'XD233-2#': '4576102980226', 'QWQ': '4621146300215',
        #           'QVQ': '4471243610926', '0V0': '4649704670029', 'FRM5-1#': '4639825910955', 'FRM5-2#': '4570182580087',
        #           'FRM5-3#': '4624140460607', '404-1#': '4462319260673', '404-2#': '4505664220683',
        #           '404-3#': '4545127080330', 'CDN': '4614832770811', 'HENT': '4607940010117', 'KGB-1#': '4629077150013',
        #           'KGB-2#': '4623779700501'}
        try:
            url_join = "https://battlefieldtracker.com/bf1/servers/pc/" + Server[Quer_Servers]
            # url = base_url.format(url1)
            headers = {
                "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
            }
            # proxies = {
            #     'http': 'username:password@125.123.122.178:9999',
            # }
            response = requests.get(url_join, headers=headers)
            htmlContent = response.content.decode("utf-8")
            pattern = '<div class="quick-info">.*?<span class="value">(.*?)<small>(.*?)</small>'
            # 服务器人数
            html = re.findall(pattern, htmlContent, re.S)
            for val in html:
                Total = val
            Prayers = (''.join(Total))
            xpath = etree.HTML(htmlContent)
            Name = xpath.xpath('/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/h1/span[1]/text()')[0]
            Map = xpath.xpath('/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div/div[3]/span[2]/text()')[0]
            Maplist = {'Ballroom Blitz': '流血宴厅', 'Argonne Forest': '阿尔贡森林', 'Fao Fortress': '法欧堡', 'Suez': '苏伊士',
                       'St Quentin Scar': '圣康坦的伤痕', 'Sinai Desert': '西奈沙漠', 'Amiens': '亚眠', 'Monte Grappa': '格拉巴山',
                       "Empire's Edge": '帝国边境', 'Passchendaele': '帕斯尚尔', 'Caporetto': '波雷托', 'River Somme': '索姆河',
                       "Razor's Edge": '剃刀边缘', 'London Calling': '伦敦的呼唤', 'Heligoland Bight': '黑尔戈兰湾', 'Zeebrugge': '泽布吕赫',
                       'Cape Helles': '海丽丝岬', 'Achi Baba': '阿奇巴巴', 'Lupkow Pass': '武普库夫山口', 'Brusilov Keep': '勃鲁西洛夫关口',
                       'Gali cia': '加利西亚', 'Albion': '阿尔比恩', 'Tsaritsyn': '察里津', 'Volga River': '窝瓦河', 'Rupture': '决裂',
                       'Soissons': '苏瓦松', 'Verdun Heights': '凡尔登高地', 'Fort De Vaux': '法乌克斯要塞', 'Prise de Tahure': '攻占托尔',
                       'Nivelle Nights': '尼维尔之夜', "Giant's Shadow": '庞然暗影'}
            try:
                Mysql_Update.Update_Servers(Quer_Servers, Name, Maplist[Map], Prayers)
            except:
                print(Quer_Servers, "更新服务器信息失败")
            print(Quer_Servers, '爬虫更新服务器信息成功')
        except:
            error = '网络问题，未查询到服务器信息，请稍后重试'
            return error
    else:
        Servers_null = "服务器未注册,请联系管理员"
        return Servers_null


# if __name__=="__main__":
#     # get_Servers("ZBW")
#     get_Overview("LEONID_47")
    # get_Weapons("BF_StoneGOGOGO")
    # get_Vehicles("BF_StoneGOGOGO")
    # get_Recent_Sessions("BF_StoneGOGOGO")
