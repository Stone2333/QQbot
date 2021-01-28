import Mysql_Select
import data_Mysql_Insert


async def Select_Overview(Query_Overview: str) -> str:
    Overview = Mysql_Select.Select_Overview(Query_Overview)
    # 判断数据库中有没有这个ID，有则直接在数据库中查询，没有则调用爬虫爬取插入
    if Overview == []:
        # 调用爬虫爬取插入
        try:
            data_Mysql_Insert.get_Overview(Query_Overview)
            # 爬取完毕在数据库中查询
            SCORE_MIN = "每分钟得多少分:" + Overview[0]
            KD_RATIO = "击毙去世比:" + Overview[1]
            WIN_PERCENT = "胜率:" + Overview[2]
            KILLS_GAME = "每场击毙:" + Overview[3]
            KILLS_MIN = "每分钟干多少:" + Overview[4]
            INFANTRY_KPM = "步兵每分钟干多少:" + Overview[5]
            INFANTRY_KD = "步兵击毙去世比:" + Overview[6]
            VEHICLE_KILLS = "载具击毙:" + Overview[7]
            VEHICLE_KPM = "载具击毙去世比:" + Overview[8]
            ACCURACY = "准度:" + Overview[10]
            Overview_list = ["\n游戏名称:" + Query_Overview, SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN,
                             INFANTRY_KPM, INFANTRY_KD, VEHICLE_KILLS, VEHICLE_KPM, ACCURACY]
            Overview_str = (' \n'.join(Overview_list))
            print('这是爬虫爬取完成后查到的战绩数据')
            return Overview_str
        except:
            error = 'ID错误/橘子信息设置为隐私,无法查询到数据'
            return error
    else:

        SCORE_MIN = "每分钟得多少分:" + Overview[0]
        KD_RATIO = "击毙去世比:" + Overview[1]
        WIN_PERCENT = "胜率:" + Overview[2]
        KILLS_GAME = "每场击毙:" + Overview[3]
        KILLS_MIN = "每分钟干多少:" + Overview[4]
        INFANTRY_KPM = "步兵每分钟干多少:" + Overview[5]
        INFANTRY_KD = "步兵击毙去世比:" + Overview[6]
        VEHICLE_KILLS = "载具击毙:" + Overview[7]
        VEHICLE_KPM = "载具击毙去世比:" + Overview[8]
        ACCURACY = "准度:" + Overview[10]
        Overview_list = ["\n游戏名称:" + Query_Overview, SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN, INFANTRY_KPM,INFANTRY_KD,VEHICLE_KILLS, VEHICLE_KPM, ACCURACY]
        Overview_str = (' \n'.join(Overview_list))
        print('这是直接查数据库查到的战绩数据')
        return Overview_str