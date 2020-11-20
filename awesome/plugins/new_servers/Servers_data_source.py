import requests
import re
import Mysql_Select
import Mysql_Insert
import Mysql_Update


async def get_Servers(server_name: str) -> str:
    name = Mysql_Select.Select_Server_Id(server_name)
    if name:
        request_server = server(name)
        server_db_name = Mysql_Select.get_server_name(server_name)
        if request_server == '我们找不到您的统计信息，请确保您名称正确':
            server_name_info = Mysql_Select.get_server_name(server_name)
            if not server_name_info:
                return '\n' + server_name_info + '\n' + '由于没有查询过服务器所以没有历史数据'
            server_info = get_db_server_info(server_name)
            return '\n' + request_server + '\n' + '以下数据是历史数据仅供参考:' + '\n' + server_info

        elif request_server == '尝试更新统计信息时发生错误,简而言之就是网站挂了,具体啥时间恢复我也不知道':
            server_name_info = Mysql_Select.get_server_name(server_name)
            if not server_name_info:
                return '\n' + server_name_info + '\n' + '由于没有查询过服务器所以没有历史数据'
            server_info = get_db_server_info(server_name)
            return '\n' + request_server + '\n' + '以下数据是历史数据仅供参考:' + '\n' + server_info

        elif request_server == '战绩网数据库维护,请稍后再试':
            server_name_info = Mysql_Select.get_server_name(server_name)
            if not server_name_info:
                return '\n' + server_name_info + '\n' + '由于没有查询过服务器所以没有历史数据'
            server_info = get_db_server_info(server_name)
            return '\n' + request_server + '\n' + '以下数据是历史数据仅供参考:' + '\n' + server_info
        elif request_server == '网络问题,请稍后再试':
            server_name_info = Mysql_Select.get_server_name(server_name)
            if not server_name_info:
                return '\n' + server_name_info + '\n' + '由于没有查询过服务器所以没有历史数据'
            server_info = get_db_server_info(server_name)
            return '\n' + request_server + '\n' + '以下数据是历史数据仅供参考:' + '\n' + server_info

        if not server_db_name:
            name = request_server[0]
            map = request_server[1]
            mode = request_server[2]
            play_number = request_server[3]
            Mysql_Insert.insert_server(server_name, name, map, mode, play_number)
            msg = get_db_server_info(server_name)
            return '\n' + msg
        else:
            name = request_server[0]
            map = request_server[1]
            mode = request_server[2]
            play_number = request_server[3]
            Mysql_Update.update_server(server_name, name, map, mode, play_number)
            msg = get_db_server_info(server_name)
            return '\n' + msg
    else:
        servers_null = "服务器未注册,请联系管理员"
        return servers_null



