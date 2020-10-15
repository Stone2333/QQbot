import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
import time
import data_Mysql_Update
import Mysql_Select
import data_Mysql_Insert
from datetime import datetime as d
from apscheduler.schedulers.blocking import BlockingScheduler
import re
import requests
import json
import sys
import time
import datetime
#sys.path.append('/root/bandwagonhost/PromotionCode/accesscode')
sys.path.append('C:\\QQbot\\awesome\\plugins')
# configpath = os.getcwd().replace('\\plugins','')
# #os.getcwd获得当前工作的目录不包含文件名，等效上面代码运行结果
# sys.path.append(configpath)


# 定时器

#@nonebot.scheduler.scheduled_job(update, 'cron', hour=16, misfire_grace_time=100)
@nonebot.scheduler.scheduled_job('cron', day_of_week='0-4', hour=18, misfire_grace_time=100)
async def _():
    bot = nonebot.get_bot()
    
    try:
        await bot.send_group_msg(group_id=552546607,
                                 message= '[CQ:at,qq=374717284]' + jiancha())
    except CQHttpError:
        pass


# 失败重跑
def retry_running(user_name,type1,type2):
    if type1 == 1:
        retry_times = 0
        retry_count = 4
        if type2 == 1:
            while retry_times < retry_count:
                try:
                    data_Mysql_Update.get_Update_Overview(user_name)
                except:
                    retry_times = retry_times + 1
                    if retry_times == retry_count:
                        print("战绩重跑失败：" + retry_times + user_name)
                        retry_times == 0
                else:
                    retry_times == 0
                    break
        elif type2 == 2:
            while retry_times < retry_count:
                try:
                    data_Mysql_Update.get_Update_Weapons(user_name)
                except:
                    retry_times = retry_times + 1
                    if retry_times == retry_count:
                        print("武器重跑失败：" + retry_times + user_name)
                        retry_times == 0
                else:
                    retry_times == 0
                    break
        elif type2 == 3:
            while retry_times < retry_count:
                try:
                    data_Mysql_Update.get_Update_Vehicles(user_name)
                except:
                    retry_times = retry_times + 1
                    if retry_times == retry_count:
                        print("载具重跑失败：" + retry_times + user_name)
                        retry_times == 0
                else:
                    retry_times == 0
                    break
    elif type1 == 2:
        retry_times = 0
        retry_count = 4
        if type2 == 1:
            while retry_times < retry_count:
                try:
                    data_Mysql_Insert.get_Overview(user_name)
                except:
                    retry_times = retry_times + 1
                    if retry_times == retry_count:
                        print("战绩重跑失败：" + retry_times + user_name)
                        retry_times == 0
                else:
                    retry_times == 0
                    break
        elif type2 == 2:
            while retry_times < retry_count:
                try:
                    data_Mysql_Insert.get_Weapons(user_name)
                except:
                    retry_times = retry_times + 1
                    if retry_times == retry_count:
                        print("武器重跑失败：" + retry_times + user_name)
                        retry_times == 0
                else:
                    retry_times == 0
                    break
        elif type2 == 3:
            while retry_times < retry_count:
                try:
                    data_Mysql_Insert.get_Vehicles(user_name)
                except:
                    retry_times = retry_times + 1
                    if retry_times == retry_count:
                        print("载具重跑失败：" + retry_times + user_name)
                        retry_times == 0
                else:
                    retry_times == 0
                    break


def insert():
    Start_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print("开始时间：", Start_Time)
    All_User = Mysql_Select.synchronous()
    print('数量:'+ str(len(All_User)))
    for index in range(len(All_User)):
        user_name = All_User[index]
        try:
            retry_running(user_name, 2, 1)
            retry_running(user_name, 2, 2)
            retry_running(user_name, 2, 3)
        except:
            pass
    End_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print("结束时间：", End_Time)


def update():
    insert()
    Start_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print("开始时间：", Start_Time)
    All_User = Mysql_Select.Select_All_User()
    print('数量:' + str(len(All_User)))
    for index in range(len(All_User)):
        user_name = All_User[index]
        try:
            retry_running(user_name, 1, 1)
            retry_running(user_name, 1, 2)
            retry_running(user_name, 1, 3)
            time.sleep(1)
        except:
            pass
    End_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print("结束时间：", End_Time)

def getData() -> str:
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    res = requests.get("https://3g.dxy.cn/newh5/view/pneumonia", headers=headers)
    content = res.content.decode(encoding="utf-8", errors="error")
    return content

