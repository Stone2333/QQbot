import requests
from lxml import etree
import re
import Mysql_Select
import data_Mysql_Insert


async def Select_Vehicles(Query_Vehicles: str) -> str:
    Vehicles = Mysql_Select.Select_Vehicles(Query_Vehicles)
    if Vehicles == []:
        try:
            data_Mysql_Insert.get_Vehicles(Query_Vehicles)
            Vehicles = Mysql_Select.Select_Vehicles(Query_Vehicles)
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
        Vehicles_list = ["\n载具名称:" + name, "击杀:" + kills, "KPM:" + kpm, "击毁载具:" + Destroyed,
                         "载具名称:" + name1, "击杀:" + kills1, "KPM:" + kpm1, "击毁载具:" + Destroyed1,
                         "载具名称:" + name2, "击杀:" + kills2, "KPM:" + kpm2, "击毁载具:" + Destroyed2,
                         ]
        Vehicles_str = (' \n'.join(Vehicles_list))
        print('这是直接查数据库查到的载具数据')
        return Vehicles_str