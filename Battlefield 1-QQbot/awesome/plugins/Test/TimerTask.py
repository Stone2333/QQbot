from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError

import Test_Mysql_Insert
import Tset_Mysql_Select
import Test_data_source
import time

# 定时器
@nonebot.scheduler.scheduled_job('interval', hour='3')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=552546607,
                                 message=f'现在{now.hour}点整啦！')

        Start_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print("开始时间：", Start_Time)
        All_User = Tset_Mysql_Select.Select_All_User()
        for index in range(len(All_User)):
            user_name = All_User[index]
            try:
                Test_Mysql_Insert.get_Weapons(user_name)
            except:
                print('失败', user_name)

            try:
                Test_Mysql_Insert.get_Overview(user_name)
            except:
                print('失败', user_name)

            try:
                Test_Mysql_Insert.get_Vehicles(user_name)
            except:
                print('失败', user_name)
        End_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print("结束时间：", End_Time)

    except CQHttpError:
        pass


# def Timing_task():
#     Start_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
#     print("开始时间：", Start_Time)
#     All_User = Tset_Mysql_Select.Select_All_User()
#     for index in range(len(All_User)):
#         user_name = All_User[index]
#         try:
#             Test_Mysql_Insert.get_Weapons(user_name)
#         except:
#             print('失败', user_name)
#
#         try:
#             Test_Mysql_Insert.get_Overview(user_name)
#         except:
#             print('失败', user_name)
#
#         try:
#             Test_Mysql_Insert.get_Vehicles(user_name)
#         except:
#             print('失败', user_name)
#     End_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
#     print("结束时间：", End_Time)


# if __name__ == '__main__':
#     Timing_task()