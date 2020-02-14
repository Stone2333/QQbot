from datetime import datetime
import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
import time
import Mysql_Select
import data_Mysql_Update
import data_Mysql_Insert
from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

# 定时器
### @nonebot.scheduler.scheduled_job('cron', minutes='*/1',misfire_grace_time=10) @nonebot.scheduler.scheduled_job('cron', minutes='*/1',misfire_grace_time=10)
@nonebot.scheduler.scheduled_job('cron', hour='*',misfire_grace_time=10)

async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        # await bot.send_group_msg(group_id=552546607,
        #                          message=dingxiang())
        await bot.send_group_msg(group_id=458824937,
                                 message=dingxiang())
        await bot.send_group_msg(group_id=729032552,
                                 message=dingxiang())
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


# 每天12点启动定时任务
if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(update, 'cron', hour=12, misfire_grace_time=100)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass


# if __name__ == '__main__':
#     dingxiang()
#     insert()
    # update()