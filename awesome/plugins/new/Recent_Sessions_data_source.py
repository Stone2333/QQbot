import requests
import re

import Mysql_Select
import data_Mysql_Insert
import data_Mysql_Update


async def recent_sessions_msg(Quer_Recent_Sessions):
    name = Mysql_Select.get_recent_sessions_all(Quer_Recent_Sessions)
    msg = get_recent_sessions(Quer_Recent_Sessions)
    if msg == '我们找不到您的统计信息，请确保您名称正确':
        return msg
    elif msg == '近期未进行游戏,暂无最近战绩,若进行了游戏没有数据则是网站未更新':
        return msg
    elif msg == '尝试更新统计信息时发生错误,简而言之就是网站挂了,具体啥时间恢复我也不知道':
        return msg
    if not name:
        data_Mysql_Insert.insert_recent_sessions_data(Quer_Recent_Sessions, msg)
        msg = get_db_recent_sessions(Quer_Recent_Sessions)
        return '\n'+msg
    else:
        data_Mysql_Update.update_recent_sessions_data(Quer_Recent_Sessions, msg)
        msg = get_db_recent_sessions(Quer_Recent_Sessions)
        return '\n'+msg


def get_recent_sessions(Quer_Recent_Sessions):
    url = "https://battlefieldtracker.com/bf1/profile/pc/{}".format(Quer_Recent_Sessions)
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    response = requests.get(url, headers=headers, timeout=60)
    html = response.content.decode("utf-8")
    msg = error(html)
    if msg == '我们找不到您的统计信息，请确保您名称正确':
        return msg
    elif msg == '尝试更新统计信息时发生错误,简而言之就是网站挂了,具体啥时间恢复我也不知道':
        return msg
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
击毙/死亡比:{kd}
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