def server(name):
    """
    获取服务器信息

    :param name:
    :return:
    """
    url_join = "https://battlefieldtracker.com/bf1/servers/pc/" + name[0]
    # url = base_url.format(url1)
    try:
        headers = {
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        # proxies = {
        #     'http': 'username:password@125.123.122.178:9999',
        # }
        response = requests.get(url_join, headers=headers, timeout=60)
        htmlContent = response.content.decode("utf-8")
    except:
        return '网络问题,请稍后再试'
    msg1 = error1(htmlContent)
    msg2 = error2(htmlContent)
    msg3 = error3(htmlContent)
    msg4 = error4(htmlContent)
    msg5 = server_error(htmlContent)
    if msg1 == '我们找不到您的统计信息，请确保您名称正确':
        return msg1
    elif msg2 == '尝试更新统计信息时发生错误,简而言之就是网站挂了,具体啥时间恢复我也不知道':
        return msg2
    elif msg3 == '很抱歉,在执行您的要求时发生了一个错误,错误报告已提交给管理员,他们将立即修复该错误!,简而言之也是服务器挂了的一种,恢复时间俺也不知道':
        return msg3
    elif msg4 == '战绩网数据库维护,请稍后再试':
        return msg4
    elif msg5 == '找不到此服务器的任何信息,服务器可能已被删除或已被赋予新的服务器ID,请及时更新服务器ID':
        return msg5
    # 服务器名称
    string2 = htmlContent.replace('\n', '').replace('\r', '').replace(' ', '')
    patt = '<spanclass="title-string">(.*?)</span><spanclass="badges">'
    name = re.findall(pattern=patt, string=string2)
    new_name = name[0].replace('&#39;', "'")
    # 人数
    patt2 = 'Players</span><spanclass="value">(.*?)</small></span>'
    number = re.findall(pattern=patt2, string=string2)
    play_number = number[0].replace('<small>', '')
    # 地图
    patt3 = '<spanclass="name">Map</span><spanclass="value">(.*)</span></div><div><spanclass="name">Mode'
    map = re.findall(pattern=patt3, string=string2)
    map_list = {'BallroomBlitz': '流血宴厅', 'ArgonneForest': '阿尔贡森林', 'FaoFortress': '法欧堡', 'Suez': '苏伊士',
                'StQuentinScar': '圣康坦的伤痕', 'SinaiDesert': '西奈沙漠', 'Amiens': '亚眠', 'MonteGrappa': '格拉巴山',
                "Empire'sEdge": '帝国边境', 'Passchendaele': '帕斯尚尔', 'Caporetto': '波雷托', 'RiverSomme': '索姆河',
                "Razor'sEdge": '剃刀边缘', 'London Calling': '伦敦的呼唤', 'HeligolandBight': '黑尔戈兰湾', 'Zeebrugge': '泽布吕赫',
                'CapeHelles': '海丽丝岬', 'Achi Baba': '阿奇巴巴', 'Łupków Pass': '武普库夫山口', 'BrusilovKeep': '勃鲁西洛夫关口',
                'Galicia': '加利西亚', 'Albion': '阿尔比恩', 'Tsaritsyn': '察里津', 'VolgaRiver': '窝瓦河', 'Rupture': '决裂',
                'Soissons': '苏瓦松', 'VerdunHeights': '凡尔登高地', 'FortDeVaux': '法乌克斯要塞', 'PrisedeTahure': '攻占托尔',
                'NivelleNights': '尼维尔之夜', "Giant'sShadow": '庞然暗影'}
    new_map = map_list[map[0]]
    # 模式
    patt4 = 'Mode</span><spanclass="value">(.*?)</span></div>'
    mode = re.findall(pattern=patt4, string=string2)
    mode_dict = {'TEAMDEATHMATCH': '团队死斗', 'CONQUEST': '征服', 'SUPPLYDROP': '空投补给',
                 'FRONTLINES': '前线', 'WARPIGEONS': '战争信鸽', 'RUSH': '突袭', 'DOMINATION': '抢攻'}
    new_mode = mode_dict[mode[0]]
    return new_name, play_number, new_map, new_mode



def error1(html):
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


def server_error(html):
    string2 = html.replace('\n', '').replace('\r', '').replace(' ', '')
    patt = '<h4>(.*?)</h4><h6>(.*?)</h6>'
    c = re.findall(pattern=patt, string=string2)
    if c[0] == 'Cannotfindanyinfoforthisserver':
        return '找不到此服务器的任何信息,服务器可能已被删除或已被赋予新的服务器ID,请及时更新服务器ID'
    else:
        pass


def get_db_server_info(name):
    """
    获取数据库信息

    :param name:
    :return:
    """
    db_server_info = Mysql_Select.get_server_info(name)
    server_name = db_server_info[0][0]
    map = db_server_info[0][1]
    mode = db_server_info[0][2]
    play_number = db_server_info[0][3]
    string = f"""
服务器名称:{server_name}
地图:{map}
模式:{mode}
人数:{play_number}    
    """
    return string
