import Mysql_Select
import data_Mysql_Insert


async def Select_Weapons(Test_Query_Weapons: str) -> str:
    Weapons = Mysql_Select.Select_Weapons(Test_Query_Weapons)
    if Weapons == []:
        try:
            data_Mysql_Insert.get_Weapons(Test_Query_Weapons)
            Weapons = Mysql_Select.Select_Weapons(Test_Query_Weapons)
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
                            "烧火棍名称:" + name1, "击毙:" + kills1, "每分钟得分:" + kpm1, "准度:" + Accuracy1, "爆头击毙:" + Headshots1,
                            "烧火棍名称:" + name2, "击毙:" + kills2, "每分钟得分:" + kpm2, "准度:" + Accuracy2, "爆头击毙:" + Headshots2]
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
                        "烧火棍名称:" + name1, "击毙:" + kills1, "每分钟得分:" + kpm1, "准度:" + Accuracy1, "爆头击毙:" + Headshots1,
                        "烧火棍名称:" + name2, "击毙:" + kills2, "每分钟得分:" + kpm2, "准度:" + Accuracy2, "爆头击毙:" + Headshots2]
        Weapons_str = (' \n'.join(Weapons_list))
        print('这是直接查数据库查到的武器数据')
        return Weapons_str