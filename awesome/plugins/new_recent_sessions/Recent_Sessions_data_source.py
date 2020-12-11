import requests
import re

import Mysql_Select
import data_Mysql_Insert
import data_Mysql_Update
import delete


async def recent_sessions_msg(Quer_Recent_Sessions):
    name = Mysql_Select.get_recent_sessions_all(Quer_Recent_Sessions)
    msg = get_recent_sessions(Quer_Recent_Sessions)
    if msg == '我们找不到您的统计信息，请确保您名称正确':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过最近战绩所以没有历史数据'
        msg1 = get_db_recent_sessions(Quer_Recent_Sessions)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
    elif msg == '近期未进行游戏,暂无最近战绩,若进行了游戏没有数据则是网站未更新':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过最近战绩所以没有历史数据'
        msg1 = get_db_recent_sessions(Quer_Recent_Sessions)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
    elif msg == '尝试更新统计信息时发生错误,简而言之就是网站挂了,具体啥时间恢复我也不知道':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过最近战绩所以没有历史数据'
        msg1 = get_db_recent_sessions(Quer_Recent_Sessions)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
    elif msg == '很抱歉,在执行您的要求时发生了一个错误,错误报告已提交给管理员,他们将立即修复该错误!,简而言之也是服务器挂了的一种,恢复时间俺也不知道':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过最近战绩所以没有历史数据'
        msg1 = get_db_recent_sessions(Quer_Recent_Sessions)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
    elif msg == '战绩网数据库维护,请稍后再试':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过最近战绩所以没有历史数据'
        msg1 = get_db_recent_sessions(Quer_Recent_Sessions)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1
    elif msg == '网络问题,请稍后再试':
        if not name:
            return '\n' + msg + '\n' + '由于没有查询过最近战绩所以没有历史数据'
        msg1 = get_db_recent_sessions(Quer_Recent_Sessions)
        return '\n' + msg + '\n' + '以下数据是历史数据仅供参考:' + '\n' + msg1

    if not name or len(name) < 3:
        if len(name) == 0:
            data_Mysql_Insert.insert_recent_sessions_data(Quer_Recent_Sessions, msg)
            msg = get_db_recent_sessions(Quer_Recent_Sessions)
            return '\n' + msg
        else:
            delete.delete_recent_sessions(Quer_Recent_Sessions)
            data_Mysql_Insert.insert_recent_sessions_data(Quer_Recent_Sessions, msg)
            msg = get_db_recent_sessions(Quer_Recent_Sessions)
            return '\n'+msg
    else:
        data_Mysql_Update.update_recent_sessions_data(Quer_Recent_Sessions, msg)
        msg = get_db_recent_sessions(Quer_Recent_Sessions)
        return '\n'+msg


def get_recent_sessions(Quer_Recent_Sessions):
    try:
        url = "https://battlefieldtracker.com/bf1/profile/pc/{}".format(Quer_Recent_Sessions)
        headers = {
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=15)
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



def get_db_recent_sessions(name):
    msg = Mysql_Select.get_recent_sessions_all(name)
    string2 = ""
    for m in msg:
        spm = m['spm']
        kd = m['kd']
        kpm = m['kpm']
        game_play_time = m['game_play_time']
        game_time = m['game_time']
        string2 +=f"""玩耍日期:{game_play_time}
每分钟干分:{spm}
干和被干比:{kd}
每分钟干多少个:{kpm}
游玩时间:{game_time}
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
