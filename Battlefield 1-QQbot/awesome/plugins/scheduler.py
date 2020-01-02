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
# @nonebot.scheduler.scheduled_job('cron', hour='12')
# async def _():
#     bot = nonebot.get_bot()
#     now = datetime.now(pytz.timezone('Asia/Shanghai'))
#     try:
#         await bot.send_group_msg(group_id=552546607,
#                                  message=f'现在{now.hour}点整啦！')
#     except CQHttpError:
#         pass


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


# 每天12点启动定时任务
if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(update, 'cron', hour=12)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass


# if __name__ == '__main__':
#     insert()
    # update()