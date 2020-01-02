import pymysql


# 根据服务器名称查询服务器ID
def Select_Server_Id(servername):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          SELECT serverid 
          FROM `server_id` 
          WHERE servername = "{}"
          '''.format(servername)
    cursor.execute(sql)
    db.commit()
    Server_Id_content =cursor.fetchall()
    # 将元组转换成列表
    try:
        Server_Id_content_list = list(Server_Id_content[0])
        print(Server_Id_content_list)
        cursor.close()
        db.close()
    except:
        Server_Id_content_list = list(Server_Id_content)
        print(Server_Id_content_list)
        cursor.close()
        db.close()
    return Server_Id_content_list


# 根据服务器名称查服务器名字、地图、人数信息
def Select_Server(servername):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          SELECT name,maplist,prayers 
          FROM `server` 
          WHERE servername = "{}"
          '''.format(servername)
    cursor.execute(sql)
    db.commit()
    Server_content =cursor.fetchall()
    # 将元组转换成列表
    try:
        Server_content_list = list(Server_content[0])
        print(Server_content_list)
        cursor.close()
        db.close()
    except:
        Server_content_list = list(Server_content)
        print(Server_content_list)
        cursor.close()
        db.close()
    return Server_content_list


# 查询所有游戏名称
def Select_All_User():
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    # 获取结果为字典
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = '''
          SELECT username 
          FROM `user`
          '''
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


# 查询游戏名称
def Select_User(username):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          SELECT username 
          FROM `user` 
          WHERE username="{}"
          '''.format(username)
    cursor.execute(sql)
    db.commit()
    User_content = cursor.fetchall()
    try:
        User_content_list = list(User_content[0])
        print(User_content_list)
        cursor.close()
        db.close()
    except:
        User_content_list = list(User_content)
        print(User_content_list)
        cursor.close()
        db.close()
    return User_content_list


# 根据游戏名称查询战绩信息
def Select_Overview(name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          SELECT score_min, kd_ratio, win_percent, kills_game, kills_min, infantry_kpm, infantry_kd, vehicle_kills, vehicle_kpm, skill, accuracy 
          FROM `overview` 
          WHERE name = "{}"
          '''.format(name)
    cursor.execute(sql)
    db.commit()
    Overview_content = cursor.fetchall()
    try:
        Overview_content_list = list(Overview_content[0])
        print(Overview_content_list)
        cursor.close()
        db.close()
    except:
        Overview_content_list = list(Overview_content)
        print(Overview_content_list)
        cursor.close()
        db.close()
    return Overview_content_list


# 根据游戏名称查询载具信息
def Select_Vehicles(name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          SELECT vehiclesname, kills, kpm, destroyed, vehiclesname1, kills1, kpm1, destroyed1, vehiclesname2, kills2, kpm2, destroyed2
          FROM `vehicles` 
          WHERE name = "{}"
          '''.format(name)
    cursor.execute(sql)
    db.commit()
    Vehicles_content = cursor.fetchall()
    try:
        Vehicles_content_list = list(Vehicles_content[0])
        print(Vehicles_content_list)
        cursor.close()
        db.close()
    except:
        Vehicles_content_list = list(Vehicles_content)
        print(Vehicles_content_list)
        cursor.close()
        db.close()
    return Vehicles_content_list


# 根据游戏名称查询武器信息
def Select_Weapons(name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          SELECT weaponsname, kills, kpm, accuracy, headshots, weaponsname1, kills1, kpm1, accuracy1, headshots1, weaponsname2, kills2, kpm2, accuracy2, headshots2 
          FROM `weapons` 
          WHERE name = "{}"
          '''.format(name)
    cursor.execute(sql)
    db.commit()
    Weapons_content = cursor.fetchall()
    try:
        Weapons_content_list = list(Weapons_content[0])
        print(Weapons_content_list)
        cursor.close()
        db.close()
    except:
        Weapons_content_list = list(Weapons_content)
        print(Weapons_content_list)
        cursor.close()
        db.close()
    return Weapons_content_list


# 根据游戏名称查询最近战绩
def Select_Recent_Sessions(name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          SELECT spm, kd, kpm, timeplayed, spm1, kd1, kpm1, timeplayed1, spm2, kd2, kpm2, timeplayed2
          FROM `recent_sessions` 
          WHERE name = "{}"
          '''.format(name)
    cursor.execute(sql)
    db.commit()
    Recent_Sessions_content = cursor.fetchall()
    try:
        Recent_Sessions_content_list = list(Recent_Sessions_content[0])
        print(Recent_Sessions_content_list)
        cursor.close()
        db.close()
    except:
        Recent_Sessions_content_list = list(Recent_Sessions_content)
        print(Recent_Sessions_content_list)
        cursor.close()
        db.close()
    return Recent_Sessions_content_list


# 游戏名称同步
def synchronous():
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          SELECT user.username 
          FROM user 
          LEFT JOIN overview ON user.username = overview.name 
          LEFT JOIN vehicles ON user.username = vehicles.name
          LEFT JOIN weapons ON user.username = weapons.name
          WHERE overview.`name`IS NULL
          '''
    cursor.execute(sql)
    db.commit()
    Recent_Sessions_content = cursor.fetchall()
    Recent_Sessions_content_list = list(Recent_Sessions_content)
    company_name_list_join = []
    for index in range(len(Recent_Sessions_content_list)):
        company_name_address = list(Recent_Sessions_content_list[index])
        for company_name_address_list in range(len(company_name_address)):
            company_name_list_join.append(company_name_address[company_name_address_list])
    print(company_name_list_join)
    cursor.close()
    db.close()
    return company_name_list_join


if __name__ == "__main__":
    Select_Server("koi")
    Select_Server_Id("koi")
    Select_User("Bear_maio")
    # Select_All_User()
    Select_Overview("Bear_maio")
    Select_Weapons("Bear_maio")
    Select_Vehicles("Bear_maio")
    Select_Recent_Sessions("Bear_maio")