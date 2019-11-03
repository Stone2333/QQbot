import pymysql


def Insert_Server_Id(ServerName,ServerID):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'INSERT INTO `server` (ServerName,ServerID) VALUES ("{}","{}") '.format(ServerName,ServerID)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print("服务器ID数据库插入成功")


def Insert_User(name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'INSERT INTO `user` (username) VALUES ("{}") '.format(name)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print("游戏ID数据库插入成功")


def Insert_Overview(name, SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN, INFANTRY_KPM, INFANTRY_KD,VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'INSERT INTO `overview` (name, SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN, INFANTRY_KPM, INFANTRY_KD,VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}") '.format(name, SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN, INFANTRY_KPM, INFANTRY_KD, VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print("战绩数据库插入成功")


def Insert_Vehicles(name, VehiclesName, KILLS, KPM, Destroyed, VehiclesName1, KILLS1, KPM1, Destroyed1, VehiclesName2, KILLS2, KPM2, Destroyed2):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'INSERT INTO `vehicles` (name, VehiclesName, KILLS, KPM, Destroyed, VehiclesName1, KILLS1, KPM1, Destroyed1, VehiclesName2, KILLS2, KPM2, Destroyed2) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}") '.format(
        name, VehiclesName, KILLS, KPM, Destroyed, VehiclesName1, KILLS1, KPM1, Destroyed1, VehiclesName2, KILLS2, KPM2, Destroyed2)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print("载具数据库插入成功")


def Insert_Weapons(name, WeaponsName, KILLS, KPM, Accuracy, Headshots, WeaponsName1, KILLS1, KPM1, Accuracy1, Headshots1, WeaponsName2, KILLS2, KPM2, Accuracy2, Headshots2):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'INSERT INTO `weapons` (name, WeaponsName,KILLS, KPM, Accuracy,Headshots,WeaponsName1,KILLS1,KPM1,Accuracy1,Headshots1,WeaponsName2,KILLS2,KPM2,Accuracy2,Headshots2) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}") '.format(name, WeaponsName, KILLS, KPM, Accuracy, Headshots, WeaponsName1, KILLS1, KPM1, Accuracy1, Headshots1, WeaponsName2, KILLS2, KPM2, Accuracy2, Headshots2)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print("武器数据库插入成功")


def Insert_Recent_Sessions(name, SPM, KD, KPM, TimePlayed, SPM1, KD1, KPM1, TimePlayed1, SPM2, KD2, KPM2, TimePlayed2):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'INSERT INTO `recent_sessions` (name, SPM,KD,KPM,TimePlayed,SPM1,KD1,KPM1,TimePlayed1,SPM2, KD2, KPM2, TimePlayed2) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}") '.format(name, SPM, KD, KPM, TimePlayed, SPM1, KD1, KPM1, TimePlayed1, SPM2, KD2, KPM2, TimePlayed2)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print("最近战绩数据库插入成功")


def Insert_Servers(ServerName,Name,Maplist,Prayers):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'INSERT INTO `server` (ServerName, Name, Maplist, Prayers) VALUES ("{}","{}","{}","{}") '.format(ServerName,
        Name, Maplist, Prayers)
    print(sql)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print("服务器信息数据库插入成功")
