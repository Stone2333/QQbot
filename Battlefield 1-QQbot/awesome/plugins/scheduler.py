from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
import time
import Mysql_Select
import data_Mysql_Update

# 定时器
@nonebot.scheduler.scheduled_job('cron', hour='*')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=552546607,
                                 message=f'现在{now.hour}点整啦！')
        await bot.send_group_msg(group_id=864770374,
                                 message=f'憨批机器人为您报时现在{now.hour}点整啦！')
    except CQHttpError:
        pass

# 定时器 每5分钟触发一次
@nonebot.scheduler.scheduled_job('cron', hour='*/12')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=552546607,
                                 message=f'定时任务开始')
        Start_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print("开始时间：", Start_Time)
        All_User = Mysql_Select.Select_All_User()
        for index in range(len(All_User)):
            user_name = All_User[index]
            try:
                retry_running(user_name, 1)
            except:
                print(user_name, '战绩定时任务失败')
            try:
                retry_running(user_name, 2)
            except:
                print(user_name, '武器定时任务失败')
            try:
                retry_running(user_name, 3)
            except:
                print(user_name, '载具定时任务失败')
        End_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print("结束时间：", End_Time)
        await bot.send_group_msg(group_id=552546607,
                                 message=f'定时任务结束')
    except CQHttpError:
        pass

# 失败重跑
def retry_running(user_name,type):
    retry_times = 0
    retry_count = 4
    if type == 1:
        while retry_times < retry_count:
            try:
                data_Mysql_Update.get_Update_Overview(user_name)
            except:
                retry_times = retry_times + 1
                if retry_times == retry_count:
                    print("武器重跑失败："+retry_times + user_name)
                    retry_times == 0
            else:
                retry_times == 0
                break
    elif type == 2:
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
    elif type == 3:
        while retry_times < retry_count:
            try:
                data_Mysql_Update.get_Update_Vehicles(user_name)
            except:
                retry_times = retry_times + 1
                if retry_times == retry_count:
                    print("载具重跑失败："+retry_times + user_name)
                    retry_times == 0
            else:
                retry_times == 0
                break