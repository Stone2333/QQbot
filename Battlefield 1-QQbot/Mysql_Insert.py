import pymysql
import test_insert

def Insert_Server(ServerName,ServerID):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'INSERT INTO `server` (ServerName,ServerID) VALUES ("{}","{}") '.format(ServerName,ServerID)
    cursor.execute(sql)
    db.commit()
    cursor.fetchall()
    cursor.close()
    db.close()
    print("服务器插入成功")


async def Insert_user(username):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'INSERT INTO `user` (username) VALUES ("{}") '.format(username)
    cursor.execute(sql)
    db.commit()
    cursor.fetchall()
    cursor.close()
    db.close()
    print("ID插入成功")

async def Insert_overview(name, SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN, INFANTRY_KPM, INFANTRY_KD,VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'INSERT INTO `overview` (name, SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN, INFANTRY_KPM, INFANTRY_KD,VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",) '.format(name, SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN, INFANTRY_KPM, INFANTRY_KD,VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY)
    cursor.execute(sql)
    db.commit()
    cursor.fetchall()
    cursor.close()
    db.close()
    print("战绩插入成功")


async def Insert_vehicles(name, VehiclesName, KILLS, KPM, Destroyed, VehiclesName1, KILLS1, KPM1, Destroyed1, VehiclesName2, KILLS2, KPM2, Destroyed2):
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
    cursor.fetchall()
    cursor.close()
    db.close()
    print("载具插入成功")

async def Insert_weapons(name, WeaponsName,KILLS, KPM, Accuracy,Headshots,WeaponsName1,KILLS1,KPM1,Accuracy1,Headshots1,WeaponsName2,KILLS2,KPM2,Accuracy2,Headshots2):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'INSERT INTO `weapons` (name, WeaponsName,KILLS, KPM, Accuracy,Headshots,WeaponsName1,KILLS1,KPM1,Accuracy1,Headshots1,WeaponsName2,KILLS2,KPM2,Accuracy2,Headshots2) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}") '.format(name, WeaponsName, KILLS, KPM, Accuracy, Headshots,WeaponsName1,KILLS1,KPM1,Accuracy1,Headshots1,WeaponsName2,KILLS2,KPM2,Accuracy2,Headshots2)
    cursor.execute(sql)
    db.commit()
    cursor.fetchall()
    cursor.close()
    db.close()
    print("武器插入成功")
    await test_insert.get_Weapons()

async def Insert_recent_sessions(name,SPM,KD,KPM,TimePlayed,SPM1,KD1,KPM1,TimePlayed1,SPM2, KD2, KPM2, TimePlayed2):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'INSERT INTO `recent_sessions` (name, SPM,KD,KPM,TimePlayed,SPM1,KD1,KPM1,TimePlayed1,SPM2, KD2, KPM2, TimePlayed2) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}") '.format(name,SPM,KD,KPM,TimePlayed,SPM1,KD1,KPM1,TimePlayed1,SPM2, KD2, KPM2, TimePlayed2)
    cursor.execute(sql)
    db.commit()
    print("最近战绩插入成功")
    cursor.fetchall()
    cursor.close()
    db.close()
