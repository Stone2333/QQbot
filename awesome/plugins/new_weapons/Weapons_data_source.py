import Mysql_Select
import Mysql_Update
import Mysql_Insert
import re
import requests
import delete


async def Select_Weapons(Test_Query_Weapons: str) -> str:
    name = Mysql_Select.get_weapons_all(Test_Query_Weapons)
    msg = weapons(Test_Query_Weapons)
    if msg == '我们找不到您的统计信息，请确保您名称正确':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
        msg1 = get_db_weapons(Test_Query_Weapons)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
    elif msg == '尝试更新统计信息时发生错误,简而言之就是网站挂了,具体啥时间恢复我也不知道':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
        msg1 = get_db_weapons(Test_Query_Weapons)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
    elif msg == '很抱歉,在执行您的要求时发生了一个错误,错误报告已提交给管理员,他们将立即修复该错误!,简而言之也是服务器挂了的一种,恢复时间俺也不知道':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
        msg1 = get_db_weapons(Test_Query_Weapons)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
    elif msg == '战绩网数据库维护,请稍后再试':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
        msg1 = get_db_weapons(Test_Query_Weapons)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
    elif msg == '网络问题,请稍后再试':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过载具所以没有历史数据'
        msg1 = get_db_weapons(Test_Query_Weapons)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1

    if not name or len(name) < 3:
        if len(name) == 0:
            insert_weapons_data(Test_Query_Weapons, msg)
            msg = get_db_weapons(Test_Query_Weapons)
            return '\n' + msg
        else:
            delete.delete_weapons(Test_Query_Weapons)
            insert_weapons_data(Test_Query_Weapons, msg)
            msg = get_db_weapons(Test_Query_Weapons)
            return '\n' + msg
    else:
        update_weapons_data(Test_Query_Weapons, msg)
        msg = get_db_weapons(Test_Query_Weapons)
        return '\n' + msg

# Select_Weapons('ziyou_nahan')
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


def error(html):
    string2 = html.replace('\n', '').replace('\r', '').replace(' ', '')
    patt = 'Wecouldnotfindyourstats,pleaseensureyourplatformandnamearecorrect'
    error = re.findall(string=string2, pattern=patt)
    if error:
        print("我们找不到您的统计信息，请确保您名称正确")
        return "我们找不到您的统计信息，请确保您名称正确"
    else:
        print(error)
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


