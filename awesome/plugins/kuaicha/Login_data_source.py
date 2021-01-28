import Mysql_Select
import requests
import delete
import re
import data_Mysql_Insert
import data_Mysql_Update
import Mysql_Insert
import json
import Mysql_Update

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
            prompt = "查询中请稍候"
            await session.send(prompt)
            name = Mysql_Select.get_overview_name(relevance[0][0])
            msg = overview(relevance[0][0])
            if msg == '我们找不到您的统计信息，请确保您名称正确':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过战绩所以没有历史数据'
                msg1 = get_db_overview(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            elif msg == '尝试更新统计信息时发生错误,简而言之就是网站挂了,具体啥时间恢复我也不知道':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过战绩所以没有历史数据'
                msg1 = get_db_overview(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            elif msg == '很抱歉,在执行您的要求时发生了一个错误,错误报告已提交给管理员,他们将立即修复该错误!,简而言之也是服务器挂了的一种,恢复时间俺也不知道':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过战绩所以没有历史数据'
                msg1 = get_db_overview(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            elif msg == '战绩网数据库维护,请稍后再试':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过战绩所以没有历史数据'
                msg1 = get_db_overview(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            elif msg == '网络问题,请稍后再试':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过战绩所以没有历史数据'
                msg1 = get_db_overview(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            if not name:
                rank = msg[0]
                win_percent = msg[1]
                kd = msg[2]
                kpm = msg[3]
                all_kills = msg[4]
                head_shots_odds = msg[5]
                accuracy_ratio = msg[6]
                infantry_kd = msg[7]
                infantry_kpm = msg[8]
                vehicle_kills = msg[9]
                vehicle_kpm = msg[10]
                Mysql_Insert.insert_overview_info(relevance[0][0], rank, win_percent, kd, kpm, all_kills,
                                                  head_shots_odds, accuracy_ratio, infantry_kd, infantry_kpm,
                                                  vehicle_kills, vehicle_kpm)
                msg = get_db_overview(relevance[0][0])
                return '\n' + msg
            else:
                rank = msg[0]
                win_percent = msg[1]
                kd = msg[2]
                kpm = msg[3]
                all_kills = msg[4]
                head_shots_odds = msg[5]
                accuracy_ratio = msg[6]
                infantry_kd = msg[7]
                infantry_kpm = msg[8]
                vehicle_kills = msg[9]
                vehicle_kpm = msg[10]
                Mysql_Update.update_overview_info(relevance[0][0], rank, win_percent, kd, kpm, all_kills,
                                                  head_shots_odds, accuracy_ratio, infantry_kd, infantry_kpm,
                                                  vehicle_kills, vehicle_kpm)
                msg = get_db_overview(relevance[0][0])
                return '\n' + msg
    elif Query_Login == '.武器':
        if relevance == ():
            return 'qq号暂未绑定游戏ID,请使用绑定关键字绑定游戏ID 绑定 XXX'
        else:
            prompt = "查询中请稍候"
            await session.send(prompt)
            name = Mysql_Select.get_weapons_all(relevance[0][0])
            msg = weapons(relevance[0][0])
            if msg == '我们找不到您的统计信息，请确保您名称正确':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
                msg1 = get_db_weapons(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            elif msg == '尝试更新统计信息时发生错误,简而言之就是网站挂了,具体啥时间恢复我也不知道':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
                msg1 = get_db_weapons(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            elif msg == '很抱歉,在执行您的要求时发生了一个错误,错误报告已提交给管理员,他们将立即修复该错误!,简而言之也是服务器挂了的一种,恢复时间俺也不知道':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
                msg1 = get_db_weapons(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            elif msg == '战绩网数据库维护,请稍后再试':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
                msg1 = get_db_weapons(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            elif msg == '网络问题,请稍后再试':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
                msg1 = get_db_weapons(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1

            if not name or len(name) < 3:
                if len(name) == 0:
                    insert_weapons_data(relevance[0][0], msg)
                    msg = get_db_weapons(relevance[0][0])
                    return '\n' + msg
                else:
                    delete.delete_weapons(relevance[0][0])
                    insert_weapons_data(relevance[0][0], msg)
                    msg = get_db_weapons(relevance[0][0])
                    return '\n' + msg
            else:
                update_weapons_data(relevance[0][0], msg)
                msg = get_db_weapons(relevance[0][0])
                return '\n' + msg


    elif Query_Login == '.载具':
        if relevance == ():
            return 'qq号暂未绑定游戏ID,请使用绑定关键字绑定游戏ID 绑定 XXX'
        else:
            prompt = "查询中请稍候"
            await session.send(prompt)
            name = Mysql_Select.get_db_vehicles_all(relevance[0][0])
            msg = vehicles(relevance[0][0])
            if msg == '我们找不到您的统计信息，请确保您名称正确':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
                msg1 = get_db_vehicles(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            elif msg == '尝试更新统计信息时发生错误,简而言之就是网站挂了,具体啥时间恢复我也不知道':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
                msg1 = get_db_vehicles(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            elif msg == '很抱歉,在执行您的要求时发生了一个错误,错误报告已提交给管理员,他们将立即修复该错误!,简而言之也是服务器挂了的一种,恢复时间俺也不知道':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
                msg1 = get_db_vehicles(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            elif msg == '战绩网数据库维护,请稍后再试':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
                msg1 = get_db_vehicles(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
            elif msg == '网络问题,请稍后再试':
                if not name:
                    return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
                msg1 = get_db_vehicles(relevance[0][0])
                return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1

            if not name or len(name) < 3:
                if len(name) == 0:
                    insert_vehicles_data(relevance[0][0], msg)
                    msg = get_db_vehicles(relevance[0][0])
                    return '\n' + msg
                else:
                    delete.delete_vehicles(relevance[0][0])
                    insert_vehicles_data(relevance[0][0], msg)
                    msg = get_db_vehicles(relevance[0][0])
                    return '\n' + msg
            else:
                update_vehicles_data(relevance[0][0], msg)
                msg = get_db_vehicles(relevance[0][0])
                return '\n' + msg

    elif Query_Login == '帮助':
        s = '[CQ:image,file=file:///C:\\1.png]'
        return s
    elif Query_Login == '唯一码':
        s = '[CQ:image,file=file:///C:\\3.png][CQ:image,file=file:///C:\\5.png][CQ:image,file=file:///C:\\4.jpg]'
        return s
    else:
        s = '原有快速查询已废弃,输入关键字".最近"，".战绩"，".武器"，".载具"，即可快速查询更为简便'
        return s

def weapons(name):
    try:
        url = "https://battlefieldtracker.com/bf1/profile/pc/{}/weapons".format(name)
        headers = {
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        html = response.content.decode("utf-8")
    except:
        return '网络问题,请稍后再试'
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
    sting = html.replace('\r', '').replace('\n', '').replace('\t', '').replace('    ', '')
    # 武器名称
    patt = """"><td class="details"><div class="title">(.*?)<a href="/bf1/"""
    weapon_name = re.findall(pattern=patt, string=sting)
    weapon_name = weapon_name[11:14]
    # 击杀数
    patt1 = """<td class="stat detailed" data-val="(.*?)">"""
    weapon_kills = re.findall(pattern=patt1, string=sting)
    weapon_kills = weapon_kills[0:5:2]
    # kpm
    patt2 = """<div class="value">(.*?)</div>"""
    weapon_kpm = re.findall(pattern=patt2, string=sting)
    kpm = weapon_kpm[23:30:3]
    accuracy = weapon_kpm[24:31:3]
    # 爆头
    patt3 = '<td class="stat" data-val="\d+">(.*?)</td>'
    head = re.findall(pattern=patt3, string=sting)
    head_shots = head[:9:3]
    return weapon_name, weapon_kills, kpm, accuracy, head_shots


def get_db_weapons(name):
    msg = Mysql_Select.get_weapons_all(name)
    string2 = ""
    for m in msg:
        weapons_name = m['weapons_name']
        weapons_kills = m['weapons_kills']
        weapons_kpm = m['weapons_kpm']
        weapons_accuracy = m['weapons_accuracy']
        weapons_head_shots_odds = m['weapons_head_shots_odds']
        string2 += f"""烧火棍名称:{weapons_name}
干翻人数:{weapons_kills}
每分钟干翻几个:{weapons_kpm}
准度:{weapons_accuracy}
爆头率:{weapons_head_shots_odds}%
*=============*
"""
    return string2

def insert_weapons_data(name, msg):
    weapons_name = msg[0]
    weapons_kills = msg[1]
    weapons_kpm = msg[2]
    weapons_accuracy = msg[3]
    weapons_head_shots_odds = msg[4]
    for weapons_name, weapons_kills, weapons_kpm, weapons_accuracy, weapons_head_shots in zip(weapons_name, weapons_kills,
                                                                                              weapons_kpm, weapons_accuracy,
                                                                                              weapons_head_shots_odds):
        weapons_head_shots = weapons_head_shots.replace(',', '')
        head_shot = float(weapons_head_shots) / float(weapons_kills) * 100
        head_shot = '%.2f' % head_shot
        Mysql_Insert.insert_weapon(name, weapons_name, weapons_kills, weapons_kpm, weapons_accuracy, head_shot)



def update_weapons_data(name, msg):
    id_tuple = Mysql_Select.get_weapons_id(name)
    weapons_name = msg[0]
    weapons_kills = msg[1]
    weapons_kpm = msg[2]
    weapons_accuracy = msg[3]
    weapons_head_shots_odds = msg[4]
    for id, weapons_name, weapons_kills, weapons_kpm, weapons_accuracy, weapons_head_shots in zip(id_tuple,weapons_name,
                                                                                              weapons_kills,
                                                                                              weapons_kpm,
                                                                                              weapons_accuracy,
                                                                                              weapons_head_shots_odds):
        weapons_head_shots = weapons_head_shots.replace(',', '')
        head_shot = float(weapons_head_shots) / float(weapons_kills) * 100
        head_shot = '%.2f' % head_shot

        Mysql_Update.update_weapons(name, id[0], weapons_name, weapons_kills, weapons_kpm, weapons_accuracy, head_shot)


def get_recent_sessions(Quer_Recent_Sessions):
    url = "https://battlefieldtracker.com/bf1/profile/pc/{}".format(Quer_Recent_Sessions)
    try:
        headers = {
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        html = response.content.decode("utf-8")
    except:
        return '网络问题,请稍后再试'
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


def overview(name):
    """
    获取服务器信息

    :param name:
    :return:
    """
    url_join = "https://battlefieldtracker.com/bf1/profile/pc/" + name
    # url = base_url.format(url1)
    try:
        headers = {
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        # proxies = {
        #     'http': 'username:password@125.123.122.178:9999',
        # }
        response = requests.get(url_join, headers=headers, timeout=10)
        htmlContent = response.content.decode("utf-8")
    except:
        return '网络问题,请稍后再试'
    msg1 = error(htmlContent)
    msg2 = error2(htmlContent)
    msg3 = error3(htmlContent)
    msg4 = error4(htmlContent)
    if msg1 == '我们找不到您的统计信息，请确保您名称正确':
        return msg1
    elif msg2 == '尝试更新统计信息时发生错误,简而言之就是网站挂了,具体啥时间恢复我也不知道':
        return msg2
    elif msg3 == '很抱歉,在执行您的要求时发生了一个错误,错误报告已提交给管理员,他们将立即修复该错误!,简而言之也是服务器挂了的一种,恢复时间俺也不知道':
        return msg3
    elif msg4 == '战绩网数据库维护,请稍后再试':
        return msg4
    string2 = htmlContent.replace('\n', '').replace('\r', '').replace(r' ', '')
    # 等级
    patt4 = '<spanclass="title">Rank(.*?)</span>'
    rank = re.findall(pattern=patt4, string=string2)
    # 总击杀
    patt7 = 'data-stat="Kills">(.*?)</div>'
    all_kills1 = re.findall(pattern=patt7, string=string2)
    all_kills = all_kills1[0]
    int_all_kills = int(all_kills1[0].replace(',', ''))
    # 爆头击杀
    patt8 = 'data-stat="HeadShots">(.*?)</div>'
    head_shots_kills = re.findall(pattern=patt8, string=string2)
    int_head_shots_kills = int(head_shots_kills[0].replace(',', ''))
    # 爆头率
    head_shots_odds = float(int_head_shots_kills / int_all_kills) * float(100)
    head_shots_odds = '%.2f' % head_shots_odds
    patt6 = "varcurrentStatsJson='(.*?)';trnDeltas."
    all = re.findall(pattern=patt6, string=string2)
    all_list = json.loads(all[0])
    all_dict = {}
    for i in all_list:
        name = i['Field']
        number = i['Value']
        all_dict[name] = number
    kd = all_dict['Kd']
    win_percent = all_dict['Wl']
    kpm = all_dict['Kpm']
    # 场均击杀
    infantry_kpm = all_dict['InfantryKpm']
    infantry_kd = all_dict['InfantryKd']
    vehicle_kills = all_dict['VehicleKills']
    vehicle_kpm = all_dict['VehicleKPM']
    # 准度
    accuracy_ratio = all_dict['AccuracyRatio']
    return rank[0], win_percent, kd, kpm, all_kills, head_shots_odds, float(accuracy_ratio) * 100, infantry_kd, infantry_kpm, vehicle_kills, vehicle_kpm


def vehicles(name):
    try:
        url = f"https://battlefieldtracker.com/bf1/profile/pc/{name}/vehicles"
        headers = {
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        # proxies = {
        #     'http': 'username:password@222.89.32.173:9999'
        # }
        response = requests.get(url, headers=headers, timeout=10)
        html = response.content.decode("utf-8")
    except:
        return '网络问题,请稍后再试'
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
    # 名字
    patt = '<trclass=""><tdclass="details"><divclass="title">(.*?)<ahref="'
    vehicles_name_list = re.findall(pattern=patt, string=string2)
    # 载具击杀
    patt2 = '</a></div></td><tdclass="statdetailed"><divclass="value">(.*?)</div><divclass="rank">'
    vehicles_kills_all_list = re.findall(pattern=patt2, string=string2)
    vehicles_kills_list = vehicles_kills_all_list[0:3]
    # kpm
    patt3 = '</div></div></div></div></td><tdclass="statdetailed"><divclass="value">(.*?)</div><divclass="rank">'
    vehicles_kpm_all_list = re.findall(pattern=patt3, string=string2)
    vehicles_kpm_list = vehicles_kpm_all_list[0:3]
    # 击毁
    patt4 = '"></div></div></div></div></td><tdclass="stat">(.*?)</td>'
    vehicles_destroyed_all_list = re.findall(pattern=patt4, string=string2)
    vehicles_destroyed_list = vehicles_destroyed_all_list[0:3]
    # 时间
    patt5 = '\d</td><tdclass="stat">(.*?)</td></tr>'
    vehicles_time_all_list = re.findall(pattern=patt5, string=string2)
    vehicles_time_list = vehicles_time_all_list[0:3]
    return vehicles_name_list, vehicles_kills_list, vehicles_kpm_list, vehicles_destroyed_list, vehicles_time_list


def get_db_vehicles(name):
    msg = Mysql_Select.get_db_vehicles_all(name)
    string2 = ""
    for m in msg:
        vehicles_name = m['vehicles_name']
        vehicles_kills = m['vehicles_kills']
        vehicles_kpm = m['vehicles_kpm']
        vehicles_destroyed = m['vehicles_destroyed']
        vehicles_time = m['vehicles_time']
        string2 += \
f"""载具名称:{vehicles_name}
击毙:{vehicles_kills}
KPM:{vehicles_kpm}
击毁载具:{vehicles_destroyed}
使用时间:{vehicles_time}
===============
"""
    return string2


def get_db_overview(name):
    msg = Mysql_Select.get_db_overview_all(name)
    string2 = ""
    for m in msg:
        rank = m['rank']
        win_percent = m['win_percent']
        kd = m['kd']
        kpm = m['kpm']
        all_kills = m['all_kills']
        head_shots_odds = m['head_shots_odds']
        accuracy_ratio = m['accuracy_ratio']
        infantry_kd = m['infantry_kd']
        infantry_kpm = m['infantry_kpm']
        vehicle_kills = m['vehicle_kills']
        vehicle_kpm = m['vehicle_kpm']
        string2 += f"""等级:{rank}
胜率:{win_percent}%
kd:{kd}
kpm:{kpm}
总击毙:{all_kills}
爆头率:{head_shots_odds}%
准度:{accuracy_ratio}%
步兵kd:{infantry_kd}
步兵kpm:{infantry_kpm}
载具击毙:{vehicle_kills}
载具kpm:{vehicle_kpm}"""
    return string2


def get_db_recent_sessions(name):
    msg = Mysql_Select.get_recent_sessions_all(name)
    string2 = ""
    for m in msg:
        spm = m['spm']
        kd = m['kd']
        kpm = m['kpm']
        game_play_time = m['game_play_time']
        game_time = m['game_time']
        string2 += f"""game_time:{game_play_time}\nspm:{spm}\nkd:{kd}\nkpm:{kpm}\nplay_time:{game_time}\n**===============**\n"""
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

def insert_vehicles_data(name, msg):
    vehicles_name_list = msg[0]
    vehicles_kills_list = msg[1]
    vehicles_kpm_list = msg[2]
    vehicles_destroyed_list = msg[3]
    vehicles_time_list = msg[4]
    for vehicles_name, vehicles_kills, vehicles_kpm_list, vehicles_destroyed, vehicles_time_list in zip(
            vehicles_name_list, vehicles_kills_list, vehicles_kpm_list, vehicles_destroyed_list,
            vehicles_time_list):
        map_dict = {'ASSAULTTANK': '圣沙蒙', 'ASSAULTTRUCK': '菊花车', 'AttackPlane': '攻击机', 'Horse': '马',
                    'Landship': '巡航坦克', 'HEAVYBOMBER': '重型轰炸机', 'LightTank': '轻型坦克', 'HeavyTank': '重型坦克',
                     'StationaryWeapon': '固定武器', 'ArtilleryTruck': '火炮车', 'Behemoth': '巨兽', 'Bomber': '轰炸机'
                      , 'Boat': '船', 'Fighter': '战斗机'}
        Mysql_Insert.insert_vehicles_info(
                name, map_dict[vehicles_name], vehicles_kills, vehicles_kpm_list, vehicles_destroyed, vehicles_time_list)


def update_vehicles_data(name, msg):
    id_tuple = Mysql_Select.get_vehicles_name(name)
    vehicles_name_list = msg[0]
    vehicles_kills_list = msg[1]
    vehicles_kpm_list = msg[2]
    vehicles_destroyed_list = msg[3]
    vehicles_time_list = msg[4]
    for id, vehicles_name, vehicles_kills, vehicles_kpm_list, vehicles_destroyed, vehicles_time_list in zip(
            id_tuple, vehicles_name_list, vehicles_kills_list, vehicles_kpm_list, vehicles_destroyed_list,
            vehicles_time_list):
            map_dict = {'ASSAULTTANK': '圣沙蒙', 'ASSAULTTRUCK': '菊花车', 'AttackPlane': '攻击机', 'Horse': '马',
                    'Landship': '巡航坦克', 'HEAVYBOMBER': '重型轰炸机', 'LightTank': '轻型坦克', 'HeavyTank': '重型坦克',
                    'StationaryWeapon': '固定武器', 'ArtilleryTruck': '火炮车', 'Behemoth': '巨兽', 'Bomber': '轰炸机'
            , 'Boat': '船', 'Fighter': '战斗机'}
            Mysql_Update.update_vehicles_info(
                name, id[0], map_dict[vehicles_name], vehicles_kills, vehicles_kpm_list, vehicles_destroyed, vehicles_time_list)



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