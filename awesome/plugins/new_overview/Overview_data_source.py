import Mysql_Select
import data_Mysql_Insert
import re
import Mysql_Update
import Mysql_Insert
import requests
import json

async def Select_Overview(Query_Overview: str) -> str:
    name = Mysql_Select.get_overview_name(Query_Overview)
    msg = overview(Query_Overview)
    if msg == '我们找不到您的统计信息，请确保您名称正确':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过战绩所以没有历史数据'
        msg1 = get_db_overview(Query_Overview)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
    elif msg == '尝试更新统计信息时发生错误,简而言之就是网站挂了,具体啥时间恢复我也不知道':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过战绩所以没有历史数据'
        msg1 = get_db_overview(Query_Overview)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
    elif msg == '很抱歉,在执行您的要求时发生了一个错误,错误报告已提交给管理员,他们将立即修复该错误!,简而言之也是服务器挂了的一种,恢复时间俺也不知道':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过战绩所以没有历史数据'
        msg1 = get_db_overview(Query_Overview)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
    elif msg == '战绩网数据库维护,请稍后再试':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过战绩所以没有历史数据'
        msg1 = get_db_overview(Query_Overview)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
    elif msg == '网络问题,请稍后再试':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过战绩所以没有历史数据'
        msg1 = get_db_overview(Query_Overview)
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
        Mysql_Insert.insert_overview_info(Query_Overview, rank, win_percent, kd, kpm, all_kills, head_shots_odds, accuracy_ratio, infantry_kd, infantry_kpm, vehicle_kills, vehicle_kpm)
        msg = get_db_overview(Query_Overview)
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
        Mysql_Update.update_overview_info(Query_Overview, rank, win_percent, kd, kpm, all_kills, head_shots_odds, accuracy_ratio, infantry_kd, infantry_kpm, vehicle_kills, vehicle_kpm)
        msg = get_db_overview(Query_Overview)
        return '\n' + msg




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
        response = requests.get(url_join, headers=headers, timeout=15)
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
    print(int_all_kills)
    # 爆头击杀
    patt8 = 'data-stat="HeadShots">(.*?)</div>'
    head_shots_kills = re.findall(pattern=patt8, string=string2)
    int_head_shots_kills = int(head_shots_kills[0].replace(',', ''))
    print(int_head_shots_kills)
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

Select_Overview('BF_STONEGOGOGO')