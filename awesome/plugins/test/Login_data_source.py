import Mysql_Select
import requests
from lxml import etree
import delete
import re
import data_Mysql_Insert
import data_Mysql_Update

async def get_img(qq, Query_Login: str, session) -> str:
    relevance = Mysql_Select.Select_Id(qq)
    if Query_Login == '快速链接':
        s = "www.ceve-market.org/index/"
        return s.strip()
    elif Query_Login == '.最近':
        if relevance == ():
            return 'qq号暂未绑定游戏ID,请使用绑定关键字绑定游戏ID 绑定 XXX'
        else:
            prompt = "查询中请稍候"
            await session.send(prompt)
            name = Mysql_Select.get_recent_sessions_all(relevance[0][0])
            msg = get_recent_sessions(relevance[0][0])
            if msg == '我们找不到您的统计信息，请确保您名称正确':
                name = Mysql_Select.get_recent_sessions_all(relevance[0][0])
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过最近战绩所以没有历史数据'
                msg1 = get_db_recent_sessions(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            elif msg == '近期未进行游戏,暂无最近战绩,若进行了游戏没有数据则是网站未更新':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过最近战绩所以没有历史数据'
                msg1 = get_db_recent_sessions(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            elif msg == '尝试更新统计信息时发生错误,简而言之就是网站挂了,具体啥时间恢复我也不知道':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过最近战绩所以没有历史数据'
                msg1 = get_db_recent_sessions(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            elif msg == '很抱歉,在执行您的要求时发生了一个错误,错误报告已提交给管理员,他们将立即修复该错误!,简而言之也是服务器挂了的一种,恢复时间俺也不知道':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过最近战绩所以没有历史数据'
                msg1 = get_db_recent_sessions(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            elif msg == '战绩网数据库维护,请稍后再试':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过最近战绩所以没有历史数据'
                msg1 = get_db_recent_sessions(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            elif msg == '网络问题,请稍后再试':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过最近战绩所以没有历史数据'
                msg1 = get_db_recent_sessions(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1

            if not name or len(name) < 3:
                if len(name) == 0:
                    data_Mysql_Insert.insert_recent_sessions_data(relevance[0][0], msg)
                    msg = get_db_recent_sessions(relevance[0][0])
                    return '\n' + msg
                else:
                    delete.delete_recent_sessions(relevance[0][0])
                    data_Mysql_Insert.insert_recent_sessions_data(relevance[0][0], msg)
                    msg = get_db_recent_sessions(relevance[0][0])
                    return '\n' + msg
            else:
                data_Mysql_Update.update_recent_sessions_data(relevance[0][0], msg)
                msg = get_db_recent_sessions(relevance[0][0])
                return '\n' + msg

    elif Query_Login == '.战绩':
        if relevance == ():
            return 'qq号暂未绑定游戏ID,请使用绑定关键字绑定游戏ID 绑定 XXX'
        else:
            Overview = Mysql_Select.Select_Overview(relevance[0][0])
            # 判断数据库中有没有这个ID，有则直接在数据库中查询，没有则调用爬虫爬取插入
            if Overview == []:
                # 调用爬虫爬取插入
                try:
                    data_Mysql_Insert.get_Overview(relevance[0][0])
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
                    Overview_list = ["\n游戏ID:" + relevance[0][0], SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME,
                                     KILLS_MIN,
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
                Overview_list = ["\n游戏ID:" + relevance[0][0], SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN,
                                 INFANTRY_KPM, INFANTRY_KD, VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY]
                Overview_str = (' \n'.join(Overview_list))
                print('这是直接查数据库查到的战绩数据')
                return Overview_str
    elif Query_Login == '.武器':
        if relevance == ():
            return 'qq号暂未绑定游戏ID,请使用绑定关键字绑定游戏ID 绑定 XXX'
        else:
            Weapons = Mysql_Select.Select_Weapons(relevance[0][0])
            if Weapons == []:
                try:
                    prompt = "查询中请稍候"
                    await session.send(prompt)
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
    elif Query_Login == '.载具':
        if relevance == ():
            return 'qq号暂未绑定游戏ID,请使用绑定关键字绑定游戏ID 绑定 XXX'
        else:
            Vehicles = Mysql_Select.Select_Vehicles(relevance[0][0])
            if Vehicles == []:
                try:
                    prompt = "查询中请稍候"
                    await session.send(prompt)
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
    elif Query_Login == '帮助':
        s = '[CQ:image,file=file:///C:\\1.png]'
        return s
    else:
        s = '原有快速查询已废弃,输入关键字".最近"，".战绩"，".武器"，".载具"，即可快速查询更为简便'
        return s



def get_recent_sessions(Quer_Recent_Sessions):
    url = "https://battlefieldtracker.com/bf1/profile/pc/{}".format(Quer_Recent_Sessions)
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    response = requests.get(url, headers=headers, timeout=60)
    html = response.content.decode("utf-8")
    msg = error(html)
    msg2 = error2(html)
    msg3 = error3(html)
    msg4 = error4(html)
    if msg == '我们找不到您的统计信息，请确保您名称正确':
        return msg
    elif msg2 == '尝试更新统计信息时发生错误,简而言之就是网站挂了,具体啥时间恢复我也不知道':
        return msg2
    elif msg3 == '很抱歉,在执行您的要求时发生了一个错误,错误报告已提交给管理员,他们将立即修复该错误!,简而言之也是服务器挂了的一种,恢复时间俺也不知道':
        return msg3
    elif msg4 == '战绩网数据库维护,请稍后再试':
        return msg4
    string2 = html.replace('\n', '').replace('\r', '').replace(' ', '')
    # 游玩的日期
    patt = '<spandata-livestamp="(.*?)T'
    game_play_time = re.findall(string=string2, pattern=patt)
    if not game_play_time:
        return '近期未进行游戏,暂无最近战绩,若进行了游戏没有数据则是网站未更新'
    # spm
    patt = '<divclass="session-stats">.*?<div>(.*?)</div>'
    spm = re.findall(string=string2, pattern=patt)
    # spm
    patt = 'Score/Min</div>.*?<div>(.*?)</div><divstyle="min-height:10px;">'
    kd = re.findall(string=string2, pattern=patt)
    # kpm
    patt = 'K/DRatio</div>.*?<div>(.*?)</div><divstyle='
    kpm = re.findall(string=string2, pattern=patt)
    # 游戏时间
    patt = '9b">GameScore</div>.*?<div>(.*?)</div><divstyle='
    game_time = re.findall(string=string2, pattern=patt)
    return game_play_time, spm, kd, kpm, game_time



def get_db_recent_sessions(name):
    msg = Mysql_Select.get_recent_sessions_all(name)
    string2 = ""
    for m in msg:
        spm = m['spm']
        kd = m['kd']
        kpm = m['kpm']
        game_play_time = m['game_play_time']
        game_time = m['game_time']
        string2 += \
f"""游玩日期:{game_play_time}
每分钟得分:{spm}
击毙/去世比:{kd}
每分钟击毙数:{kpm}
游玩时间:{game_time}
===============
"""
    return string2


def error(html):
    string2 = html.replace('\n', '').replace('\r', '').replace(' ', '')
    patt = 'Wecouldnotfindyourstats,pleaseensureyourplatformandnamearecorrect'
    error = re.findall(string=string2, pattern=patt)
    if error:
        print("我们找不到您的统计信息，请确保您名称正确")
        return "我们找不到您的统计信息，请确保您名称正确"
    else:
        pass


def error2(html):
    # 战绩、最近、载具
    string2 = html.replace('\n', '').replace('\r', '').replace(' ', '')
    patt = 'Anerroroccuredwhiletryingtoupdateyourstats.'
    error = re.findall(string=string2, pattern=patt)
    if error:
        print("尝试更新统计信息时发生错误,简而言之就是网站挂了,具体啥时间恢复我也不知道")
        return "尝试更新统计信息时发生错误,简而言之就是网站挂了,具体啥时间恢复我也不知道"
    else:
        pass


def error3(html):
    # 查服务器、查武器
    string2 = html.replace('\n', '').replace('\r', '').replace(' ', '')
    patt = "Sorry,anerroroccurredwhileprocessingyourrequest.Anerrorreporthasbeensubmittedtotheadministratorandthey'llfixitimmediately!"
    error = re.findall(string=string2, pattern=patt)
    if error:
        print("很抱歉,在执行您的要求时发生了一个错误,错误报告已提交给管理员,他们将立即修复该错误!,简而言之也是服务器挂了的一种,恢复时间俺也不知道")
        return "很抱歉,在执行您的要求时发生了一个错误,错误报告已提交给管理员,他们将立即修复该错误!,简而言之也是服务器挂了的一种,恢复时间俺也不知道"
    else:
        pass


def error4(html):
    patt = "We're very sorry for the inconvenience but we&rsquo;re performing database maintenance. Doing this improves the speed and stability of the site.  We do this from time to time to keep things working smoothly."
    error = re.findall(string=html, pattern=patt)
    if error:
        print('战绩网数据库维护,请稍后再试')
        return '战绩网数据库维护,请稍后再试'