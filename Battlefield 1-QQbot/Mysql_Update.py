import pymysql


# 根据名称更新服务器ID
def Update_Server_Id(servername,serverid):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          UPDATE `server_id` 
          SET serverid = "{}" 
          WHERE servername = "{}"
          '''.format(serverid, servername)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


# 根据游戏名称更新战绩信息
def Update_Overview(name, score_min, kd_ratio, win_percent, kills_game, kills_min, infantry_kpm, infantry_kd, vehicle_kills, vehicle_kpm, skill, accuracy):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          UPDATE `overview` 
          SET  score_min = "{}", kd_ratio = "{}", win_percent = "{}", kills_game = "{}", kills_min = "{}", infantry_kpm = "{}", infantry_kd = "{}",vehicle_kills = "{}", vehicle_kpm = "{}", skill = "{}", accuracy = "{}"
          WHERE name = "{}"
          '''.format(score_min, kd_ratio, win_percent, kills_game, kills_min, infantry_kpm, infantry_kd,vehicle_kills, vehicle_kpm, skill, accuracy, name)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(name, "战绩数据库更新成功")


# 根据游戏名称更新载具信息
def Update_Vehicles(name, vehiclesname, kills, kpm, destroyed, vehiclesname1, kills1, kpm1, destroyed1, vehiclesname2, kills2, kpm2, destroyed2):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          UPDATE `vehicles` 
          SET vehiclesname = "{}", kills = "{}", kpm = "{}", destroyed = "{}", vehiclesname1 = "{}", kills1 = "{}", kpm1 = "{}", destroyed1 = "{}", vehiclesname2 = "{}", kills2 ="{}", kpm2 = "{}", destroyed2 = "{}" 
          WHERE name = "{}"
          '''.format(vehiclesname, kills, kpm, destroyed, vehiclesname1, kills1, kpm1, destroyed1, vehiclesname2, kills2, kpm2, destroyed2, name)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(name, "载具数据库更新成功")


# 根据游戏名称更新武器信息
def Update_Weapons(name, weaponsname, kills, kpm, accuracy, headshots, weaponsname1, kills1, kpm1, accuracy1, headshots1, weaponsname2, kills2, kpm2, accuracy2, headshots2):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          UPDATE `weapons` 
          SET weaponsname = "{}", kills = "{}", kpm = "{}", accuracy = "{}", headshots = "{}", weaponsname1 = "{}",kills1 = "{}", kpm1 = "{}", accuracy1 = "{}", headshots1 = "{}", weaponsname2 = "{}", kills2 = "{}", kpm2 = "{}", accuracy2 = "{}", headshots2 = "{}" 
          WHERE name = "{}"
          '''.format(weaponsname, kills, kpm, accuracy, headshots, weaponsname1, kills1, kpm1, accuracy1, headshots1, weaponsname2, kills2, kpm2, accuracy2, headshots2, name)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(name, "武器数据库更新成功")


# 根据游戏名称更新最近战绩
def Update_Recent_Sessions(name, spm, kd, kpm, timeplayed, spm1, kd1, kpm1, timeplayed1, spm2, kd2, kpm2, timeplayed2):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          UPDATE `recent_sessions` 
          SET spm = "{}", kd = "{}", kpm = "{}", timeplayed = "{}", spm1 = "{}", kd1 = "{}", kpm1 = "{}", timeplayed1 = "{}", spm2 = "{}", kd2 = "{}",kpm2 = "{}", timeplayed2 = "{}"  
          WHERE name = "{}"
          '''.format(spm, kd, kpm, timeplayed, spm1, kd1, kpm1, timeplayed1, spm2, kd2, kpm2, timeplayed2, name)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(name, "最近战绩数据库插入成功")


# 根据服务器名称更新服务器信息
def Update_Servers(servername, name, maplist, prayers):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          UPDATE `server` 
          SET name = "{}", maplist = "{}", prayers = "{}" 
          WHERE ServerName = "{}"
          '''.format(servername, name, maplist, prayers)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(servername, "服务器信息数据库插入成功")

# 根据游戏名称更新游戏名称
def Update_User(name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          UPDATE `user` 
          SET username = "{}" 
          WHERE username = "{}"
          '''.format(name, name)
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