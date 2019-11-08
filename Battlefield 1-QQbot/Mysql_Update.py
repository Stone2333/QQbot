import pymysql


def Update_Server_Id(ServerName,ServerID):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'UPDATE `server_id` SET ServerID = "{}" WHERE ServerName = "{}"'.format(ServerID, ServerName)
    print(sql)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()



def Update_Overview(name, SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN, INFANTRY_KPM, INFANTRY_KD,VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'UPDATE `overview` SET SCORE_MIN = "{}", KD_RATIO = "{}", WIN_PERCENT = "{}", KILLS_GAME = "{}", KILLS_MIN = "{}", INFANTRY_KPM = "{}", INFANTRY_KD = "{}",VEHICLE_KILLS = "{}", VEHICLE_KPM = "{}", SKILL = "{}", ACCURACY = "{}" where name = "{}"'.format(SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN, INFANTRY_KPM, INFANTRY_KD, VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY, name)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(name, "战绩数据库更新成功")


def Update_Vehicles(name, VehiclesName, KILLS, KPM, Destroyed, VehiclesName1, KILLS1, KPM1, Destroyed1, VehiclesName2, KILLS2, KPM2, Destroyed2):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'UPDATE `vehicles` set VehiclesName = "{}", KILLS = "{}", KPM = "{}", Destroyed = "{}", VehiclesName1 = "{}", KILLS1 = "{}", KPM1 = "{}", Destroyed1 = "{}", VehiclesName2 = "{}", KILLS2 ="{}", KPM2 = "{}", Destroyed2 = "{}" where name = "{}"'.format(VehiclesName, KILLS, KPM, Destroyed, VehiclesName1, KILLS1, KPM1, Destroyed1, VehiclesName2, KILLS2, KPM2, Destroyed2, name)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(name, "载具数据库更新成功")


def Update_Weapons(name, WeaponsName, KILLS, KPM, Accuracy, Headshots, WeaponsName1, KILLS1, KPM1, Accuracy1, Headshots1, WeaponsName2, KILLS2, KPM2, Accuracy2, Headshots2):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'UPDATE `weapons` set WeaponsName = "{}", KILLS = "{}", KPM = "{}", Accuracy = "{}", Headshots = "{}", WeaponsName1 = "{}",KILLS1 = "{}", KPM1 = "{}", Accuracy1 = "{}", Headshots1 = "{}", WeaponsName2 = "{}", KILLS2 = "{}", KPM2 = "{}", Accuracy2 = "{}", Headshots2 = "{}" where name = "{}"'.format(WeaponsName, KILLS, KPM, Accuracy, Headshots, WeaponsName1, KILLS1, KPM1, Accuracy1, Headshots1, WeaponsName2, KILLS2, KPM2, Accuracy2, Headshots2, name)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(name, "武器数据库更新成功")


def Update_Recent_Sessions(name, SPM, KD, KPM, TimePlayed, SPM1, KD1, KPM1, TimePlayed1, SPM2, KD2, KPM2, TimePlayed2):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'UPDATE `recent_sessions` set  SPM = "{}", KD = "{}", KPM = "{}", TimePlayed = "{}", SPM1 = "{}", KD1 = "{}", KPM1 = "{}", TimePlayed1 = "{}", SPM2 = "{}", KD2 = "{}",KPM2 = "{}", TimePlayed2 = "{}" where name = "{}"'.format(SPM, KD, KPM, TimePlayed, SPM1, KD1, KPM1, TimePlayed1, SPM2, KD2, KPM2, TimePlayed2, name)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(name, "最近战绩数据库插入成功")

def Update_Servers(ServerName,Name,Maplist,Prayers):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'UPDATE `server` set Name = "{}", Maplist = "{}", Prayers = "{}" where ServerName = "{}"'.format(Name, Maplist, Prayers, ServerName)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(ServerName, "服务器信息数据库插入成功")

def Update_User(name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'UPDATE `user` set username = "{}" where username = "{}"'.format(name, name)
    print(sql)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(name, "游戏ID信息数据库插入成功")


if __name__ == '__main__':
    Update_User('bf_stonegogogo')



# if __name__ == "__main__":
#     # Update_Server_Id(456, 'zbw')
#     Update_Overview("drunkard50","a","a","a","a","a","a","a","a","a","a","a")
#     Update_Weapons("drunkard50",2,2,1,1,1,1,1,1,1,1,1,1,11,1,1)
#     Update_Vehicles("drunkard50",1,1,1,1,1,1,1,1,1,1,1,1)
#     Update_Recent_Sessions('drunkard50',1,1,1,1,1,1,1,1,1,1,1,1,)
#     Update_Servers("zbw",1,1,1)