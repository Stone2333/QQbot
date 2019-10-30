import requests
from lxml import etree
import re

async def get_wuqi(wuqi: str) -> str:
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
    # return f'{wuqi}武器数据如下xxx'

async def get_zhanji(zhanji: str) -> str:
    # 爬取html
    base_url = "https://battlefieldtracker.com/bf1/search?platform=pc&name="
    url = base_url + zhanji
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
        SCORE_MIN = "分数/分钟:" + res[2]
        KD_RATIO = "K/D比:" + res[3]
        WIN_PERCENT = "胜率:" + res[4]
        KILLS_GAME = "场均击杀:" + res[5]
        KILLS_MIN = "杀敌/分钟:" + res[6]
        INFANTRY_KPM = "步兵KPM:" + res[7]
        INFANTRY_KD = "步兵KD:" + res[8]
        VEHICLE_KILLS = "载具击杀:" + res[9]
        VEHICLE_KPM = "载具KPM:" + res[10]
        SKILL = "技巧值:" + res[11]
        ACCURACY = "准度:" + res[15]
        # 存进列表
        res1 = ["\n游戏ID:" + zhanji, SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN, INFANTRY_KPM, INFANTRY_KD,
                VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY]
        # 去逗号
        res2 = (' \n'.join(res1))
        return res2
    except:
        str1 = 'ID错误或网络问题，请稍后重试'
        return str1
    # return f'{zhanji}战绩如下xxx'

async def get_zuijinzhanji(zuijinzhanji: str) -> str:
    url2 = "https://battlefieldtracker.com/bf1/profile/pc/"
    url = url2 + zuijinzhanji
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

        c = ["\n最近战绩:", "SPM:" + SPM1, "KD:" + Kd1, "Kpm:" + KPM1, "游戏时间:" + TimePlayed1,
             "\nSPM:" + SPM2, "KD:" + Kd2, "Kpm:" + KPM2, "游戏时间:" + TimePlayed2,
             "\nSPM:" + SPM3, "KD:" + Kd3, "Kpm:" + KPM3, "游戏时间:" + TimePlayed3
             ]
        res2 = (' \n'.join(c))
        return res2
    except:
        a = '无法查询到最近战绩'
        return a

    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回真实数据的天气 API，并拼接成天气预报内容
    # return f'{zuijinzhanji}最近战绩如下xxx'

async def get_fuwuqi(chafuwuqi: str) -> str:
    Server = {'ZBW': '4548409440277', 'zbw': '4548409440277'}
    if chafuwuqi in Server:
        # Server = {'ZBW': '4548409440277', 'zbw': '4548409440277', '711': '4549052410528', 'FAZE': '4617118720211',
        #           'XD233-1#': '4460849620490', 'XD233-2#': '4576102980226', 'QWQ': '4621146300215',
        #           'QVQ': '4471243610926', '0V0': '4649704670029', 'FRM5-1#': '4639825910955', 'FRM5-2#': '4570182580087',
        #           'FRM5-3#': '4624140460607', '404-1#': '4462319260673', '404-2#': '4505664220683',
        #           '404-3#': '4545127080330', 'CDN': '4614832770811', 'HENT': '4607940010117', 'KGB-1#': '4629077150013',
        #           'KGB-2#': '4623779700501'}
        try:
            base_url = "https://battlefieldtracker.com/bf1/servers/pc/" + Server[chafuwuqi]
            # url = base_url.format(url1)
            headers = {
                "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
            }
            # proxies = {
            #     'http': 'username:password@125.123.122.178:9999',
            # }
            response = requests.get(base_url, headers=headers)
            htmlContent = response.content.decode("utf-8")
            pattern = '<div class="quick-info">.*?<span class="value">(.*?)<small>(.*?)</small>'
            # 服务器人数
            html = re.findall(pattern, htmlContent, re.S)
            for val in html:
                name1 = val
            Prayers = (''.join(name1))
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
            c = ['\n服务器名称:' + Name, '\n地图:' + Maplist[Map], '\n服务器人数:' + Prayers]
            a = (''.join(c))
            return a
        except:
            # b = '\n服务器未注册、服务器不存在或网络问题\n可查询服务器列表：\nZBW，711，FAZE，XD233-1#，XD233-2#，FRM5-1#，FRM5-2#，FRM5-3#，QWQ，QVQ,0V0，404-1#，404-2#，404-3#，CDN,KGB-1#,KGB-2#\n查询格式：\n【查服务器】+空格+列表'
            b = '网络问题，未查询到服务器信息，请稍后重试'
            return b
    else:
        a = "服务器未注册,请联系管理员"
        return a
    # return f'{chafuwuqi}最近战绩如下xxx'

async def get_zaiju(zaiju: str) -> str:
    base_url = "https://battlefieldtracker.com/bf1/profile/pc/{}/vehicles"
    url = base_url.format(zaiju)
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
        d = ["\n载具名称:" + name, "击杀:" + kills, "KPM:" + kpm, "击毁载具:" + Destroyed,
             "载具名称:" + name1, "击杀:" + kills1, "KPM:" + kpm1, "击毁载具:" + Destroyed1,
             "载具名称:" + name2, "击杀:" + kills2, "KPM:" + kpm2, "击毁载具:" + Destroyed2,
             ]
        res2 = (' \n'.join(d))
        return res2
    except:
        c = 'ID错误或网络问题，请稍后重试'
        return c

    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回真实数据的天气 API，并拼接成天气预报内容
    # return f'{chazaiju}最近战绩如下xxx'

#
# async def get_weather_of_city(city: str) -> str:
#     return f'{city}天气如下xxx'