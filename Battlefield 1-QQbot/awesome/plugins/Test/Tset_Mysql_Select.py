import pymysql


def Select_Server_Id(ServerName):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'SELECT ServerID FROM `server_id` WHERE ServerName = "{}"'.format(ServerName)
    cursor.execute(sql)
    db.commit()
    Server_Id_content =cursor.fetchall()
    # 将元组转换成列表
    Server_Id_content_list = list(Server_Id_content[0])
    print(Server_Id_content_list)
    cursor.close()
    db.close()
    return Server_Id_content_list

def Select_Server(ServerName):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'SELECT Name,Maplist,Prayers FROM `server` WHERE ServerName = "{}"'.format(ServerName)
    cursor.execute(sql)
    db.commit()
    Server_content =cursor.fetchall()
    # 将元组转换成列表
    Server_content_list = list(Server_content[0])
    print(Server_content_list)
    cursor.close()
    db.close()
    return Server_content_list


def Select_All_User():
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    # 获取结果为字典
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = 'SELECT username FROM `user`'
    cursor.execute(sql)
    db.commit()
    All_User_content = cursor.fetchall()
    # 讲遍历出的内容拼接成列表
    All_User_content_list = []
    for (row,) in All_User_content:
        All_User_content_list.append(row)
    print(All_User_content_list)
    cursor.close()
    db.close()
    return All_User_content_list


def Select_User(username):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'SELECT username FROM `user` where username="{}"'.format(username)
    cursor.execute(sql)
    db.commit()
    User_content = cursor.fetchall()
    User_content_list = list(User_content[0])
    print(User_content_list)
    cursor.close()
    db.close()
    return User_content_list


def Select_Overview(name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'SELECT SCORE_MIN,KD_RATIO,WIN_PERCENT,KILLS_GAME,KILLS_MIN,INFANTRY_KPM,INFANTRY_KD,VEHICLE_KILLS,VEHICLE_KPM,SKILL,ACCURACY FROM `overview` WHERE name = "{}"'.format(name)
    cursor.execute(sql)
    db.commit()
    Overview_content = cursor.fetchall()
    Overview_content_list = list(Overview_content[0])
    print(Overview_content_list)
    cursor.close()
    db.close()
    return Overview_content_list


def Select_Vehicles(name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'SELECT VehiclesName, KILLS, KPM, Destroyed, VehiclesName1, KILLS1, KPM1, Destroyed1, VehiclesName2, KILLS2, KPM2, Destroyed2 FROM `vehicles` WHERE name = "{}"'.format(name)
    cursor.execute(sql)
    db.commit()
    Vehicles_content = cursor.fetchall()
    Vehicles_content_list = list(Vehicles_content[0])
    print(Vehicles_content_list)
    cursor.close()
    db.close()
    return Vehicles_content_list


def Select_Weapons(name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'SELECT WeaponsName,KILLS, KPM, Accuracy,Headshots,WeaponsName1,KILLS1,KPM1,Accuracy1,Headshots1,WeaponsName2,KILLS2,KPM2,Accuracy2,Headshots2 FROM `weapons` WHERE name = "{}"'.format(name)
    cursor.execute(sql)
    db.commit()
    Weapons_content = cursor.fetchall()
    Weapons_content_list = list(Weapons_content[0])
    print(Weapons_content_list)
    cursor.close()
    db.close()
    return Weapons_content_list


def Select_Recent_Sessions(name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'SELECT SPM,KD,KPM,TimePlayed,SPM1,KD1,KPM1,TimePlayed1,SPM2, KD2, KPM2, TimePlayed2 FROM `recent_sessions` WHERE name = "{}"'.format(name)
    cursor.execute(sql)
    db.commit()
    Recent_Sessions_content = cursor.fetchall()
    Recent_Sessions_content_list = list(Recent_Sessions_content[0])
    print(Recent_Sessions_content_list)
    cursor.close()
    db.close()
    return Recent_Sessions_content_list

# loop = asyncio.get_event_loop()
# tasks = [Select_Overview()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

if __name__ == "__main__":
    Select_Server("ZBW")
    Select_User("BF_StoneGOGOGO")
    Select_All_User()
    Select_Overview("BF_StoneGOGOGO")
    Select_Weapons("BF_StoneGOGOGO")
    Select_Vehicles("BF_StoneGOGOGO")
    Select_Recent_Sessions("BF_StoneGOGOGO")