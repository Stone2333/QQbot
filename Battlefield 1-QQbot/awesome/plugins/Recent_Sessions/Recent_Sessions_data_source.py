import requests
from lxml import etree
import re


async def get_Recent_Sessions(Quer_Recent_Sessions: str) -> str:
    url = "https://battlefieldtracker.com/bf1/profile/pc/"
    url_join = url + Quer_Recent_Sessions
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    response = requests.get(url_join, headers=headers)
    html = response.content.decode("utf-8")
    # xpath定位
    xpath = etree.HTML(html)
    # 取出最近战绩
    try:
        SPM1 = xpath.xpath("//div[@class='sessions'][1]/div[@class='session-stats']/div[1]/div[1]//text()")[0]
        Kd1 = xpath.xpath(
            "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]//text()")[
            0]
        KPM1 = xpath.xpath("//div[@class='sessions'][1]/div[@class='session-stats']/div[3]/div[1]//text()")[0]
        try:
            TimePlayed1 = xpath.xpath(
                "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[6]/div[1]//text()")[
                0]
        except:
            TimePlayed1 = ''

        try:
            SPM2 = xpath.xpath(
                "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]//text()")[
                0]
            Kd2 = xpath.xpath(
                "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]//text()")[
                0]
            KPM2 = xpath.xpath(
                "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[1]//text()")[
                0]
            try:
                TimePlayed2 = xpath.xpath(
                    "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[6]/div[1]//text()")[
                    0]
            except:
                TimePlayed2 = ''
        except:
            SPM2 = ''
            Kd2 = ''
            KPM2 = ''
            TimePlayed2 = ''

        try:
            SPM3 = xpath.xpath(
                "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[1]/div[1]//text()")[
                0]
            Kd3 = xpath.xpath(
                "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[2]/div[1]//text()")[
                0]
            KPM3 = xpath.xpath(
                "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[3]/div[1]//text()")[
                0]
            try:
                TimePlayed3 = xpath.xpath(
                    "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[6]/div[1]//text()")[
                    0]
            except:
                TimePlayed3 = ''
        except:
            SPM3 = ''
            Kd3 = ''
            KPM3 = ''
            TimePlayed3 = ''

        Recent_Sessions_list = ["\n最近战绩:", "SPM:" + SPM1, "KD:" + Kd1, "Kpm:" + KPM1, "游戏时间:" + TimePlayed1,
             "\nSPM:" + SPM2, "KD:" + Kd2, "Kpm:" + KPM2, "游戏时间:" + TimePlayed2,
             "\nSPM:" + SPM3, "KD:" + Kd3, "Kpm:" + KPM3, "游戏时间:" + TimePlayed3
             ]
        Recent_Sessions_str = (' \n'.join(Recent_Sessions_list))
        return Recent_Sessions_str
    except:
        error = '无法查询到最近战绩'
        return error
