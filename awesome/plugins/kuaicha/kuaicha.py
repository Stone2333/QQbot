import Mysql_Select
import data_Mysql_Insert
import requests
from lxml import etree
import re


async def kuaicha2(qq, Query_Overview: str) -> str:
    relevance = Mysql_Select.Select_Id(qq)
    if Query_Overview == '战绩':
        if relevance == ():
            return 'qq号暂未绑定游戏ID,请使用绑定关键字绑定游戏ID 绑定 XXX'
        else:
            Overview = Mysql_Select.Select_Overview(relevance[0][0])
            # 判断数据库中有没有这个ID，有则直接在数据库中查询，没有则调用爬虫爬取插入
            if Overview == []:
                # 调用爬虫爬取插入
                try:
                    data_Mysql_Insert.get_Overview(Query_Overview)
                    # 爬取完毕在数据库中查询
                    Overview = Mysql_Select.Select_Overview(relevance[0][0])
                    SCORE_MIN = "分数/分钟:" + Overview[0]
                    KD_RATIO = "K/D比:" + Overview[1]
                    WIN_PERCENT = "胜率:" + Overview[2]
                    KILLS_GAME = "场均击杀:" + Overview[3]
                    KILLS_MIN = "杀敌/分钟:" + Overview[4]
                    INFANTRY_KPM = "步兵KPM:" + Overview[5]
                    INFANTRY_KD = "步兵KD:" + Overview[6]
                    VEHICLE_KILLS = "载具击杀:" + Overview[7]
                    VEHICLE_KPM = "载具KPM:" + Overview[8]
                    SKILL = "技巧值:" + Overview[9]
                    ACCURACY = "准度:" + Overview[10]
                    Overview_list = ["\n游戏ID:" + relevance[0][0], SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN,
                                     INFANTRY_KPM,
                                     INFANTRY_KD,
                                     VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY]
                    # 去逗号
                    Overview_str = (' \n'.join(Overview_list))
                    print('这是爬虫爬取完成后查到的战绩数据')
                    return Overview_str
                except:
                    error = 'ID错误/橘子信息设置为隐私,无法查询到数据'
                    return error
            else:
                SCORE_MIN = "分数/分钟:" + Overview[0]
                KD_RATIO = "K/D比:" + Overview[1]
                WIN_PERCENT = "胜率:" + Overview[2]
                KILLS_GAME = "场均击杀:" + Overview[3]
                KILLS_MIN = "杀敌/分钟:" + Overview[4]
                INFANTRY_KPM = "步兵KPM:" + Overview[5]
                INFANTRY_KD = "步兵KD:" + Overview[6]
                VEHICLE_KILLS = "载具击杀:" + Overview[7]
                VEHICLE_KPM = "载具KPM:" + Overview[8]
                SKILL = "技巧值:" + Overview[9]
                ACCURACY = "准度:" + Overview[10]
                Overview_list = ["\n游戏ID:" + relevance[0][0], SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN, INFANTRY_KPM,INFANTRY_KD,VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY]
                Overview_str = (' \n'.join(Overview_list))
                print('这是直接查数据库查到的战绩数据')
                return Overview_str
    elif Query_Overview == '武器':

        if relevance == ():
            return 'qq号暂未绑定游戏ID,请使用绑定关键字绑定游戏ID 绑定 XXX'
        else:
            Weapons = Mysql_Select.Select_Weapons(relevance[0][0])
            if Weapons == []:
                try:
                    data_Mysql_Insert.get_Weapons(relevance[0][0])
                    Weapons = Mysql_Select.Select_Weapons(relevance[0][0])
                    name = Weapons[0]
                    kills = Weapons[1]
                    kpm = Weapons[2]
                    Accuracy = Weapons[3]
                    Headshots = Weapons[4]
                    name1 = Weapons[5]
                    kills1 = Weapons[6]
                    kpm1 = Weapons[7]
                    Accuracy1 = Weapons[8]
                    Headshots1 = Weapons[9]
                    name2 = Weapons[10]
                    kills2 = Weapons[11]
                    kpm2 = Weapons[12]
                    Accuracy2 = Weapons[13]
                    Headshots2 = Weapons[14]
                    Weapons_list = ["\n烧火棍名称:" + name, "击毙:" + kills, "每分钟得分:" + kpm, "准度:" + Accuracy,
                                    "爆头击毙:" + Headshots,
                                    "烧火棍名称:" + name1, "击毙:" + kills1, "每分钟得分:" + kpm1, "准度:" + Accuracy1,
                                    "爆头击毙:" + Headshots1,
                                    "烧火棍名称:" + name2, "击毙:" + kills2, "每分钟得分:" + kpm2, "准度:" + Accuracy2,
                                    "爆头击毙:" + Headshots2]
                    Weapons_str = (' \n'.join(Weapons_list))
                    print('这是爬虫爬取完成后查到的武器数据')
                    return Weapons_str
                except:
                    error = 'ID错误/橘子信息设置为隐私/没用过武器/网络问题,无法查询到最近战绩'
                    return error
            else:
                name = Weapons[0]
                kills = Weapons[1]
                kpm = Weapons[2]
                Accuracy = Weapons[3]
                Headshots = Weapons[4]
                name1 = Weapons[5]
                kills1 = Weapons[6]
                kpm1 = Weapons[7]
                Accuracy1 = Weapons[8]
                Headshots1 = Weapons[9]
                name2 = Weapons[10]
                kills2 = Weapons[11]
                kpm2 = Weapons[12]
                Accuracy2 = Weapons[13]
                Headshots2 = Weapons[14]
                Weapons_list = ["\n烧火棍名称:" + name, "击毙:" + kills, "每分钟得分:" + kpm, "准度:" + Accuracy, "爆头击毙:" + Headshots,
                                "烧火棍名称:" + name1, "击毙:" + kills1, "每分钟得分:" + kpm1, "准度:" + Accuracy1,
                                "爆头击毙:" + Headshots1,
                                "烧火棍名称:" + name2, "击毙:" + kills2, "每分钟得分:" + kpm2, "准度:" + Accuracy2,
                                "爆头击毙:" + Headshots2]
                Weapons_str = (' \n'.join(Weapons_list))
                print('这是直接查数据库查到的武器数据')
                return Weapons_str
    elif Query_Overview == '载具':
        if relevance == ():
            return 'qq号暂未绑定游戏ID,请使用绑定关键字绑定游戏ID 绑定 XXX'
        else:
            Vehicles = Mysql_Select.Select_Vehicles(relevance[0][0])
            if Vehicles == []:
                try:
                    data_Mysql_Insert.get_Vehicles(relevance[0][0])
                    Vehicles = Mysql_Select.Select_Vehicles(relevance[0][0])
                    name = Vehicles[0]
                    kills = Vehicles[1]
                    kpm = Vehicles[2]
                    Destroyed = Vehicles[3]
                    name1 = Vehicles[4]
                    kills1 = Vehicles[5]
                    kpm1 = Vehicles[6]
                    Destroyed1 = Vehicles[7]
                    name2 = Vehicles[8]
                    kills2 = Vehicles[9]
                    kpm2 = Vehicles[10]
                    Destroyed2 = Vehicles[11]
                    Vehicles_list = ["\n载具名称:" + name, "击毙:" + kills, "每分钟得分:" + kpm, "击毁载具:" + Destroyed,
                                     "载具名称:" + name1, "击毙:" + kills1, "每分钟得分:" + kpm1, "击毁载具:" + Destroyed1,
                                     "载具名称:" + name2, "击毙:" + kills2, "每分钟得分:" + kpm2, "击毁载具:" + Destroyed2]
                    Vehicles_str = (' \n'.join(Vehicles_list))
                    print('这是爬虫爬取完成后查到的载具数据')
                    return Vehicles_str
                except:
                    error = 'ID错误/橘子信息设置为隐私/没用过载具,无法查询到数据'
                    return error
            else:
                name = Vehicles[0]
                kills = Vehicles[1]
                kpm = Vehicles[2]
                Destroyed = Vehicles[3]
                name1 = Vehicles[4]
                kills1 = Vehicles[5]
                kpm1 = Vehicles[6]
                Destroyed1 = Vehicles[7]
                name2 = Vehicles[8]
                kills2 = Vehicles[9]
                kpm2 = Vehicles[10]
                Destroyed2 = Vehicles[11]
                Vehicles_list = ["\n载具名称:" + name, "击毙:" + kills, "每分钟得分:" + kpm, "击毁载具:" + Destroyed,
                                 "载具名称:" + name1, "击毙:" + kills1, "每分钟得分:" + kpm1, "击毁载具:" + Destroyed1,
                                 "载具名称:" + name2, "击毙:" + kills2, "每分钟得分:" + kpm2, "击毁载具:" + Destroyed2]
                Vehicles_str = (' \n'.join(Vehicles_list))
                print('这是直接查数据库查到的载具数据')
                return Vehicles_str
    elif Query_Overview == '最近':
        if relevance == ():
            return 'qq号暂未绑定游戏ID,请使用绑定关键字绑定游戏ID 绑定 XXX'
        else:
            try:
                url = "https://battlefieldtracker.com/bf1/profile/pc/{}".format(relevance[0][0])
                headers = {
                    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
                }
                response = requests.get(url, headers=headers, timeout=60)
                html = response.content.decode("utf-8")
                # xpath定位
                xpath = etree.HTML(html)
                # 取出最近战绩
                pattern = '<span data-livestamp="(.*)T'
                Time = re.findall(pattern=pattern, string=html)
                try:
                    Time1 = Time[0]
                    SPM1 = xpath.xpath(
                        "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/text()")[
                        0]
                    Kd1 = xpath.xpath(
                        "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/text()")[
                        0]
                    KPM1 = xpath.xpath(
                        "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[3]/div[1]/text()")[
                        0]
                    try:
                        TimePlayed1 = xpath.xpath(
                            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[6]/div[1]/text()")[
                            0]
                    except:
                        TimePlayed1 = ''

                    try:
                        Time2 = Time[1]
                        SPM2 = xpath.xpath(
                            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/text()")[
                            0]
                        Kd2 = xpath.xpath(
                            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/text()")[
                            0]
                        KPM2 = xpath.xpath(
                            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[1]/text()")[
                            0]
                        try:
                            TimePlayed2 = xpath.xpath(
                                "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[6]/div[1]/text()")[
                                0]
                        except:
                            TimePlayed2 = ''
                    except:
                        Time2 = ''
                        SPM2 = ''
                        Kd2 = ''
                        KPM2 = ''
                        TimePlayed2 = ''

                    try:
                        Time3 = Time[2]
                        SPM3 = xpath.xpath(
                            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[1]/div[1]/text()")[
                            0]
                        Kd3 = xpath.xpath(
                            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[2]/div[1]/text()")[
                            0]
                        KPM3 = xpath.xpath(
                            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[3]/div[1]/text()")[
                            0]
                        try:
                            TimePlayed3 = xpath.xpath(
                                "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[6]/div[1]/text()")[
                                0]
                        except:
                            TimePlayed3 = ''
                    except:
                        Time3 = ''
                        SPM3 = ''
                        Kd3 = ''
                        KPM3 = ''
                        TimePlayed3 = ''
                except:
                    error = 'ID错误/橘子信息设置为隐私/很久没玩,无法查询到最近战绩'
                    return error
                Recent_Sessions_list = ["\n最近战绩:", "游玩时间:" + Time1, "每分钟得分:" + SPM1, "击杀/死亡比:" + Kd1, "每分钟杀敌数:" + KPM1,
                                        "游戏时间:" + TimePlayed1, '================',
                                        "游玩时间:" + Time2, "每分钟得分:" + SPM2, "击杀/死亡比:" + Kd2, "每分钟杀敌数:" + KPM2,
                                        "游戏时间:" + TimePlayed2,
                                        '================',
                                        "游玩时间:" + Time3, "每分钟得分:" + SPM3, "击杀/死亡比:" + Kd3, "每分钟杀敌数:" + KPM3,
                                        "游戏时间:" + TimePlayed3]
                Recent_Sessions_str = (' \n'.join(Recent_Sessions_list))
                return Recent_Sessions_str
            except:
                error = '网络问题请稍后重试'
                return error
    else:
        return '类型只支持:武器、载具、战绩、最近'