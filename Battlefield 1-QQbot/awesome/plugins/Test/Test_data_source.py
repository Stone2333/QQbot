import Tset_Mysql_Select
import Test_Mysql_Insert


# 调用爬虫插入可能会受网络原因失败 已优化
async def Tset_Select_Overview(Test_Query_Overview: str) -> str:
    Overview = Tset_Mysql_Select.Select_Overview(Test_Query_Overview)
    # 判断数据库中有没有这个ID，有则直接在数据库中查询，没有则调用爬虫爬取插入
    if Overview == []:
        # 调用爬虫爬取插入
        try:
            Test_Mysql_Insert.get_Overview(Test_Query_Overview)
            # 爬取完毕在数据库中查询
            Overview = Tset_Mysql_Select.Select_Overview(Test_Query_Overview)
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
            Overview_list = ["\n游戏ID:" + Test_Query_Overview, SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN,
                             INFANTRY_KPM,
                             INFANTRY_KD,
                             VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY]
            # 去逗号
            Overview_str = (' \n'.join(Overview_list))
            print('这是爬虫爬取完成后查到的战绩数据')
            return Overview_str
        except:
            error = '网络原因请稍候重试'
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
        Overview_list = ["\n游戏ID:" + Test_Query_Overview, SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN, INFANTRY_KPM,INFANTRY_KD,VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY]
        Overview_str = (' \n'.join(Overview_list))
        print('这是直接查数据库查到的战绩数据')
        return Overview_str


async def Tset_Select_Servers_Id(Test_Quer_Servers: str) -> str:
    ServersID = Tset_Mysql_Select.Select_Server_Id(Test_Quer_Servers)
    ServersID_str = ServersID[0]
    return ServersID_str

async def Tset_Select_Servers(Test_Quer_Servers: str) -> str:
    Servers = Tset_Mysql_Select.Select_Server(Test_Quer_Servers)
    if Servers == []:
        try:
            Test_Mysql_Insert.get_Servers(Test_Quer_Servers)
            Servers = Tset_Mysql_Select.Select_Server(Test_Quer_Servers)
            Name = Servers[0]
            Maplist = Servers[1]
            Prayers = Servers[2]
            Servers_list = ['\n服务器名称:' + Name, '\n地图:' + Maplist, '\n服务器人数:' + Prayers]
            Servers_str = (''.join(Servers_list))
            print('这是爬虫爬取完成后查到的服务器数据')
            return Servers_str
        except:
            error = '网络原因请稍候重试'
            return error
    else:
        Name = Servers[0]
        Maplist = Servers[1]
        Prayers =Servers[2]
        Servers_list = ['\n服务器名称:' + Name, '\n地图:' + Maplist, '\n服务器人数:' + Prayers]
        Servers_str = (''.join(Servers_list))
        print('这是直接查数据库查到的服务器数据')
        return Servers_str


async def Tset_Select_Weapons(Test_Query_Weapons: str) -> str:
    Weapons = Tset_Mysql_Select.Select_Weapons(Test_Query_Weapons)
    if Weapons == []:
        try:
            Test_Mysql_Insert.get_Weapons(Test_Query_Weapons)
            Weapons = Tset_Mysql_Select.Select_Weapons(Test_Query_Weapons)
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
            Weapons_list = ["\n武器名称:" + name, "击杀:" + kills, "Kpm:" + kpm, "准度:" + Accuracy, "爆头击杀:" + Headshots,
                            "武器名称:" + name1, "击杀:" + kills1, "Kpm:" + kpm1, "准度:" + Accuracy1, "爆头击杀:" + Headshots1,
                            "武器名称:" + name2, "击杀:" + kills2, "Kpm:" + kpm2, "准度:" + Accuracy2, "爆头击杀:" + Headshots2]
            Weapons_str = (' \n'.join(Weapons_list))
            print('这是爬虫爬取完成后查到的武器数据')
            return Weapons_str
        except:
            error = '网络原因请稍候重试'
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
        Weapons_list = ["\n武器名称:" + name, "击杀:" + kills, "Kpm:" + kpm, "准度:" + Accuracy, "爆头击杀:" + Headshots,
                        "武器名称:" + name1, "击杀:" + kills1, "Kpm:" + kpm1, "准度:" + Accuracy1, "爆头击杀:" + Headshots1,
                        "武器名称:" + name2, "击杀:" + kills2, "Kpm:" + kpm2, "准度:" + Accuracy2, "爆头击杀:" + Headshots2]
        Weapons_str = (' \n'.join(Weapons_list))
        print('这是直接查数据库查到的武器数据')
        return Weapons_str


