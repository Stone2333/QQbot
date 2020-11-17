import requests
from lxml import etree
import re
import Mysql_Select


async def get_Servers(Quer_Servers: str) -> str:
    name = Mysql_Select.Select_Server_Id(Quer_Servers)
   
    if name != []:
        try:
            url_join = "https://battlefieldtracker.com/bf1/servers/pc/" + name[0]
            # url = base_url.format(url1)
            headers = {
                "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
            }
            # proxies = {
            #     'http': 'username:password@125.123.122.178:9999',
            # }
            response = requests.get(url_join, headers=headers,timeout=60)
            htmlContent = response.content.decode("utf-8")
            msg1 = error1(htmlContent)
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
            pattern = '<div class="quick-info">.*?<span class="value">(.*?)<small>(.*?)</small>'
            # 服务器人数
            html = re.findall(pattern, htmlContent, re.S)
            for val in html:
                Total = val
            Prayers = (''.join(Total))
            xpath = etree.HTML(htmlContent)
            Name = xpath.xpath('/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/h1/span[1]/text()')[0]
            try:
                Map = xpath.xpath('/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div/div[3]/span[2]/text()')[0]
                Maplist = {'Ballroom Blitz': '流血宴厅', 'Argonne Forest': '阿尔贡森林', 'Fao Fortress': '法欧堡', 'Suez': '苏伊士',
                           'St Quentin Scar': '圣康坦的伤痕', 'Sinai Desert': '西奈沙漠', 'Amiens': '亚眠', 'Monte Grappa': '格拉巴山',
                           "Empire's Edge": '帝国边境', 'Passchendaele': '帕斯尚尔', 'Caporetto': '波雷托', 'River Somme': '索姆河',
                           "Razor's Edge": '剃刀边缘', 'London Calling': '伦敦的呼唤', 'Heligoland Bight': '黑尔戈兰湾', 'Zeebrugge': '泽布吕赫',
                           'Cape Helles': '海丽丝岬', 'Achi Baba': '阿奇巴巴', 'Łupków Pass': '武普库夫山口', 'Brusilov Keep': '勃鲁西洛夫关口',
                           'Galicia': '加利西亚', 'Albion': '阿尔比恩', 'Tsaritsyn': '察里津', 'Volga River': '窝瓦河', 'Rupture': '决裂',
                           'Soissons': '苏瓦松', 'Verdun Heights': '凡尔登高地', 'Fort De Vaux': '法乌克斯要塞', 'Prise de Tahure': '攻占托尔',
                           'Nivelle Nights': '尼维尔之夜', "Giant's Shadow": '庞然暗影'}
            except:
                Map = ''
                Maplist = {'': '未知'}
            Servers_list = ['\n服务器名称:' + Name, '\n地图:' + Maplist[Map], '\n服务器人数:' + Prayers]
            Servers_str = (''.join(Servers_list))
            return Servers_str
        except:
            # b = '\n服务器未注册、服务器不存在或网络问题\n可查询服务器列表：\nZBW，711，FAZE，XD233-1#，XD233-2#，FRM5-1#，FRM5-2#，FRM5-3#，QWQ，QVQ,0V0，404-1#，404-2#，404-3#，CDN,KGB-1#,KGB-2#\n查询格式：\n【查服务器】+空格+列表'
            error = '网络问题，未查询到服务器信息，请稍后重试'
            return error
    else:
        Servers_null = "服务器未注册,请联系管理员"
        return Servers_null


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
