import pymysql

def Select_Server(ServerName):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'SELECT ServerID FROM `server` WHERE ServerName = "{}"'.format(ServerName)
    cursor.execute(sql)
    db.commit()
    a =cursor.fetchall()
    print(a)
    cursor.close()
    db.close()
    for (row,) in a: print(row)


def Select_User():
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'SELECT username FROM `user`'
    print(sql)
    cursor.execute(sql)
    db.commit()
    a = cursor.fetchall()
    print(a)
    cursor.close()
    db.close()

def Select_Overview(name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'SELECT SCORE_MIN,KD_RATIO,WIN_PERCENT,KILLS_GAME,KILLS_MIN,INFANTRY_KPM,INFANTRY_KD,VEHICLE_KILLS,VEHICLE_KPM,SKILL,ACCURACY FROM `overview` WHERE name = "{}"'.format(name)
    print(sql)
    cursor.execute(sql)
    db.commit()
    a = cursor.fetchall()
    b = list(a[0])
    print(b[3])
    cursor.close()
    db.close()

def Select_Vehicles(name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'SELECT VehiclesName, KILLS, KPM, Destroyed, VehiclesName1, KILLS1, KPM1, Destroyed1, VehiclesName2, KILLS2, KPM2, Destroyed2 FROM `vehicles` WHERE name = "{}"'.format(name)
    print(sql)
    cursor.execute(sql)
    db.commit()
    a = cursor.fetchall()
    b = list(a[0])
    print(b[3])
    cursor.close()
    db.close()

def Select_weapons(name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = 'SELECT WeaponsName,KILLS, KPM, Accuracy,Headshots,WeaponsName1,KILLS1,KPM1,Accuracy1,Headshots1,WeaponsName2,KILLS2,KPM2,Accuracy2,Headshots2 FROM `vehicles` WHERE name = "{}"'.format(name)
    print(sql)
    cursor.execute(sql)
    db.commit()
    a = cursor.fetchall()
    b = list(a[0])
    print(b[3])
    cursor.close()
    db.close()


if __name__ == "__main__":
    Select_Server("ZBW")
    Select_User()
    Select_Overview(1)