import Mysql_Select
import requests
from lxml import etree
import re

async def get_img(qq, Query_Login: str,) -> str:
    relevance = Mysql_Select.Select_Id(qq)
    if Query_Login == '色图':
        print(Query_Login)
        c = '[CQ:image,file=file:///E:/2.jpg]'
        return c
    elif Query_Login == '吃瓜':
        return '吃瓜'
    elif Query_Login == '快速链接':
        s = "www.ceve-market.org/index/\nwww.baidu.com"
        return s.strip()
    elif Query_Login == '劳动仲裁':
        s = "文档：劳动仲裁和劳动法记录.note\n链接：http://note.youdao.com/noteshare?id=13ef9e3ff1cbcd4cb61b459c3e46cabf&sub=8C73DE805D394DF9A6C58AF74D900D06"
        return  s
    elif Query_Login == '最近':
        if relevance == ():
            return 'qq号暂未绑定游戏ID,请使用绑定关键字绑定游戏ID 绑定 XXX'
        else:
            try:
                url = "https://battlefieldtracker.com/bf1/profile/pc/{}".format(relevance[0][0])
                headers = {
                    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
                }
                response = requests.get(url, headers=headers, timeout=60)
                html = response.content.decode("utf-8")
                # xpath定位
                xpath = etree.HTML(html)
                # 取出最近战绩
                pattern = '<span data-livestamp="(.*)T'
                Time = re.findall(pattern=pattern, string=html)
                try:
                    Time1 = Time[0]
                    SPM1 = xpath.xpath(
                        "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/text()")[
                        0]
                    Kd1 = xpath.xpath(
                        "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/text()")[
                        0]
                    KPM1 = xpath.xpath(
                        "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[3]/div[1]/text()")[
                        0]
                    try:
                        TimePlayed1 = xpath.xpath(
                            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[6]/div[1]/text()")[
                            0]
                    except:
                        TimePlayed1 = ''

                    try:
                        Time2 = Time[1]
                        SPM2 = xpath.xpath(
                            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/text()")[
                            0]
                        Kd2 = xpath.xpath(
                            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/text()")[
                            0]
                        KPM2 = xpath.xpath(
                            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[1]/text()")[
                            0]
                        try:
                            TimePlayed2 = xpath.xpath(
                                "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[6]/div[1]/text()")[
                                0]
                        except:
                            TimePlayed2 = ''
                    except:
                        Time2 = ''
                        SPM2 = ''
                        Kd2 = ''
                        KPM2 = ''
                        TimePlayed2 = ''

                    try:
                        Time3 = Time[2]
                        SPM3 = xpath.xpath(
                            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[1]/div[1]/text()")[
                            0]
                        Kd3 = xpath.xpath(
                            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[2]/div[1]/text()")[
                            0]
                        KPM3 = xpath.xpath(
                            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[3]/div[1]/text()")[
                            0]
                        try:
                            TimePlayed3 = xpath.xpath(
                                "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[6]/div[1]/text()")[
                                0]
                        except:
                            TimePlayed3 = ''
                    except:
                        Time3 = ''
                        SPM3 = ''
                        Kd3 = ''
                        KPM3 = ''
                        TimePlayed3 = ''
                except:
                    error = 'ID错误/橘子信息设置为隐私/很久没玩,无法查询到最近战绩'
                    return error
                Recent_Sessions_list = ["\n最近战绩:", "游玩时间:" + Time1, "每分钟得分:" + SPM1, "击杀/死亡比:" + Kd1, "每分钟杀敌数:" + KPM1,
                                        "游戏时间:" + TimePlayed1, '================',
                                        "游玩时间:" + Time2, "每分钟得分:" + SPM2, "击杀/死亡比:" + Kd2, "每分钟杀敌数:" + KPM2,
                                        "游戏时间:" + TimePlayed2,
                                        '================',
                                        "游玩时间:" + Time3, "每分钟得分:" + SPM3, "击杀/死亡比:" + Kd3, "每分钟杀敌数:" + KPM3,
                                        "游戏时间:" + TimePlayed3]
                Recent_Sessions_str = (' \n'.join(Recent_Sessions_list))
                return Recent_Sessions_str
            except:
                error = '网络问题请稍后重试'
                return error