def queryAll():
    content = getData()
    pattern = re.compile(r'window.getStatisticsService = (.*?)}catch\(e\){}')
    result = pattern.findall(content)
    data = json.loads(result[0])
    queryTime = "查询时间: {}\n".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    updateTime = "更新时间: {}\n".format(datetime.fromtimestamp(data["modifyTime"] / 1000).strftime('%Y-%m-%d %H:%M:%S', ))
    startStr = '全国新型肺炎疫情实时动态：\n'
    try:
        data0Str = '累计确诊:{}例,今日新增{}例\n'.format(data["confirmedCount"],data["confirmedIncr"])
        data1Str = '现存确诊:{}例,今日新增{}例\n'.format(data["currentConfirmedCount"],data["currentConfirmedIncr"])
        data2Str = '现存疑似:{}例,今日新增{}例\n'.format(data["suspectedCount"],data["suspectedIncr"])
        data3Str = '累计治愈:{}例,今日新增{}例\n'.format(data["curedCount"],data["curedIncr"])
        data4Str = '累计重症:{}例,今日新增{}例\n'.format(data["seriousCount"],data["seriousIncr"])
        data5Str = '累计死亡:{}例,今日新增{}例\n'.format(data["deadCount"],data["deadIncr"])
        endStr = "疑似病例数来自国家卫健委数据，目前为全国数据\n数据来源:丁香医生"
        return '{}{}{}{}{}{}{}{}{}{}'.format(queryTime,updateTime,startStr,data0Str,data1Str,data2Str,data3Str,data4Str,data5Str,endStr)
    except:
        data0Str = '累计确诊:{}例\n'.format(data["confirmedCount"])
        data1Str = '现存确诊:{}例\n'.format(data["currentConfirmedCount"])
        data2Str = '现存疑似:{}例\n'.format(data["suspectedCount"])
        data3Str = '累计治愈:{}例\n'.format(data["curedCount"])
        data4Str = '累计重症:{}例\n'.format(data["seriousCount"])
        data5Str = '累计死亡:{}例\n'.format(data["deadCount"])
        endStr = "\n疑似病例数来自国家卫健委数据，目前为全国数据\n数据来源:丁香医生"
        new = "较昨日变化数据：待国家卫健委数据公布中"
        return '{}{}{}{}{}{}{}{}{}{}{}'.format(queryTime, updateTime, startStr, data0Str, data1Str, data2Str, data3Str,
                                             data4Str, data5Str, new, endStr)


def dingxiang():
    import json
    import requests
    import re
    url = "https://3g.dxy.cn/newh5/view/pneumonia"
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    # proxies = {
    #     'http': 'username:password@125.123.122.178:9999',
    # }
    try:
        response = requests.get(url, headers=headers)
        htmlContent = response.content.decode("utf-8")
        # 全国统计
        patt = '"countRemark":"",(.*?),"virus":"该字段已替换为说明1"'
        s = re.findall(string=htmlContent, pattern=patt)
        f = "{%s}" % s[0]
        c = json.loads(f)
        d = c["confirmedCount"]
        e = c["suspectedCount"]
        # 治愈
        f = c["curedCount"]
        g = c["deadCount"]
        k = c["seriousCount"]
        # 截止时间
        # patt = '<div class="title___2d1_B"><span>(.*?)</span><em><img alt="question"'
        # s1 = re.findall(string=htmlContent, pattern=patt)
        # print(s1)
        Start_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        time1 = "查询时间：" + Start_Time + '\n'
        s3 = time1 + '全国新型肺炎疫情实时动态：\n' +'全国确诊:'+str(d)+'例'+',疑似:'+str(e)+'例'+',治愈:'+str(f)+'例'+',重症:'+str(k)+'例'+',死亡:'+str(g)+'例'+'\n'+ '疑似病例数来自国家卫健委数据，目前为全国数据'+'\n数据来源:丁香医生'
        return s3
    except:
        return '页面改版，呼叫石头'


def oaLogin():
    url = 'http://noa.xinyegk.com/login'
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    data = {
        "username": "石文兵",
        "password": "123456",
        "captcha": ""
    }
    response = requests.post(headers=headers, url=url, json=data)
    return response



def getCookies():
    """
    获取OAcookie
    :return:cookie
    """
    response = oaLogin()
    cookies = response.cookies
    cookie = requests.utils.dict_from_cookiejar(cookies)
    return cookie

def getTimestamp():
    timestamp = time.time() * 1000
    patt = '^\d{13}'
    interceptingTimestamp = re.findall(pattern=patt, string=str(timestamp))
    return interceptingTimestamp[0]


def getRz():
    timestamp = getTimestamp()
    nowTime = d.now().strftime('%Y-%m-%d')
    url = 'http://noa.xinyegk.com/logmanagement/lm01/page?deptId=&creator=&logdate={}&_t={}'.format(nowTime, timestamp)
    cookie = getCookies()
    headers = {
        # 'Content-Type': 'application/json, text/plain, */*',
        'Cookie': 'JSESSIONID={}'.format(cookie['JSESSIONID'])
    }
    response = requests.get(headers=headers, url=url)
    responseData = response.json()
    # print(responseData)
    if responseData['data']['total'] == 0:
        print(nowTime + '没写日志')
        return nowTime + '没写日志'
    elif responseData['data']['total'] == 1:
        print(nowTime + '写了日志')
        return nowTime + '写了日志'


def getZb():
    week = d.now().isocalendar()
    timestamp = getTimestamp()
    url = 'http://noa.xinyegk.com/logmanagement/lm02/page?deptId=&creator=&newweek={}&_t={}'.format(week[1], timestamp)
    cookie = getCookies()
    headers = {
        # 'Content-Type': 'application/json, text/plain, */*',
        'Cookie': 'JSESSIONID={}'.format(cookie['JSESSIONID'])
    }
    response = requests.get(headers=headers, url=url)
    responseData = response.json()
    if responseData['data']['list'] != []:
        print(str(week[0]) + '年' + str(week[1]) + '周' + '写了周报')
        return str(week[0]) + '年' + str(week[1]) + '周' + '写了周报'
    else:
        print(str(week[0]) + '年' + str(week[1]) + '周' + '没写周报')
        return str(week[0]) + '年' + str(week[1]) + '周' + '没写周报'

def jiancha():
    dayOfWeek = d.now().isoweekday()
    if dayOfWeek == 5:
        string = getRz() + '\n' + getZb()
        return string
    else:
        string = getRz()
        return string



# 每天12点启动定时任务
# if __name__ == '__main__':
#     scheduler = BlockingScheduler()
#     scheduler.add_job(update, 'cron', hour=12, misfire_grace_time=100)
#     try:
#         scheduler.start()
#     except (KeyboardInterrupt, SystemExit):
#         pass


# if __name__ == '__main__':
#     dingxiang()
#     insert()
    # update()
