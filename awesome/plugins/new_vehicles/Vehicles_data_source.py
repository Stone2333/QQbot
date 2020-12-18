import Mysql_Select
import data_Mysql_Insert
import Mysql_Update
import Mysql_Insert
import re
import requests
import delete
#
async def Select_Vehicles(Query_Vehicles: str) -> str:
    name = Mysql_Select.get_db_vehicles_all(Query_Vehicles)
    msg = vehicles(Query_Vehicles)
    if msg == '我们找不到您的统计信息，请确保您名称正确':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
        msg1 = get_db_vehicles(Query_Vehicles)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
    elif msg == '尝试更新统计信息时发生错误,简而言之就是网站挂了,具体啥时间恢复我也不知道':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
        msg1 = get_db_vehicles(Query_Vehicles)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
    elif msg == '很抱歉,在执行您的要求时发生了一个错误,错误报告已提交给管理员,他们将立即修复该错误!,简而言之也是服务器挂了的一种,恢复时间俺也不知道':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
        msg1 = get_db_vehicles(Query_Vehicles)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
    elif msg == '战绩网数据库维护,请稍后再试':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
        msg1 = get_db_vehicles(Query_Vehicles)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
    elif msg == '网络问题,请稍后再试':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
        msg1 = get_db_vehicles(Query_Vehicles)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1

    if not name or len(name) < 3:
        if len(name) == 0:
            insert_vehicles_data(Query_Vehicles, msg)
            msg = get_db_vehicles(Query_Vehicles)
            return '\n' + msg
        else:
            delete.delete_vehicles(Query_Vehicles)
            insert_vehicles_data(Query_Vehicles, msg)
            msg = get_db_vehicles(Query_Vehicles)
            return '\n' + msg
    else:
        update_vehicles_data(Query_Vehicles, msg)
        msg = get_db_vehicles(Query_Vehicles)
        return '\n' + msg



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



