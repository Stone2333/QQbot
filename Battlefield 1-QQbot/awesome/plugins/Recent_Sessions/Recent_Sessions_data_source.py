import requests
from lxml import etree
import re


async def get_Recent_Sessions(Quer_Recent_Sessions: str) -> str:
    try:
        url = "https://battlefieldtracker.com/bf1/profile/pc/{}".format(Quer_Recent_Sessions)
        headers = {
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        response = requests.get(url, headers=headers,timeout=60)
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
        Recent_Sessions_list = ["\n最近战绩:", "游玩时间:" + Time1, "SPM:" + SPM1, "KD:" + Kd1, "Kpm:" + KPM1,
                                "游戏时间:" + TimePlayed1,
                                "\n游玩时间:" + Time2, "SPM:" + SPM2, "KD:" + Kd2, "Kpm:" + KPM2, "游戏时间:" + TimePlayed2,
                                "\n游玩时间:" + Time3, "SPM:" + SPM3, "KD:" + Kd3, "Kpm:" + KPM3, "游戏时间:" + TimePlayed3]
        Recent_Sessions_str = (' \n'.join(Recent_Sessions_list))
        return Recent_Sessions_str
    except:
        error = '网络问题请稍后重试'
        return error
