from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError

import Test_Mysql_Update
import Test_Mysql_Select
import time

# 定时器 每5分钟触发一次
# @nonebot.scheduler.scheduled_job('cron', minute='*/5')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=552546607,
                                 message=f'定时任务开始')
        Start_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print("开始时间：", Start_Time)
        All_User = Test_Mysql_Select.Select_All_User()
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

    except CQHttpError:
        pass

# 失败重跑
def retry_running(user_name,type):
    retry_times = 0
    retry_count = 4
    if type == 1:
        while retry_times < retry_count:
            try:
                Test_Mysql_Update.get_Update_Overview(user_name)
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
                Test_Mysql_Update.get_Update_Weapons(user_name)
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
                Test_Mysql_Update.get_Update_Vehicles(user_name)
            except:
                retry_times = retry_times + 1
                if retry_times == retry_count:
                    print("载具重跑失败："+retry_times + user_name)
                    retry_times == 0
            else:
                retry_times == 0
                break

# if __name__ == '__main__':
#     Timing_task()