async def Tset_Select_Recent_Sessions(Test_Query_Recent_Sessions: str) -> str:
    Recent_Sessions = Tset_Mysql_Select.Select_Recent_Sessions(Test_Query_Recent_Sessions)
    if Recent_Sessions == []:
        try:
            Test_Mysql_Insert.get_Recent_Sessions(Test_Query_Recent_Sessions)
            Recent_Sessions = Tset_Mysql_Select.Select_Recent_Sessions(Test_Query_Recent_Sessions)
            SPM1 = Recent_Sessions[0]
            KD1 = Recent_Sessions[1]
            KPM1 = Recent_Sessions[2]
            TimePlayed1 = Recent_Sessions[3]
            SPM2 = Recent_Sessions[4]
            KD2 = Recent_Sessions[5]
            KPM2 = Recent_Sessions[6]
            TimePlayed2 = Recent_Sessions[7]
            SPM3 = Recent_Sessions[8]
            KD3 = Recent_Sessions[9]
            KPM3 = Recent_Sessions[10]
            TimePlayed3 = Recent_Sessions[11]
            Recent_Sessions_list = ["\n最近战绩:", "SPM:" + SPM1, "KD:" + KD1, "Kpm:" + KPM1, "游戏时间:" + TimePlayed1,
                                    "\nSPM:" + SPM2, "KD:" + KD2, "Kpm:" + KPM2, "游戏时间:" + TimePlayed2,
                                    "\nSPM:" + SPM3, "KD:" + KD3, "Kpm:" + KPM3, "游戏时间:" + TimePlayed3]
            Recent_Sessions_str = (' \n'.join(Recent_Sessions_list))
            print('这是爬虫爬取完成后查到的最近战绩数据')
            return Recent_Sessions_str
        except:
            error = '网络原因请稍候重试'
            return error
    else:
        SPM1 = Recent_Sessions[0]
        KD1 = Recent_Sessions[1]
        KPM1 = Recent_Sessions[2]
        TimePlayed1 = Recent_Sessions[3]
        SPM2 = Recent_Sessions[4]
        KD2 = Recent_Sessions[5]
        KPM2 = Recent_Sessions[6]
        TimePlayed2 = Recent_Sessions[7]
        SPM3 = Recent_Sessions[8]
        KD3 = Recent_Sessions[9]
        KPM3 = Recent_Sessions[10]
        TimePlayed3 = Recent_Sessions[11]
        Recent_Sessions_list = ["\n最近战绩:", "SPM:" + SPM1, "KD:" + KD1, "Kpm:" + KPM1, "游戏时间:" + TimePlayed1,
                                "\nSPM:" + SPM2, "KD:" + KD2, "Kpm:" + KPM2, "游戏时间:" + TimePlayed2,
                                "\nSPM:" + SPM3, "KD:" + KD3, "Kpm:" + KPM3, "游戏时间:" + TimePlayed3
                                ]
        Recent_Sessions_str = (' \n'.join(Recent_Sessions_list))
        print('这是直接查数据库查到的最近战绩数据')
        return Recent_Sessions_str


async def Tset_Select_Vehicles(Test_Query_Vehicles: str) -> str:
    Vehicles = Tset_Mysql_Select.Select_Vehicles(Test_Query_Vehicles)
    if Vehicles == []:
        try:
            Test_Mysql_Insert.get_Vehicles(Test_Query_Vehicles)
            Vehicles = Tset_Mysql_Select.Select_Vehicles(Test_Query_Vehicles)
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
            Vehicles_list = ["\n载具名称:" + name, "击杀:" + kills, "KPM:" + kpm, "击毁载具:" + Destroyed,
                             "载具名称:" + name1, "击杀:" + kills1, "KPM:" + kpm1, "击毁载具:" + Destroyed1,
                             "载具名称:" + name2, "击杀:" + kills2, "KPM:" + kpm2, "击毁载具:" + Destroyed2]
            Vehicles_str = (' \n'.join(Vehicles_list))
            print('这是爬虫爬取完成后查到的载具数据')
            return Vehicles_str
        except:
            error = '网络原因请稍候重试'
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
        Vehicles_list = ["\n载具名称:" + name, "击杀:" + kills, "KPM:" + kpm, "击毁载具:" + Destroyed,
                         "载具名称:" + name1, "击杀:" + kills1, "KPM:" + kpm1, "击毁载具:" + Destroyed1,
                         "载具名称:" + name2, "击杀:" + kills2, "KPM:" + kpm2, "击毁载具:" + Destroyed2,
                         ]
        Vehicles_str = (' \n'.join(Vehicles_list))
        print('这是直接查数据库查到的载具数据')
        return Vehicles_str


